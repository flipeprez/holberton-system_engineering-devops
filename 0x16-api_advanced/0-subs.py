#!/usr/bin/python3
''' a nice comment'''
import request 
import json


def number_of_suscribers(subreddit)
    ''' a nice comments'''
    header = {'user-agent':'mozilla/100.0.2'}
    url = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    response = request.get(url, headers=header)
    if response.status_code = 200:
        sub = response.json()['data']['suscribers']
    else:
        sub = 0
    return sub

