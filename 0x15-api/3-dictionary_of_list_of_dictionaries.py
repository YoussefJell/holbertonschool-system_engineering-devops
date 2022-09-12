#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries module"""
from json import dumps
import requests

if __name__ == "__main__":
    endpoint = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(endpoint)).json()
    users_count = len(users)
    employeeDict = {}
    with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
        for i in range(1, users_count):
            employeeName = users[i].get('username')
            todo = requests.get(
                "{}/users/{}/todos".format(endpoint, i)).json()
            row = []
            for elem in todo:
                dict = {
                    "username": employeeName,
                    "task": elem.get('title'),
                    "completed": elem.get('completed')
                }
                row.append(dict)
            employeeDict[i] = row

        file.write(dumps(employeeDict))