import praw
import json
with open ('.secret/keys.json', 'r') as f:
    keys = json.load(f)

def get_reddit_api():
    reddit = praw.Reddit(
        client_id=keys['CLIENT_ID'],
        client_secret=keys['CLIENT_SECRET'],
        user_agent="my user agent",
    )

    return reddit.subreddit("AmItheAsshole")