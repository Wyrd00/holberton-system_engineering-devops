#!/usr/bin/python3
'''
    module for querying Reddit API
'''
import requests as req


def number_of_subscribers(subreddit):
    '''
        get total subscribers of a subreddit
    '''
    try:
        res = req.get('https://www.reddit.com/r/{}/about.json'
                      .format(subreddit),
                      headers={"user-agent": 'ames'}).json()
        return res['data']['subscribers']
    except KeyError:
        return 0
