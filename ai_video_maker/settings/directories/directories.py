from .num_of_directories import num_of_directories
from ai_video_maker.choice import set_choice


def directories():
    choices = {
        "Change number of creating directories": num_of_directories,
        "Exit": None,
    }

    return set_choice(
        "Settings",
        choices,
    )
