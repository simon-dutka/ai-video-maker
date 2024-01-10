import os
import re
import json


def make_dir():
    dir_path = "stories"

    folders_in_dir = [
        folder
        for folder in os.listdir(dir_path)
        if os.path.isdir(os.path.join(dir_path, folder))
    ]

    if len(folders_in_dir) == 0:
        folders_in_dir_last = 0
    else:
        folders_in_dir_last = folders_in_dir[len(folders_in_dir) - 1]
        folders_in_dir_last = int(
            re.sub("[a-z]|[A-Z]", "", folders_in_dir_last).replace(" - ", "")
        )

    with open("settings/settings.json", "r") as f:
        num_of_directories = json.load(f)["num_of_directories"]

        end_of_range = folders_in_dir_last + num_of_directories

        for i in range(folders_in_dir_last, end_of_range):
            folders_in_dir_last = folders_in_dir_last + 1

            folder_name = f"story{folders_in_dir_last:04d} - Empty"

            path = os.path.join(dir_path, folder_name)
            os.makedirs(path)
