import os
import re
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

dir_path = "./stories"

files = []


def get_status_to_set():
    choices = [
        "Check story",
        "Ready to make audio",
        "Check audio",
        "Ready to make video",
        "Check video",
        "Ready to upload",
        "Exit",
    ]

    is_exit = False

    while is_exit is False:
        choiceIndex = get_inquirer_choice("Set type of status to set", choices)

        if choices[choiceIndex] == "Exit":
            is_exit = True
        else:
            change_ready_status(change_ready_status(choices[choiceIndex]))


def change_ready_status(status_to_set):
    isExit = False

    while isExit is False:
        folders_in_dir = [
            folder
            for folder in os.listdir(dir_path)
            if os.path.isdir(os.path.join(dir_path, folder))
        ]

        for i in range(len(folders_in_dir)):
            files.append(folders_in_dir[i])

        files.append("Exit")

        choiceIndex = get_inquirer_choice("Set file to change status", files)

        if files[choiceIndex] == "Exit":
            isExit = True
        else:
            old_folder_name = folders_in_dir[choiceIndex]
            olds_status = re.split("story\d{4} - ", folders_in_dir[choiceIndex])
            new_folder_name = old_folder_name.replace(olds_status[1], status_to_set)

            os.rename(
                "stories/" + folders_in_dir[choiceIndex], "stories/" + new_folder_name
            )

        files.clear()
