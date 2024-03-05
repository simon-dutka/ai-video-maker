from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice


def set_choice(choices, title):
    class ExitStatus:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = ExitStatus(False)

    while is_exit.is_exit == False:
        choice_index = get_inquirer_choice(title, list(choices.keys()))

        if list(choices)[choice_index] == "Exit":
            break
        choices[list(choices)[choice_index]]()
