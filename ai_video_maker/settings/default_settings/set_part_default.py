import json
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice


def show_parts():
    is_exit = False

    with open("settings/settings.json", "r") as settings_file:
        data = json.load(settings_file)

    choices = list(data.keys())

    choices.append("Exit")

    while is_exit == False:
        choiceIndex = get_inquirer_choice("Select part to set as default", choices)

        if choices[choiceIndex] == "Exit":
            is_exit = True
        else:
            set_part_default(choices[choiceIndex])


def set_part_default(part):
    with open("settings/default_settings.json", "r") as default_settings_file:
        default_data = json.load(default_settings_file)
        default_part_settings = default_data[part]

    with open("settings/settings.json", "r") as settings_file:
        settings_data = json.load(settings_file)
        settings_data[part] = default_part_settings

    with open("settings/settings.json", "w") as settings_file:
        default_data[part] = default_part_settings
        json.dump(settings_data, settings_file, indent=4)
