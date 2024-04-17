import os
from ai_video_maker.choice import set_choice
from . import change_status


def set_directory_to_change_status():
    dire_path = "./stories/"
    directories = [
        f for f in os.listdir(dire_path) if os.path.isdir(os.path.join(dire_path, f))
    ]

    directories_names = []
    chocies = {}

    if directories:
        for directory in directories:
            directories_names.append(directory)
    else:
        print("No avaiable directories")

    new_choices = {}

    def test():
        pass

    for key in directories_names:
        new_choices[key] = lambda: change_status(key)

    chocies.update(new_choices)

    return set_choice(
        "Set directory to change status",
        chocies,
    )
