import requests
from pprint import pprint as pp

HOST = "http://192.168.49.2:30700"
PASSWORD="password"

def get_request(endpoint):
    #session = requests.Session() 
    url = "{host}{endpoint}".format(host=HOST, endpoint=endpoint)
    print("connecting to {}".format(url))
    response = requests.get(url)
    return response.json()

def post_request(payload, endpoint):
    url = "{host}{endpoint}".format(host=HOST, endpoint=endpoint)
    print("connecting to {}".format(url))
    response = requests.post(url, json=payload)
    print(response.content)
    return response.ok

def put_request():
    pass


#print(get_request('/users'))
#print(get_request('/user/1'))

common_names = ['James', 'John', 'Tom', 'Andy', 'Josh', 'Mark', 'David', 'Sam', 'Esther', 'Olivia', 'Daniel']

#for name in common_names:
#    payload = {"name": name, "email": "{}@email.com".format(name), "pwd": name[0:2]+'xyz123'}
#    pp(payload)
#    post_request(payload, '/create')


pp(get_request('/users'))
