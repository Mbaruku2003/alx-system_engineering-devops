#!/usr/bin/python3
"""export data in JSN format."""
import requests
import sys
import json


def export_to_json(employee_id):
    """export data in JSON format."""

    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User  not found")
        return

    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch TODOs data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare the data structure for JSON
    tasks = []
    for todo in todos_data:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        }
        tasks.append(task_info)

    # Create the final JSON structure
    json_data = {str(employee_id): tasks}

    # Write to JSON file
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
