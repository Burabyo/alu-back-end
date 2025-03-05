#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import json
import urllib.request
import sys

if __name__ == "__main__":
    """
    Request user info by employee ID
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    with urllib.request.urlopen(user_url) as response:
        employee = json.loads(response.read().decode())

    """
    Extract employee name
    """
    employee_name = employee.get("name")

    """
    Request user's TODO list
    """
    todos_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
    with urllib.request.urlopen(todos_url) as response:
        employee_todos = json.loads(response.read().decode())

    """
    Dictionary to store task status in boolean format
    """
    tasks = {task["title"]: task["completed"] for task in employee_todos}

    """
    Return name, total number of tasks & completed tasks
    """
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = sum(tasks.values())  # Count completed tasks

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title, completed in tasks.items():
        if completed:
            print("\t {}".format(title))

