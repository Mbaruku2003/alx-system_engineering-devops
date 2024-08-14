#!/usr/bin/python3
"""uses Reddit API to get all posts."""
import requests


def recurse(subreddit, hot_list=[]):
    """get all the hot posts."""

    if after is None:
        return []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'UserAgent': 'Request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    thejson = response.json()
    json_post = thejson.get("data").get("children")
    for post in json_post:
        the_list.append(post.get("data").get("title"))
    return the_list + recurse(subreddit, [], thejson.get("data").get("after"))
