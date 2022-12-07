#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    # url base
    url_base = 'https://jsonplaceholder.typicode.com/'
    user_id = int(argv[1])
    EMPLOYEE_NAME = ""
    # msg = 'Employee {} is done with tasks({}/{}):'
    # url (all_user, id_user, todos, cmp_task)
    url_user = '{}users'.format(url_base)
    url_id = '{}/{}'.format(url_user, user_id)
    url_todos = '{}todos'.format(url_base)
    url_cmp_tk = '{}?completed=true'.format(url_todos)
    url_todos_userId = '{}?userId={}'.format(url_todos, user_id)
    response_user = requests.get(url_user)

    # user_id
    response_name = requests.get(url_id)
    response_name_json = response_name.json()
    user_name = response_name_json.get("username")

    response_task = requests.get(url_todos_userId)
    response_task_json = response_task.json()
    data_export = []

    for task in response_task_json:
        task_status = task.get("completed")
        task_title = task.get("title")
        data_export.append({"task": task_title,
                            "completed": task_status,
                            "useranme": user_name})

    json_to_export = {"{}".format(user_id): data_export}
    with open("{}.json".format(user_id), "wt") as fs:
        json.dump(json_to_export, fs)
