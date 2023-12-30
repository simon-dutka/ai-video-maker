import sys
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .subreddit.set_subreddit import set_subreddit
from .voice.change_voice import change_voice

def settings():
    choices = ['Set subreddit', 'Change voice', 'Exit']

    isExit = False
    
    while isExit == False:
        choiceIndex = get_inquirer_choice("Settings", choices)

        match choiceIndex:
            case 0:
                set_subreddit()
            case 1:
                change_voice()
            case 2:
                isExit = True