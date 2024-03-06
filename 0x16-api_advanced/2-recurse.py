#!/usr/bin/python3
import requests
"""
    queries the Reddit API and returns a list containing the titles
"""


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "DeFatso/App"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            posts = data.get('data', {}).get('children', [])
            if not posts:
                return hot_list
            else:
                for post in posts:
                    title = post.get('data', {}).get('title', '')
                    hot_list.append(title)

                after = data.get('data', {}).get('after', None)
                if after:
                    return recurse(subreddit, hot_list)
                else:
                    return hot_list
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
