#!/usr/bin/python3
'''
    script using REST API that returns employee TODO list progress
'''


import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1])).json()
    completed = []
    total = 0
    for t in tasks:
        if t.get('completed') is True:
            completed.append(t.get('title'))
        total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), total))
    print("\n".join('\t {}'.format(i) for i in completed))
