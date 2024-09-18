import json
import requests


# url1="http://127.0.0.1:8000/stu-info/"

# r = requests.get(url = url1)

# data = r.json()

# print(data)

url1="http://127.0.0.1:8000/stu-create/"

data = {
    'name' : 'abdul hanan',
    'roll' : 1125689,
    'city' : 'Lahore'
}

json_data = json.dumps(data)
r = requests.post(url=url1, data=json_data) 

