
from flask.globals import request
import requests

BASEURL = "http://127.0.0.1:5000/"

data = [{"name": "Aeropress championships 2021", "time": 320, "temperature": 94, "coffee": 30, "water": 300},
        {"name": "Aeropress championships 2020", "time": 180, "temperature": 98, "coffee": 20, "water": 340},
        {"name": "Aeropress championships 2019", "time": 230, "temperature": 88, "coffee": 65, "water": 450}]

for i in range(len(data)):
    response = requests.put(BASEURL + "recipes/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASEURL + "recipes/" + str(1))
print(response.json())
input()
response = requests.patch(BASEURL + "recipes/" + str(1),{"name": "Aeropress champion 2021", "time": 9, "coffee": 30, "water": 90})
print(response.json())
input()
response = requests.get(BASEURL + "recipes/" + str(1))
print(response.json())