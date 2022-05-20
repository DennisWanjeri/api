#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first !0 hosts
"""
import requests


def top_ten(subreddit):
    """
    prints titles of the 10 hottest posts on a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Linux:advanced_api"
        }
    params = {
        "limit": 10
        }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
