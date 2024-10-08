import os
import sys
import json
import itertools
import inquirer
import numpy as np
from moviepy.editor import *
from ai_video_maker.choice import set_choice
from moviepy.audio.AudioClip import AudioArrayClip

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def set_background(audio_length, audio_file):
    background_choices = {}

    with open("./background_videos/backgrounds_info.json", "r") as file:
        data = json.load(file)

        names = [
            item.get("name")
            for item in data["available backgrounds"]
            if float(item.get("background-length", 0)) > float(audio_length)
        ]

        for background_path in names:
            print(background_path)
            background_choices[background_path] = (
                lambda background_path=background_path,
                audio_file=audio_file: create_video_files(background_path, audio_file)
            )

    if len(background_choices) > 0:
        return set_choice(
            "Select a video to set as a background",
            background_choices,
        )
    else:
        print("No available backgrounds")


def choose_video_length():
    while True:
        video_name = input("Enter the video name: ")

        video_path = f"videos/{video_name}"

        if not os.path.exists(video_path):
            os.makedirs(video_path)
            break
        else:
            print(f"A video with the name {video_name} already exists.")

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
        auto_select_stories(video_name)
    else:
        manual_select_stories(video_name)


def combine_audio(audio_len_list, video_name, avg_sum):
    audio_clips = [AudioFileClip(audio_file) for audio_file in audio_len_list]

    combined_audio = concatenate_audioclips(audio_clips)

    combined_audio.write_audiofile(f"./videos/{video_name}/{video_name}.mp3")

    set_background(avg_sum, video_name)


def auto_select_stories(video_name):
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
                    audio_len[f"./stories/{story_dir}/{story_dir}.mp3"] = data[
                        "audio-length"
                    ]

    def find_combinations(d, video_length):
        keys = list(d.keys())
        best_combination = None
        best_difference = float("inf")
        for r in range(1, len(keys) + 1):
            for combination in itertools.combinations(keys, r):
                current_sum = sum(d[key] for key in combination)
                current_difference = abs(video_length - current_sum)
                if current_difference < best_difference:
                    best_combination = combination
                    best_difference = current_difference
                    if best_difference == 0:
                        return best_combination, current_sum

        return best_combination, sum(d[key] for key in best_combination)

    best_combination, avg_sum = find_combinations(audio_len, video_length)

    combine_audio(best_combination, video_name, avg_sum)


def manual_select_stories(video_name):
    root_directory = "./stories"

    available_stories = []

    for root, dirs, files in os.walk(root_directory):
        for dir_name in dirs:
            info_file_path = f"./stories/{dir_name}/info.json"

            with open(info_file_path, "r") as file:
                data = json.load(file)

                if data.get("status") == "Ready to create a video":
                    available_stories.append(dir_name)

    questions = [
        inquirer.Checkbox(
            "select_stories",
            message="Select audio files (use space then enter to confirm)",
            choices=available_stories,
        ),
    ]

    selected_stories = inquirer.prompt(questions)


def create_video_files(background_file, audio_file):
    audio_dir = f"./videos/{audio_file}/{audio_file}.mp3"
    #! Update dir with variable
    background_dir = f"./background_videos/{background_file}.mp4"

    audio = AudioFileClip(audio_dir)

    silent_audio = AudioArrayClip(
        np.zeros((5 * audio.fps, audio.nchannels)), fps=audio.fps
    )

    final_audio = concatenate_audioclips([silent_audio, audio])

    background = VideoFileClip(background_dir)

    background = background.subclip(0, audio.duration + 5)

    background.audio = CompositeAudioClip([final_audio])

    background.write_videofile(f"./videos/{audio_file}/{audio_file}.mp4")
    sys.exit()
