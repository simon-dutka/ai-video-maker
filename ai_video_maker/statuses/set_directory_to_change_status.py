import os
import json
from ai_video_maker.choice import set_choice
from .change_status import change_status


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
                    lambda dir=directory: change_status(dir)
                )

    return set_choice("Set directory to change status", choices)
