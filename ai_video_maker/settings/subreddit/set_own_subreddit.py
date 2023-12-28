import inquirer, json

def set_own_subreddit():
    subreddit = {
        'subreddit': inquirer.text(message="Enter subreddit title")
    }

    with open('data/settings.json', 'w') as settings:
        json.dump(subreddit, settings)