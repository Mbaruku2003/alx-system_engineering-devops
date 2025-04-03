#!/usr/bin/python3
"""We will export our data after imporing it in csv file."""
import requests
import csv
import sys


def export_to_csv(employee_data):
    """we will export data into a csv file."""

    usrurl = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todosurl = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    usrres = requests.get(usrurl)
    if usrres.status_code != 200:
        print("User not found")
        return
    userdata = usrres.json()
    usrname = userdata.get("username")
    todosres = requests.get(todosurl)
    todosdata = todosres.json()

    csv_file = f"{employee_id}.csv"

    #write to csv file
    with open(csv_file, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        #write each task to the csv
        for todo in todosdata:
            csv_writer.writerow([employee_id, usrname, todo['completed'], todo['title']])
    print(f"Data exported to {csv_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
