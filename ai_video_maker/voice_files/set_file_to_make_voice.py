import os
from .make_voice_file import make_voice_file
from ai_video_maker.choice.set_choice import set_choice


def set_file_to_make_voice():
    choices = {}

    for directory in os.listdir("./stories"):
        if "- Ready to make audio" in directory:
            choices[directory] = lambda: make_voice_file(directory)

    return set_choice("Set file to make voice", choices)
