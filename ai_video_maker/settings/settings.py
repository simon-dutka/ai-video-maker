import sys
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .subreddit.set_subreddit import set_subreddit

def settings():
    choices = ['Set subreddit', 'Exit']

    isExit = False
    
    while isExit == False:
        choiceIndex = get_inquirer_choice("Settings", choices)

        match choiceIndex:
            case 0:
                set_subreddit()
            case 1:
                isExit = True