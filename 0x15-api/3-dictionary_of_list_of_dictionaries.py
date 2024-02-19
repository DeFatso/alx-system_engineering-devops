#!/usr/bin/python3
"""
Python script to export all users' to-do list data in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    """ Base URL for the JSONPlaceholder API """
    base_url = "https://jsonplaceholder.typicode.com/"

    """ Get all users from the API """
    users = requests.get(base_url + "users").json()

    """ Create a dictionary to store tasks for all users """
    all_users_tasks = {}

    """ Iterate over each user and fetch their to-do list """
    for user in users:
        user_id = user['id']
        user_name = user['username']
        user_tasks_url = base_url + "todos?userId={}".format(user_id)
        tasks = requests.get(user_tasks_url).json()

        """ Store tasks in the dictionary with user ID as the key """
        user_tasks = []
        for task in tasks:
            task_info = {
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_info)

        all_users_tasks[user_id] = user_tasks

    """ Write the all_users_tasks dictionary to a JSON file """
    json_filename = 'todo_all_employees.json'
    with open(json_filename, 'w') as json_file:
        json.dump(all_users_tasks, json_file)

    """ Print a message indicating successful export """
    print(f"To-do list for all employees exported to {json_filename}")
