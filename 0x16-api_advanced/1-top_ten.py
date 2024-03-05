#!/usr/bin/python3
"Function to query Reddit API and prints titles of first 10 hot posts"

import requests


def top_ten(subreddit):
    """Module to return the titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        print(None)
