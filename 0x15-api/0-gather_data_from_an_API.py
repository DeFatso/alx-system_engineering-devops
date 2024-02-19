#!/usr/bin/python3
"""
Returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Base link
    link = "https://jsonplaceholder.typicode.com/"
    employee_id = argv[1]

    # Fetch user information
    user = requests.get(link + "users/{}".format(employee_id)).json()

    # Fetch TODO list for the employee
    parameters = {"userId": employee_id}
    todos = requests.get(link + "todos", parameters).json()

    # Filter completed tasks and count them
    task_completed = [t["title"] for t in todos if t.get("completed")]

    # Print employee information and completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(task_completed), len(todos)))

    for task_title in task_completed:
        print("\t" + task_title)
