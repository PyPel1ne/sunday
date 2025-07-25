import asyncio
import logging
import time
import sys

from datetime import datetime, timedelta
from elasticsearch import Elasticsearch, helpers

from asyncua import Client, ua


ES_HOST = {"host": "127.0.0.1", "port": 9200} 
es = Elasticsearch(hosts=[ES_HOST])
        
### Document generator, need name of the index
def doc_generator(record, ind):
    line = record
    yield {
            "_index": ind,
            "_type": "_doc",
            "_source": line
        }     

### main script to collect data, needed OPC server address and port, attributes
async def main():
    url = "opc.tcp://123.1.1.1:1234"
    i = 1
    names = ['Tlak', 'Prud']
    nodes = ['ns=1;s=tlak', 'ns=2;s=prud']  
    async with Client(url=url) as client:
        while True:
            try:
                start = datetime.now()
                params = ua.ReadParameters()
                for node_id_str in nodes:
                    nodeid = ua.NodeId.from_string(node_id_str)
                    attr = ua.ReadValueId()
                    attr.NodeId = nodeid
                    attr.AttributeId = ua.AttributeIds.Value
                    params.NodesToRead.append(attr)
                result = await client.uaclient.read(params)
                timestamp = datetime.utcnow()
                time_ = datetime.now()
                    
                row = {}
                i = 0
                for name in names:
                    row[name] = getattr(result[i],"Value").Value
                    i = i + 1
                row['timestamp'] = timestamp
                row['time'] = time_
               
                index = "Asd_".format(str(datetime.today())[:10])
                body = doc_generator(row, index) ##tuna sa generuje document do ES
                helpers.bulk(es, body)
                        
                if (datetime.now() - start).total_seconds() < 300: #kazdych 300ms
                    delay = abs((datetime.now() - start).total_seconds() - 0.09)
                    time.sleep(delay)
                else:
                    pass
                    
            except asyncio.TimeoutError:
                print("TimeException Error on: {}".format(datetime.now()))
                pass


if __name__ == "__main__":
    print(datetime.now())
    asyncio.run(main())