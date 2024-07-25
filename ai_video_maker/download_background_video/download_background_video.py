import os
from yt_dlp import YoutubeDL


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

    except:
        print("Error")
