#!/usr/bin/python3
"""
    returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    usr = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr).json()
    todo = requests.get(todos).json()

    comp_nb = 0
    total_nb = 0
    completed_tasks = []

    for task in todo:
        total_nb += 1
        if task.get("completed") is True:
            comp_nb += 1
            completed_tasks.append(task.get("title"))

    e = "Employee {} is done with tasks({}/{}):"
    print(e.format(user.get("name"), comp_nb, total_nb))
    for task in completed_tasks:
        print("\t {}".format(task))
