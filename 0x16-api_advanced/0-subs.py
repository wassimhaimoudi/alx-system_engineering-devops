#!/usr/bin/python3
"""This module contains the definition
of the `number_of_subscribers()` function
"""
from requests import get


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

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
