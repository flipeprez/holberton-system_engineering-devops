#!/usr/bin/python3
'''a nice comment'''
import json
import requests
import sys


def todo_done(id):
    '''a nice comment for checker'''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    res_json = response.json()
    employ_name = res_json.get("name")

    url = "https://jsonplaceholder.typicode.com/user/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    tsk_list = []


    for tsk in todos_json:
        tsk_dict = {}
        tsk_dict["tsk"] = tsk.get("title")
        tsk_dict["completed"] = tsk.get("completed")
        tsk_dict["username"] = employ_name
        tsk_list.append(tsk_dict)

    todos = {"{}".format(id): tsk_list}

    f_name = "{}.json".format(id)
    with open(f_name, "a") as fd:
        json.dump(todos, fd)


if __name__ == "__main__":
    todo_done(sys.argv[1])
