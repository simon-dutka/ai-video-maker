import os
import json
import numpy as np
import inquirer
from moviepy.editor import *
from ai_video_maker.choice import set_choice
from moviepy.audio.AudioClip import AudioArrayClip

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def choose_video_length():
    choices = [
        "Select story automatically based on length in minutes",
        "Manually select stories for the video",
    ]

    select_method = inquirer.prompt(
        [
            inquirer.List(
                "Select method",
                message="Choose a method to select the length of the video",
                choices=choices,
            ),
        ]
    )

    selected_index = choices.index(select_method["Select method"])

    if selected_index == 0:
        auto_select_stories()
    else:
        manual_select_stories()


def auto_select_stories():
    audio_len = {}

    while True:
        try:
            video_length = int(input("Choose video length in minutes: "))
            break
        except ValueError:
            print("Invalid value. Enter a numeric value")

    directory = "./stories"

    for story_dir in os.listdir(directory):
        story_dir_path = os.path.join(directory, story_dir)
        if os.path.isdir(story_dir_path):
            file_path = f"./stories/{story_dir}/info.json"

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if "audio file" in data.get("available-files", []):
                    audio_len[story_dir] = data["audio-length"]


def manual_select_stories():
    pass


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