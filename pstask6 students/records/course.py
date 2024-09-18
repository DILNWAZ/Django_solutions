import requests
import json

URL = "http://127.0.0.1:8000/course_create/"

data = {
    'course_id' : 'c4',
    'title' : 'Python (Django)',
    'decsription' : 'lsaf sdlfa sadlfsa sdfjkaf',
    'instructor' : 'ABC',
    'duration' : '15 360:00:00',
}

json_data = json.dumps(data)
# print("data in python file:",json_data)
r = requests.post(url = URL, data=json_data)