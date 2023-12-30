import json

def set_own_subreddit():
    subreddit = {
        'subreddit': 'Test'
    }
    with open('settings/settings.json', 'w') as settings:
        json.dump(subreddit, settings)

set_own_subreddit()