#!/usr/bin/python3
"""
Script to export data i JSON format and records all employees tasks
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "user").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in get(base_url + "todos",
                           params={"user_id": u.get("id")}).json()]
            for u in user}, jsonfile)
