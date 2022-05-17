#!/usr/bin/python3
'''a nice comment'''
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
    number_of_tsk = len(todos_json)

    tsk_completed = 0
    tsk_list = ""

    for tsk in todos_json:
        if tsk.get("completed") is True:
            tsk_completed += 1
            tsk_list += "\t" + tsk.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(employ_name,
                                                          tsk_completed,
                                                          number_of_tsk))
    print(tsk_list[:-1])


if __name__ == "__main__":
    todo_done(sys.argv[1])
