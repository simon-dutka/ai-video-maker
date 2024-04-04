import json


def create_info(file_path, directory):
    data = {"directory_name": directory, "status": "empty"}

    with open(file_path, "w") as info_file:
        json.dump(data, info_file, indent=4)
