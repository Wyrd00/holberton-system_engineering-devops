#!/usr/bin/python3
'''
    module for querying Reddit API
'''
import requests as req


def top_ten(subreddit):
    '''
        prints titles of the first 10 hots listings
    '''
    try:
        res = req.get('https://www.reddit.com/r/{}/hot.json?limit=8'
                      .format(subreddit), allow_redirections=False,
                      headers={"user-agent": 'ames'}).json()
        for post in res['data']['children']:
            print(post['data']['title'])
    except BaseException:
        print('None')
