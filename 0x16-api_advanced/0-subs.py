#!/usr/bin/python3
"""
    queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "DeFatso/App"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
