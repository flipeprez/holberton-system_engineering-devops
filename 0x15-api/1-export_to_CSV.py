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

    f_name = "{}.csv".format(id)
    
    with open(f_name, "a") as fd:
        for t2 in todos_json:
            comp = t2.get("completed")
            title = t2.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id,
                                                              employ_name,
                                                              comp,
                                                              title)

            fd.write(csv_data)


if __name__ == "__main__":
    todo_done(sys.argv[1])
