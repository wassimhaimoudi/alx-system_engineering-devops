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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyUser/1.0'}

    # Make the request
    response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
            )

    # Check if the subreddit is valid
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')

        # Print the titles of the first 10 hot posts
        for post in posts[:10]:
            print(f"{post.get('data').get('title')}")
    else:
        print(None)
