#!/usr/bin/python3
"""Query subscribers of a given reddit subreddit"""
import requests
import json


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a subreddit."""

    url = f"https:www.reddit.com/r/{subreddit}/about.json"

    header = {'User-Agent': 'Python:subscribers-check:v1.0 (b /u/yourusername)'
            }
    try:
        response = rquests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
