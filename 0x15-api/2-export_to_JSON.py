#!/usr/bin/python3
"""
Script to export data in the JSON format, then records employees tasks
"""
import csv
import json
from requests import get
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user = get(base_url + 'users/{}'.format(sys.argv[1])).json()
    user_id = sys.argv[1]
    name = user.get('username')
    todo = get(base_url + 'todos', params={'userId': sys.argv[1]}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": name
            } for t in todo]}, jsonfile)
