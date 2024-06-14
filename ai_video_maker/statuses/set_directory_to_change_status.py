import os
from ai_video_maker.choice import set_choice
from .change_status import change_status


def set_directory_to_change_status():
    dire_path = "./stories/"

    directories = [
        f for f in os.listdir(dire_path) if os.path.isdir(os.path.join(dire_path, f))
    ]

    if not directories:
        print("No available directories")

    choices = {}

    for directory in directories:
        choices[directory] = lambda dir=directory: change_status(dir)

    return set_choice("Set directory to change status", choices)
    # ToDo: Use returns answer as an argument and do change_statuses(answer)
