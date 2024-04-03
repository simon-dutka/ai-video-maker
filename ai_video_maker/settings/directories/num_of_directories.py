import inquirer
import json


def num_of_directories():
    with open("settings/settings.json", "r") as jsonFile:
        json_data = json.load(jsonFile)

    json_data["directoriesSettings"]["num_of_directories"] = int(
        inquirer.text(message="Enter number of directories to create")
    )

    with open("settings/settings.json", "w") as jsonFile:
        json.dump(json_data, jsonFile, indent=4)
