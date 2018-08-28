#!/usr/bin/python3
'''
    script using REST API that returns employee TODO list progress
'''
import requests
from sys import argv


if __name__ == "__main__":
    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(argv[1]))
    user = userRes.json().get('name', None)

    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    done = 0
    total = 0
    for task in tasks.json():
        if task.get('completed') is True:
            done += 1
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(user, done, total))
    for t in tasks.json():
        if t.get('completed') is True:
            print("\t{}".format(t.get('title')))
