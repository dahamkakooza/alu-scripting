#!/usr/bin/python3
"""DOCS"""
import requests

def top_ten(subreddit):
    """Print the top ten hot posts of a given subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        if 'children' in data:
            for post in data['children'][:10]:
                print(post['data']['title'])
            return "OK"  # Indicating successful completion
        else:
            print(None)
            return "None"  # In case data is empty or not formatted as expected
    else:
        print(None)
        return "None"  # Indicating failure due to a non-200 status code
