#!/usr/bin/python3
"""Module for task 0"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    data = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False
            )
    if data.status_code >= 300:
        return 0

    return data.json().get("data").get("subscribers")
