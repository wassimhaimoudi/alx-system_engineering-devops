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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests error
    h = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/wassimhaimoudi)'
        }

    # Make the request
    response = requests.get(
            url,
            headers=h,
            allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
