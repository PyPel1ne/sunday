from hashlib import new
import os
from pathlib import Path
import json

def save_new_script(address, frequency, index_name, attributes, script_name, service):
    names, nodes = [], []
    for attribute in attributes:
        names.append(attribute[0].get())
        nodes.append(attribute[1].get())

    source_file_path = f'{os.path.dirname(os.path.abspath("main.py"))}\config\default_scripts\data_loading.txt'
    new_file_path = os.path.join('.\config\data_loading_scripts\\', script_name)

    command = '''mkdir "{}"'''.format(new_file_path)
    os.system(command)
    command = '''COPY "{}" "{}"'''.format(source_file_path, new_file_path)
    os.system(command)

    with open(f'{new_file_path}\data_loading.txt', 'r') as file :
        new_script = file.read()

    # Replace the target string
    new_script = new_script.replace('SERVER_URL', f'"{address}"')
    new_script = new_script.replace('ATTRIBUTES_NAME', str(names))
    new_script = new_script.replace('ATTRIBUTES_NODE', str(nodes))
    new_script = new_script.replace('INDEX_NAME', f'"{index_name}_"')
    new_script = new_script.replace('FREQUENCY', frequency)

    with open(f'{new_file_path}/data_loading.txt', 'w') as file:
        file.write(new_script)

    info = {
        "url": address,
        "names": names,
        "nodes": nodes,
        "index_name": index_name,
        "frequency": frequency
    }

    with open(f'{new_file_path}/{script_name}.json', 'w') as file:
        json.dump(info, file)

    with open(f'{new_file_path}/{script_name}.bat', 'w') as file:
        file.write(f'''@echo off\n
                        ".\\venv\\Scripts\\python.exe" "{new_file_path}/{script_name}.bat"\n
                        pause''')

    file = f'{new_file_path}\\data_loading.txt'
    ext = os.path.realpath(file).split(".")[-1:][0]
    filefinal = file.replace(ext,'')
    filefinal = filefinal.replace('.','')
    filefinal = "." + filefinal + f'_{script_name}.py'
    os.rename(file ,filefinal)

    # if service:
    #     command_service = f'''sc create {script_name} binpath= "{new_file_path}/{script_name}.bat"'''
    #     os.system(command_service)

    return None