from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .directories.directories import directories
from .subreddit.subreddit import subreddit
from .voice.voice import voice
from .default.set_default_settings import set_default_settings


def settings():
    choices = ["Directories", "Subreddit", "Voice", "Set default settings", "Exit"]

    isExit = False

    while isExit is False:
        choiceIndex = get_inquirer_choice("Settings", choices)

        match choiceIndex:
            case 0:
                directories()
            case 1:
                subreddit()
            case 2:
                voice()
            case 3:
                set_default_settings()
            case 4:
                isExit = True
