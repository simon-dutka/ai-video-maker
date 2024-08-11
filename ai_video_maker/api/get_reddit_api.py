import praw
import json


def get_reddit():
    with open(".secret/keys.json", "r") as file:
        keys = json.load(file)

    reddit = praw.Reddit(
        client_id=keys["REDDIT_CLIENT_ID"],
        client_secret=keys["REDDIT_CLIENT_SECRET"],
        user_agent="my user agent",
    )

    return reddit


def get_subreddit():
    reddit = get_reddit()

    with open("settings/settings.json", "r") as file:
        data = json.load(file)
        using_subreddit = data["subredditSettings"]["using-subreddit"]

        return reddit.subreddit(using_subreddit)
