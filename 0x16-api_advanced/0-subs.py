#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    ''' Finds the number of subscribers in a subreddit '''

    header = {'User-Agent': 'Chrome/66.0.3359.139 Mobile Safari/537.36'}
    url = "https://api.reddit.com/r/{subreddit}/about.json".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        sub = response.json()["data"]["subscribers"]
    else:
        sub = 0
    return sub
