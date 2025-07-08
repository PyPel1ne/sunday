import json

def authentificate_user(username, password):
    with open(r'.\config\users\users.json') as json_file:
        users = json.load(json_file)
    for roles in users['roles']:
        for user in users['roles'][roles]:
            if user['username'] == username and user['password'] == password:
                return True, roles
    return False, None
