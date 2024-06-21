import json


def list_of_subreddits():
    choices = ["List of most popular subreddits", "Exit"]
    is_exit = False

    while is_exit is False:
        choiceIndex = get_inquirer_choice("Set subreddit to use", choices)

        match choiceIndex:
            case 0:
                list_of_subreddits()
            case 1:
                is_exit = True

    subreddit = {"using-subreddit": "Test"}

    with open("settings/settings.json", "w") as settings:
        json.dump(subreddit, settings, indent=4)
