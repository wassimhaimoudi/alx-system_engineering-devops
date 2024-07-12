#!/usr/bin/python3
"""
This module contains the top_ten function definition
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the top 10 hot posts
    in a given subreddit
    """
    # Reddit API endpoint for hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Custom User-Agent to avoid Too Many Requests error
    h = {
        'User-Agent': 'linux:0x16.api_advanced:v1.0.0 (by /u/wassimhaimoudi)'
            }
    params = {
            'limit': 10
            }

    # Make the request
    response = requests.get(
            url,
            headers=h,
            params=params,
            allow_redirects=False
            )

    # Check if the subreddit is valid
    if response.status_code == 404:
        print(None)
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
