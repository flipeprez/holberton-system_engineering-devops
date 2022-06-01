from importlib import import_module
import requests


def number_of_subscribers(subreddit):
    ''' Finds the number of subscribers in a subreddit '''

    header = {'User-Agent':  'mozilla/100.0.2'}
    url = "https://api.reddit.com/r/{subreddit}/about.json".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        subs = response.json()["data"]["subscribers"]
    else:
        subs = 0
    return subs
