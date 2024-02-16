from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from .change_ready_status import get_status_to_set
from .statuses_stats import statuses_stats


def statuses():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Change statuses": get_status_to_set,
        "Statuses stats": statuses_stats,
        "Exit": is_exit.change_exit_status,
    }

    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice("Statuses", list(choices.keys()))

        choices[list(choices)[choiceIndex]]()
