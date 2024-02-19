#!/usr/bin/python3
"""
    Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    """ get id """
    user_id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = ("https://jsonplaceholder.typicode.com/users/{}/todos"
                 .format(user_id))

    """ Make HTTP requests to fetch user and to-do list data """
    user_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    """ Open a CSV file in write mode with a dynamically generated filename """
    csv_filename = '{}.csv'.format(user_id)
    with open(csv_filename, 'w', newline='') as csv_file:
        """ Create a CSV writer with quoting set to QUOTE_ALL """
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        """
        h_row = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csv_writer.writerow(h_row)
        """

        """ Iterate over each to-do item and write to the CSV file """
        for todo in todos_data:
            """ Extract relevant information for each to-do item """
            user_id = user_id
            username = user_data.get("username")
            completed_status = todo.get("completed")
            task_title = todo.get("title")

            """ Convert values to strings, write as a row to the CSV file """
            row = [str(user_id), username, str(completed_status), task_title]
            csv_writer.writerow(row)

    """ Print a message indicating successful export """
    print(f"To-do list for User {user_data.get('name')} "
          f"exported to {csv_filename}")
