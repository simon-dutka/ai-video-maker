import os
import re
import numpy as np
from moviepy.editor import *
from ai_video_maker.choice import set_choice
from moviepy.audio.AudioClip import AudioArrayClip

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


def make_video_files(background_file, audio_file):
    audio_dir = f"stories/{audio_file}/{audio_file}.mp3"
    #! Update dir with variable
    background_dir = f"background_videos/never_used/{background_file}"

    audio = AudioFileClip(audio_dir)

    silent_audio = AudioArrayClip(
        np.zeros((5 * audio.fps, audio.nchannels)), fps=audio.fps
    )

    final_audio = concatenate_audioclips([silent_audio, audio])

    background = VideoFileClip(background_dir)

    background = background.subclip(0, audio.duration + 5)

    background.audio = CompositeAudioClip([final_audio])

    background.write_videofile(f"./stories/{audio_file}/{audio_file}.mp4")