import inquirer
import json


def set_own_subreddit():
    subreddit = {
        ["subredditSettings"]["using-subreddit"]: inquirer.text(
            message="Enter subreddit title"
        )
    }

    with open("settings/settings.json", "w") as settings:
        json.dump(subreddit, settings, indent=4)
