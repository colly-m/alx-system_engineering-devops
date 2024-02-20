#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
from requests import get
import sys
import json


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = get(base_url + 'users/{}'.format(sys.argv[1])).json()
    todo = get(base_url + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [title.get("title") for title in todo if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(user_id.get("name"),
                                                          len(completed),
                                                          len(todo)))
    [print("\t {}".format(title)) for title in completed]
