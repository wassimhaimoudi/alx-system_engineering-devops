#!/usr/bin/python3
"""This module contains the definition
of the `number_of_subscribers()` function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers for a given subreddit

    Args:
        subreddit(str): The name of the subreddit to query

    Returns:
        int: The number of subscribers for the given subreddit
        Return 0 if the subreddit is invalid or if there's an error.

    Note: This function does not follow redirects to ensure invalid
        subreddit are properly handled.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla Browser'}
    try:
        response = requests.get(
                url,
                headers=headers,
                allow_redirects=False
                )
        if response.status_code == 200:
            return response.json().get('data').get('subscribers')
        else:
            return 0
    except Exception:
        return 0
