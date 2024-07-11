#!/usr/bin/python3
"""This Module contains the definition of the function recurse
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and returns a list
    containing the titles of all hot articles
    for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyUser/1.0'}

    # Parameters for pagination
    params = {'limit': 100}
    if after:
        params['after'] = after

    # Make the request
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    # Check if the subreddit is valid
    if response.status_code != 200:
        return None if not hot_list else hot_list

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    # Add titles to the hot_list
    for post in posts:
        title = post.get('data', {}).get('title')
        if title:
            hot_list.append(title)

    # Check for more pages
    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
