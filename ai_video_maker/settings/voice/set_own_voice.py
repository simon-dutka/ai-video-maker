import inquirer, json

def set_own_voice():
    #! Add .dump instead
    # voice = {
    #     'voice-id': inquirer.text(message="Enter voice id"),
    #     'voice-name': inquirer.text(message="Enter voice name")
    # }
    #ToDo: add iteration by getting last saved (in json) num of id
    with open("settings/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["voice_id-1"] = inquirer.text(message="Enter voice id")

    with open("settings/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
