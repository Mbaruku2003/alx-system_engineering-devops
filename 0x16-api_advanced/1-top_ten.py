#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed."""
import requests


def top_ten(subreddit):
    """reddit api endpost"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
