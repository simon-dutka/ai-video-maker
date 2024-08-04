import os
import json
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip


def update_backgrounds_info(video_name):
    video_path = f"./background_videos/{video_name}"
    video = VideoFileClip(video_path)

    background_info_file_path = "./background_videos/backgrounds_info.json"

    with open(background_info_file_path, "r") as json_file:
        json_info_data = json.load(json_file)

    new_background_info = {
        video_name: "never used",
        "background-length": round(video.duration / 60, 1),
    }

    json_info_data["available backgrounds"].append(new_background_info)

    with open(background_info_file_path, "w") as json_file:
        json.dump(json_info_data, json_file, indent=4)


def download_background_video(url):
    video_name = input("Enter the video name: ")
    download_path = "./background_videos"

    try:
        ydl_opts = {
            "format": "mp4",
            "outtmpl": "%(title)s.%(ext)s",
            "outtmpl": os.path.join(download_path, f"{video_name}.%(ext)s"),
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

            update_backgrounds_info(f"{video_name}.mp4")

    except:
        print("Error")
