import os
import re
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from .make_voice_file import make_voice_file

dir_path = "stories"

folders_in_dir = [
    folder
    for folder in os.listdir(dir_path)
    if os.path.isdir(os.path.join(dir_path, folder))
]
choices = []

for directory in os.listdir("./stories"):
    if "- Ready to make audio" in directory:
        choices.append(directory)

choices.append("Exit")

index_of_exit = len(choices) - 1


def set_file_to_make_voice():
    for directory in os.listdir("./stories"):
        if "- Ready to make voice" in directory:
            print(directory)

    is_exit = False

    while is_exit is False:
        choiceIndex = get_inquirer_choice("Set file to make voice", choices)

        if choiceIndex == index_of_exit:
            is_exit = True
        else:
            make_voice_file(re.sub(r"- Ready to make voice", "", choices[choiceIndex]))
