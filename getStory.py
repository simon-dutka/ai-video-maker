import praw
import json
with open ('.secret/keys.json', 'r') as f:
    keys = json.load(f)

reddit = praw.Reddit(
    client_id=keys['CLIENT_ID'],
    client_secret=keys['CLIENT_SECRET'],
    user_agent="my user agent",
)

subreddit = reddit.subreddit("AmItheAsshole")

for post in subreddit.top(time_filter="day", limit=1):
    print(post.title)
    print(post.selftext)