#!/usr/bin/python3
"""
Script to export data in the csv format, then records tasks
"""
import csv
from requests import get
import sys


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user = get(base_url + 'users/{}'.format(sys.argv[1])).json()
    user_id = sys.argv[1]
    name = user.get('username')
    todo = get(base_url + 'todos', params={'userId': sys.argv[1]}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, name, elem.get("completed"),
                          elem.get("title")]) for elem in todo]
