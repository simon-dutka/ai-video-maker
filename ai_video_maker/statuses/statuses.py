from  ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from .change_ready_status import get_status_to_set
choices = ['Change statuses', 'Statuses stats', 'Exit']

def statuses():

    is_exit = False

    while is_exit == False:
        choiceIndex = get_inquirer_choice("Statuses", choices)

        match choiceIndex:
            case 0:
                get_status_to_set()
            case 1:
                pass
            case 2:
                is_exit == True