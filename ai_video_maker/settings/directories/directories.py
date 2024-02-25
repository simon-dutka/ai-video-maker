from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .num_of_directories import num_of_directories


def directories():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Change number of creating directories": num_of_directories,
        "Exit": is_exit.change_exit_status,
    }

    is_exit = False

    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice("Settings", list(choices.keys()))

        choices[list(choices)[choiceIndex]]()
