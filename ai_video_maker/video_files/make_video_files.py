import os
import re
import numpy as np
from moviepy.editor import *
from ai_video_maker.choice import set_choice
from moviepy.audio.AudioClip import AudioArrayClip

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def choose_video_length():
    while True:
        try:
            video_length = int(input("Choose video length in minutes: "))
            print(f"Video length: {video_length} minutes")
            break
        except ValueError:
            print("Invalid value. Enter a numeric value")


def set_background_to_make_video(audio_file):
    background_choices = {}

    for directory in os.listdir(f"./background_videos"):
        if directory != ".mp4":
            continue
        else:
            background_choices[directory] = (
                lambda dir=directory, audio_file=audio_file: make_video_files(
                    dir, audio_file
                )
            )

    if len(background_choices) > 0:
        return set_choice(
            "Select a video to set as a background",
            background_choices,
        )
    else:
        print("No available backgrounds")


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