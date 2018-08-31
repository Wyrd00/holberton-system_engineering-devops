#!/usr/bin/python3
'''
    module for querying Reddit API
'''
import requests
from sys import argv

def number_of_subscribers(subreddit):
    '''
        get total subscribers of a subreddit
    '''
    try:
        res = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit), headers={"user-agent": 'ames'})
                           .json()
        #valid = requests.get('https://reddit.subreddits.search_by_name({}, exact=True)'.format(subreddit))
        return res['data']['subscribers']
    except:
        return 0
