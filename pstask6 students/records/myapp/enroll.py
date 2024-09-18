import requests
import json

URL = "http://127.0.0.1:8000/enroll/"

data = {
    'student' : '1007',
    'course' : 'c1',
}

json_data = json.dumps(data)
print("data in python file:",json_data)
r = requests.post(url = URL, data=json_data)