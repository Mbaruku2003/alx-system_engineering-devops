#!/usr/bin/python3
"""uses reddit to print the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers."""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python:subscribers-check:v1.0 (by /u/yourusername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0
