#!/usr/bin/python3
"""
Script to export data in the csv format, then records tasks
"""
import requests
import sys


def fetch_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data['name']

        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        ended_tasks = [todo['title'] for todo in todos_data
                       if todo['completed']]
        num_completed_tasks = len(ended_tasks)

        print(f"Employee {employee_name} is done with tasks("
              f"{num_completed_tasks}/{total_tasks}): ")
        for task_title in ended_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
