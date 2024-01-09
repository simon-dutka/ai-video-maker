from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .num_of_directories import num_of_directories


def directories():
    choices = ["Change number of creating directories", "Exit"]

    isExit = False

    while isExit is False:
        choiceIndex = get_inquirer_choice("Settings", choices)

        match choiceIndex:
            case 0:
                num_of_directories()
            case 1:
                isExit = True
