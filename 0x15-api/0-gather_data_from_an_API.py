#!/usr/bin/python3
"""
Script to using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    todo_url = base_url + "/user/{}/todos".format(argv[1])
    name_id = base_url + "/users/{}".format(argv[1])
    todo_outcome = get(todo_url).json()
    name_outcome = get(name_id).json()

    todo_num = len(todo_outcome)
    todo_complete = len([todo for todo in todo_outcome
                         if todo.get("completed")])
    name = name_outcome.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_outcome:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
