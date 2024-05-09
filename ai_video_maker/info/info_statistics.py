import os
import json
from .create_info import create_info

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def statuses_stats():
    statistics_file = "./statistics.md"

    # Create statistics.md if not exists
    if not os.path.exists(statistics_file):
        with open(statistics_file, "w") as f:
            pass

    # ToDo: Add more statuses
    #! ToDo: Should get data from statistics.md
    statuses = {"empty": 0}

    # Function to check if "info.json" exists in a folder
    def check_info_json(folder):
        info_json_path = os.path.join(folder, "info.json")
        return os.path.exists(info_json_path)

    # Go through the subfolders
    for subfolder in os.listdir(dir_path):
        folder_path = os.path.join(dir_path, subfolder)
        if os.path.isdir(folder_path):
            # Create info.json file if not exists
            if check_info_json(folder_path) == False:
                file_path = os.path.join(f"./stories/{subfolder}/info.json")
                create_info(file_path, subfolder)

            info_file = os.path.join(dir_path, subfolder, "info.json")

            with open(info_file, "r") as f:
                data = json.load(f)
                status = data.get("status")

                if status in statuses:
                    statuses[status] += 1

    print("Statistics")
    for key in statuses:
        print(f"{key}: {statuses[key]}")
