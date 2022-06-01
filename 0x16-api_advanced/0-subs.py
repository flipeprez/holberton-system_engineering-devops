<<<<<<< HEAD
#!/usr/bin/python3
''' a nice comment'''
import request


def number_of_suscribers(subreddit):
    ''' a nice comments'''
    header = {'user-agent': 'mozilla/100.0.2'}
    url = 'https://api.reddit.com/r/{subreddit}/about.json'.format(subreddit)
    response = request.get(url, headers=header)
    if response.status_code == 200:
        sub = response.json()['data']['suscribers']
=======
from importlib import import_module
import requests


def number_of_subscribers(subreddit):
    ''' Finds the number of subscribers in a subreddit '''

    header = {'User-Agent':  'mozilla/100.0.2'}
    url = "https://api.reddit.com/r/{subreddit}/about.json".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        subs = response.json()["data"]["subscribers"]
>>>>>>> b9c049f59e4769fe91c05d9c4368e4b83dfcd89e
    else:
        subs = 0
    return subs
