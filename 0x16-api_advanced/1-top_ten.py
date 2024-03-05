#!/usr/bin/python3
"""
    queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "DeFatso/App"}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get('data', {}).get('title', '')
            print(title)
    else:
        print("None")
