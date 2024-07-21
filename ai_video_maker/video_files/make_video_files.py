import os, re
from moviepy.editor import *
from ai_video_maker.choice import set_choice


dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Adding just name to a list
# def set_background_to_make_video():
#     files = {}  # Initialize an Empty list to store all file names
#     for directory in os.listdir("./background_videos"):
#         directory_path = os.path.join("./background_videos", directory)
#         files.extend(file for file in os.listdir(directory_path) if file != ".gitkeep")

#     print(files)


def set_background_to_make_video():
    files = {}  # Initialize an Empty dictionary to store all file names
    for directory in os.listdir("./background_videos"):
        directory_path = os.path.join("./background_videos", directory)
        files.update(
            {file: "test" for file in os.listdir(directory_path) if file != ".gitkeep"}
        )

    print(files)


# set_background_to_make_video()


def make_video_files(audio_file):
    set_background_to_make_video()

    audio = AudioFileClip(audio_file)
    background = VideoFileClip(background_file)
    # video = editor.set_audio(audio.audio)

    background.audio = CompositeAudioClip([audio])

    background.write_videofile("./new_filename.mp4")


# make_video_files()
# make_video_files(
#     "./stories/story0001 - Ready to make video/story0001.mp3",
#     "./background_videos/never_used/test02.mp4",
# )
