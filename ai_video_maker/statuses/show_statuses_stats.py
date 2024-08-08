import os
import json


def show_statuses_stats():
    stats = {
        "Empty": 0,
        "Ready to make an audio": 0,
    }

    for directory in os.listdir("./stories"):
        if os.path.isdir(f"stories/{directory}"):
            with open(f"stories/{directory}/info.json", "r", encoding="utf-8") as file:
                file_status = json.load(file)["status"]
                if file_status in stats:
                    stats[file_status] += 1

    for key, value in stats.items():
        print(f"{key}: {value}")
