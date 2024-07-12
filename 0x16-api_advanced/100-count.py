#!/usr/bin/python3
"""
This Module contains the count_words function def
"""
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Queries the titles of all hot articles
    and prints the sorted count of giver keywords
    """
    if word_count is None:
        word_count = Counter()

    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/1.0'}

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
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    # Process titles
    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        words = re.findall(r'\b[\w]+\b', title)
        for word in words:
            if word.lower() in [w.lower() for w in word_list]:
                word_count[word.lower()] += 1

    # Check for more pages
    after = data.get('data', {}).get('after')
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        # Print results
        s = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in s:
            if count > 0:
                print(f"{word.lower()}: {count}")
