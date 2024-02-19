#!/usr/bin/python3
"""
Script to using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests


def fetch_todo_list_progress(employee_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/todos?userId={employee_id}"
    user_url = f"{main_url}/users/{employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data['name']

        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed_tasks = [todo['title'] for todo in todo_data
                           if todo['completed']]
        num_completed_tasks = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks("
              f"{num_completed_tasks}/{total_tasks}): ")
        for task_title in completed_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
