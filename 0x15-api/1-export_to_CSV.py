#!/usr/bin/python3
'''
    script using REST API that returns employee TODO list progress
'''
import csv
import requests
from sys import argv

if __name__ == "__main__":
    userRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(argv[1]))
    user = userRes.json().get('username', None)

    taskR = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        result = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        listy = []
        for entry in taskR.json():
            listy.append([entry.get("userId"), user, entry.get("completed"),
                         entry.get("title")])
            result.writerows(listy)
