#!/usr/bin/python3
"""Module to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Gets the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    """Checks for validity and existstance of the subreddit"""
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
