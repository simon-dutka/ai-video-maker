import sys
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .subreddit.subreddit import subreddit
from .voice.change_voice import voice

def settings():
    choices = ['Subreddit', 'Voice', 'Exit']

    isExit = False
    
    while isExit == False:
        choiceIndex = get_inquirer_choice("Settings", choices)

        match choiceIndex:
            case 0:
                subreddit()
            case 1:
                voice()
            case 2:
                isExit = True