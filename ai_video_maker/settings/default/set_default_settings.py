import json


def set_default_settings():
    default_settings = ""

    with open("settings/default_settings.json", "r") as default:
        default_settings = json.load(default)

    with open("settings/settings.json", "w") as settings:
        json.dump(default_settings, settings)
