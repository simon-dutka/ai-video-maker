from .directories.directories import directories
from .subreddit.subreddit import subreddit
from .voice.voice import voice
from .default_settings.set_default_settings import set_default_settings
from ai_video_maker.choice import set_choice


def settings():
    choices = {
        "Directories": directories,
        "Subreddit": subreddit,
        "Voice": voice,
        "Set default settings": set_default_settings,
        "Exit": None,
    }

    return set_choice(
        "Settings",
        choices,
    )
