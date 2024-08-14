#!/usr/bin/python3
"""Query subscribers of a given reddit subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a subreddit."""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    response = requests.get(url, headers=headers, allow_redirect=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results.get("subscribers")
