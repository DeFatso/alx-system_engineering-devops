#!/usr/bin/python3
"""
Python script to export user's to-do list data in JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Get user ID from command-line argument """
    user_id = argv[1]

    """ Construct URLs for fetching user and to-do list data """
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = ("https://jsonplaceholder.typicode.com/users/{}/todos"
                 .format(user_id))

    """ Make HTTP requests to fetch user and to-do list data """
    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    """ Create a dictionary to store tasks with user ID as the key """
    user_tasks = {user_id: []}

    """ Iterate over each to-do itemand append to the user_tasks dictionary """
    for todo in todos_data:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_data.get("username")
        }
        user_tasks[user_id].append(task_info)

    """ Write the user_tasks dictionary to a JSON file """
    json_filename = '{}.json'.format(user_id)
    with open(json_filename, 'w') as json_file:
        json.dump(user_tasks, json_file)

    """ Print a message indicating successful export """
    print(f"To-do list for User {user_data.get('name')} "
          f"exported to {json_filename}")
