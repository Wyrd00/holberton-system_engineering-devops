#!/usr/bin/python3
"""
    script using REST API that returns employee TODO list progress
"""


import csv
import requests
from sys import argv


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(argv[1])).json()
    task = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        result = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for entry in task:
            result.writerow([int(argv[1]), user.get('username'),
                         entry.get("completed"), entry.get("title")])
