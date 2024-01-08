import os
import re

dir_path = "./stories"


def statuses_stats():
    existing_statuses = []
    # All statuses
    statuses = [
        "Empty",
        "Check story",
        "Ready to make audio",
        "Check audio",
        "Ready to make video",
        "Check video",
        "Ready to upload",
    ]

    folders_in_dir = [
        folder
        for folder in os.listdir(dir_path)
        if os.path.isdir(os.path.join(dir_path, folder))
    ]

    for i in range(len(folders_in_dir)):
        for j in range(len(statuses)):
            checking_folder = re.split("story\d{4} - ", folders_in_dir[i])

            if checking_folder[1] == statuses[j]:
                existing_statuses.append(statuses[j])

    # Counting and print stats
    for i in range(len(statuses)):
        print(statuses[i] + ": " + str(existing_statuses.count(statuses[i])))
