import requests
import json

URL='http://127.0.0.1:8000/stu/'
data={
    'name':'kashish',
    'roll':101,
    'city':'kanpur'
}

python_data=json.dumps(data)

r=requests.post(url=URL,data=python_data)
d=r.json()
print(d)