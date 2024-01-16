from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from .change_ready_status import get_status_to_set
from .statuses_stats import statuses_stats

choices = ["Change statuses", "Statuses stats", "Exit"]


def statuses():
    is_exit = False

    while is_exit is False:
        choiceIndex = get_inquirer_choice("Statuses", choices)

        match choiceIndex:
            case 0:
                get_status_to_set()
            case 1:
                statuses_stats()
            case 2:
                is_exit = True
