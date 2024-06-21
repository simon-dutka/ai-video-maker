import json


def update_status(directory, new_status):
    with open(f"{directory}/info.json", "r") as info_file:
        json_data = json.load(info_file)

        json_data["status"] = new_status

    # Not finished
    with open(f"{directory}/info.json", "w") as settings_file:
        json.dump(default_settings, settings_file, indent=4)
