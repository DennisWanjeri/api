#!/usr/bin/python3
import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 78, "name": "Joe", "views": 90000},
    {"likes": 100000, "name": "REST API", "views": 1008889},
    {"likes": 2234, "name": "Tim", "views": 10000}
    ]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/6")
print(response.json())
