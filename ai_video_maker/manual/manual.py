from rich.console import Console
from rich.markdown import Markdown
from ai_video_maker.choice.set_choice import set_choice

choices = {
    "How to change voice": lambda: display_manual(
        "ai_video_maker/manual/manuals/how_to_change_voice.md"
    ),
    "Exit": None,
}


def display_manual(file_path):
    with open(file_path, "r") as file:
        Console().print(Markdown(file.read()))


def manual():
    set_choice(choices, "Manual")
