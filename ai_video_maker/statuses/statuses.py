from  ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

choices = ['Change statuses', 'Statuses stats', 'Exit']

def statuses():

    is_exit = False

    while is_exit == False:
        choiceIndex = get_inquirer_choice("Statuses", choices)

       