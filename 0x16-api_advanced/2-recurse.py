#!/usr/bin/python3
'''
    module for querying Reddit API
'''
import requests as req


def recurse(subreddit, hot_list=[], page='placeholder'):
    '''
        recursively query all the hottest post in a given subreddit
    '''
    try:
        res = req.get('https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
                      .format(subreddit, page),
                      headers={"user-agent": 'ames'}).json()
        if page is None:
            return hot_list
        else:
            next_page = res['data']['after']
            for post in res['data']['children']:
                hot_list.append(post['data']['title'])
            final = recurse(subreddit, hot_list, next_page)
            return final
    except KeyError:
        return None
