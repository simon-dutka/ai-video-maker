from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from ..info.info_statistics import statuses_stats
from .set_directory_to_change_status import set_directory_to_change_status
from .show_statuses_stats import show_statuses_stats


def statuses():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Change statuses": set_directory_to_change_status,
        "Statuses stats": show_statuses_stats,
        "Exit": is_exit.change_exit_status,
    }

    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice("Statuses", list(choices.keys()))

        choices[list(choices)[choiceIndex]]()
