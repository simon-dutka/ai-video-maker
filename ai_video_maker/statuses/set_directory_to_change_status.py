import os
import json
from .new_status_to_set import new_status_to_set
from ai_video_maker.choice import set_choice


def set_directory_to_change_status():
    dir_path = "./stories/"

    choices = {}

    directories = [
        f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))
    ]

    if not directories:
        print("No available directories")
    else:
        for directory in directories:
            with open(f"./stories/{directory}/info.json", "r") as file:
                data = json.load(file)
                status = data.get("status")

                choices[f"{directory} - {status}"] = (
                    lambda dir=directory: new_status_to_set(dir)
                )

    return set_choice("Set directory to change status", choices)
