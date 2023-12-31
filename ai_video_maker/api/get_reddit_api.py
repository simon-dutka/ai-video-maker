import praw
import json

with open(".secret/keys.json", "r") as f:
    keys = json.load(f)

reddit = praw.Reddit(
    client_id=keys["REDDIT_CLIENT_ID"],
    client_secret=keys["REDDIT_CLIENT_SECRET"],
    user_agent="my user agent",
)


def get_reddit():
    return reddit


def get_subreddit():
    return reddit.subreddit("AmItheAsshole")
