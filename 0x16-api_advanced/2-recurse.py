#!/usr/bin/python3
import requests
"""detailed info."""


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5-0'}
    parameters = {'limit': 100}
    if after:
        parameters['after'] = after
    try:
        response = requests.get(
                   url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after', None)
            for post in posts:
                hottest_list.append(post['data']['title'])
            if after:
                return recurse(subreddit, hottest_list, after)
            else:
                return hottest_list
        else:
            return None

    except requests.RequestException:
        return None
