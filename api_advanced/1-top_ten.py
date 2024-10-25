#!/usr/bin/python3
"""DOCS"""
import requests

def top_ten(subreddit):
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    
    # Sending GET request without following redirects
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    # Check if the response status is 200 (OK)
    if response.status_code == 200:
        try:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children:
                print(None)
                return
            # Print the titles of the first 10 hot posts
            for post in children[:10]:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
