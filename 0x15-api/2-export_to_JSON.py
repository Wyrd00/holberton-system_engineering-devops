#!/usr/bin/python3
'''
    script recording tasks owned by specific employee in JSON format
'''
import requests
from sys import argv
import json

if __name__ == "__main__":
    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(argv[1]))
    user = userRes.json().get('username', None)

    taskR = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    data = {}
    listy = []
    with open('{}.json'.format(argv[1]), 'w', encoding="utf-8") as jsonfile:
        for entry in taskR.json():
            listy.append({"task": entry.get("title"),
                          "completed": entry.get("completed"),
                          "username": user})
        data[argv[1]] = listy
        json.dump(data, jsonfile)
