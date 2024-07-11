#!/usr/bin/python3
"""
This module contains the number_of_subsribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subs
    in a subreddit
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyUser/1.0'}

    # Make the request
    response = requests.get(
            url,
            headers=headers,
            allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
