#!/usr/bin/python3
"""
    returns information about his/her TODO list progress.
"""


import requests
import sys
from sys import argv

if __name__ == "__main__":
    """ base link """
    link = "https://jsonplaceholder.typicode.com/"
    employee_id = argv[1]
    user = requests.get(link + "users/{}".format(employee_id)).json()
    parameters = {"userId": employee_id}
    todos = requests.get(link + "todos", parameters).json()

    task_completed = [t["title"] for t in todos if t.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(task_completed), len(todos)))
    [print("\t {}".format(complete)) for complete in task_completed]
