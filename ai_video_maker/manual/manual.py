from rich.console import Console
from rich.markdown import Markdown
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice


choices = {
    "How to change voice": "ai_video_maker/manual/manuals/how_to_change_voice.md",
}


def display_manual(file_path):
    with open(file_path, "r") as file:
        Console().print(Markdown(file.read()))


class exit_status:
    def __init__(self, is_exit):
        self.is_exit = is_exit

    def change_exit_status(self):
        self.is_exit = True


is_exit = exit_status(False)


def manual():
    while is_exit.is_exit == False:
        choiceIndex = get_inquirer_choice("Manual", list(choices.keys()))

        display_manual(choices[list(choices)[choiceIndex]])
        # ToDo: Add exit function
