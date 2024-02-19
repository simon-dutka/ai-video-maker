import json


def set_all_default():
    with open("settings/default_settings.json", "r") as default_settings_file:
        default_settings = json.load(default_settings_file)

    with open("settings/settings.json", "w") as settings_file:
        json.dump(default_settings, settings_file, indent=4)
