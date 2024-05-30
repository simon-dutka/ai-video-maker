import json
import os


def create_info(
    directory_path,
    directory_name,
):
    data = {"directory_name": directory_name, "status": "empty"}

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(directory_path), exist_ok=True)

    with open(directory_path, "w") as info_file:
        json.dump(data, info_file, indent=4)
