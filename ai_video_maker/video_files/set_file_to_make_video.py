import os
from .make_video_files import make_video_files
from ai_video_maker.choice import set_choice


def set_file_to_make_video():
    choices = {}

    for directory in os.listdir("./stories"):
        if "- Ready to make video" in directory:
            choices[directory] = lambda: make_video_files(directory)

    set_choice(choices, "Set file to make video")
