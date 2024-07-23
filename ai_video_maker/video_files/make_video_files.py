import os, re
from moviepy.editor import *
from ai_video_maker.choice import set_choice

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def set_directory_to_choose_background(audio_file):
    directory_choices = {}

    for directory in os.listdir("./background_videos"):
        directory_choices[directory] = (
            lambda dir=directory: set_background_to_make_video(dir, audio_file)
        )

    return set_choice(
        "Select the folder from which you want to choose a background",
        directory_choices,
    )


def set_background_to_make_video(dir, audio_file):
    background_choices = {}
    for directory in os.listdir(f"./background_videos/{dir}"):
        if directory == ".gitkeep":
            continue
        else:
            background_choices[directory] = (
                lambda dir=directory, audio_file=audio_file: make_video_files(
                    dir, audio_file
                )
            )

    return set_choice(
        "Select a video to set as a background",
        background_choices,
    )


# Execute after choose background video
def make_video_files(dir, audio_file):
    pass
