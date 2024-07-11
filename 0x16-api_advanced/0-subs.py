#!/usr/bin/python3
"""Module for task 0"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    try:
        data = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={"User-Agent": "Mozilla/5.0 \
                    (X11; Linux x86_64; rv:127.0) \
                    Gecko/20100101 Firefox/127.0"}
            )
        return data.json().get("data").get("subscribers")
    except Exception:
        return 0
