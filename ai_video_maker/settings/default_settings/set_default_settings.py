from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .set_all_default import set_all_default
from .set_part_default import show_parts


def set_default_settings():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Set all of settings as default": set_all_default,
        "Set part of settings as default": show_parts,
        "Exit": is_exit.change_exit_status,
    }

    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice(
            "Set settings as default", list(choices.keys())
        )

        choices[list(choices)[choiceIndex]]()
