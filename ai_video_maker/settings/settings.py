from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .directories.directories import directories
from .subreddit.subreddit import subreddit
from .voice.voice import voice
from .default.set_default_settings import set_default_settings


def settings():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Directories": directories,
        "Subreddit": subreddit,
        "Voice": voice,
        "Set default settings": set_default_settings,
        "Exit": is_exit.change_exit_status,
    }

    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice("Settings", list(choices.keys()))

        choices[list(choices)[choiceIndex]]()
