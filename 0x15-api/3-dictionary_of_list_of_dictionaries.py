#!/usr/bin/python3
'''
    script that records tasks from all employees in JSON format
'''
import json
import requests

if __name__ == "__main__":
    userRes = requests.get('https://jsonplaceholder.typicode.com/users')
    data = {}
    listy = []
    with open("todo_all_employees.json", 'w', encoding="utf-8") as jsonfile:
        for user in userRes.json():
            user_id = user.get('id')
            taskR = requests.get(
                    'https://jsonplaceholder.typicode.com/users/{}/todos'
                    .format(user_id))
            for entry in taskR.json():
                listy.append({"task": entry.get("title"),
                              "completed": entry.get("completed"),
                              "username": user.get('username')})
                data[user_id] = listy
            listy = []
        json.dump(data, jsonfile)
