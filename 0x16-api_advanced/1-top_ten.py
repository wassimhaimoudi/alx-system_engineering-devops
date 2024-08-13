#!/usr/bin/python3
"""
This module containd the definition of the function
`top_ten()`
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the top 10 hot
    posts of a given subreddit
    
    Args:
        subreddit(int): The name of the subreddit

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'My Mozilla Browser'}
    params = {'limit': 10}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
                )
        if response.status_code == 200:
            posts = response.json().get('data').get('children')

            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)
