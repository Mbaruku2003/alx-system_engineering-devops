#!/usr/bin/python3
"""we will send files into a csv file after loading the employee contents."""
import requests
import sys
import csv


def export_to_csv(employee_id):
    """finding content and putting it in a csv file."""

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

    # Prepare the CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Write to CSV file
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        # Write each task to the CSV
        for todo in todos_data:
            csv_writer.writerow([employee_id, username, todo['completed'], todo['title']])

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
