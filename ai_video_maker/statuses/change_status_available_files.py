import json


def change_status_available_files(file_to_change_status, file_to_add):
    info_file_path = f"stories/{file_to_change_status}/info.json"

    with open(info_file_path, "r") as json_file:
        json_info_data = json.load(json_file)

        json_info_data["available-files"].append(file_to_add)

    with open(info_file_path, "w") as json_file:
        json.dump(json_info_data, json_file, indent=4)
