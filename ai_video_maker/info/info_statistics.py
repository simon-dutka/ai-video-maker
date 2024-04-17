import os
import json

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def statuses_stats():
    # Add more statuses
    statuses = {"empty": 0}

    info_file = os.path.join(dir_path, "info.json")

    # Check if info.json exists in directory
    if os.path.exists(info_file):
        with open(info_file, "r") as f:
            data = json.load(f)
            status = data.get("status")
            if status in statuses:
                statuses[status] += 1
    else:
        # ToDo: Create info.json file if not exists
        pass

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            for file in os.listdir(item_path):
                with open(os.path.join(item_path, file), "r") as f:
                    story_data = json.load(f)
                    status = story_data.get("status", "empty")
                    if status in statuses:
                        statuses[status] += 1

    print("Statistics")
    for key in statuses:
        print(f"{key}: {statuses[key]}")
