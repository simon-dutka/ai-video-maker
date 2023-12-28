from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from ..story_files import list_of_subreddits

def set_subreddit():
    choices = ['List of most popular subreddits', 'Exit']
    isExit = False

    while isExit == False:
        choiceIndex = get_inquirer_choice("Set subreddit to use", choices)

        match choiceIndex:
            case 0:
                list_of_subreddits()
            case 1:
                isExit = True
