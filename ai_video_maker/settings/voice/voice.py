from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

from .set_own_voice import set_own_voice


def voice():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Set own voice": set_own_voice,
        "List of voices to set": list_of_voices_to_set,
        "List of using voices": list_of_using_voices,
        "Exit": is_exit.change_exit_status,
    }

    isExit = False

    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice("Voice settings", list(choices.keys()))

        choices[list(choices)[choiceIndex]]()
