import json
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

def list_of_subreddits():
    choices = ['List of most popular subreddits', 'Exit']
    isExit = False

    while isExit == False:
        choiceIndex = get_inquirer_choice("Set subreddit to use", choices)

        match choiceIndex:
            case 0:
                list_of_subreddits()
            case 1:
                isExit = True

    subreddit = {
        'subreddit': 'Test'
    }

    with open('data/settings.json', 'w') as settings:
        json.dump(subreddit, settings)
