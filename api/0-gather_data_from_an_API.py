#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # url base
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = int(argv[1])
    EMPLOYEE_NAME = ""
    msg = 'Employee {} is done with tasks({}/{}):'
    # url (all_user, id_user, todos, cmp_task)
    url_user = '{}user'.format(url)
    url_id = '{}{}'.format(url_user, user_id)
    url_todos = '{}/todos'.format(url_id)
    url_cmp_tk = '{}?completed=true'.format(url_todos)
    response_user = request.get(url_user)
    user_json = responde_user.json()
    for i in user_json:
        if i.get("id") == url_id:
            EMPLOYEE_NAME = i.get("name")
    response_todos = requets.get(url_todos)
    todos_json = response_todos.json()
    DONE_TASKS = []
    for i in todos_json:
        if i.get("userId") == user_id and i.get("completed" is True):
            DONE_TASKS.append(i.get("title"))
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASK = 0
    # response_todos = request.get(url.todos)
    for i in todos_json:
        if i.get("userId") == user_id:
            TOTAL_NUMBER_OF_TASK += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,
                  NUMBER_OF_DONE_TASK,
                  TOTAL_NUMBER_OF_TASK))
    for i in DONE_TASKS:
        print("\t {}".format(i))
