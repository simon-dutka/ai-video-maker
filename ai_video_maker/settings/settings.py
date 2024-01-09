from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .directories.directories import directories
from .subreddit.subreddit import subreddit
from .voice.voice import voice


def settings():
    choices = ["Directories", "Subreddit", "Voice", "Exit"]

    isExit = False

    while isExit is False:
        choiceIndex = get_inquirer_choice("Settings", choices)

        match choiceIndex:
            case 0:
                directories()
            case 0:
                subreddit()
            case 1:
                voice()
            case 2:
                isExit = True
