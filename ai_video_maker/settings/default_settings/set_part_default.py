import json
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice


def show_parts():
    is_exit = False

    settings = "settings/settings.json"

    with open(settings, "r") as settings_file:
        data = json.load(settings_file)

    choices = list(data.keys())

    choices.append("Exit")

    while is_exit == False:
        choiceIndex = get_inquirer_choice("Select part to set as default", choices)

        if choices[choiceIndex] == "Exit":
            is_exit = True
        else:
            set_all_default(choices[choiceIndex])

