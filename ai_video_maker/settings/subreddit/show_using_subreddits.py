import json


# ToDo: Show all avaiable subreddits
def show_using_subreddits():
    with open("settings/settings.json", "r") as settings:
        settings_data = json.load(settings)

    using_subreddit = settings_data["subredditSettings"]["subreddit"]

    print(using_subreddit)
