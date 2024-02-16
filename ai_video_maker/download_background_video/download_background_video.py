from pytube import YouTube


def download_background_video(url):
    yt = YouTube(url).yt.streams.get_highest_resolution()

    video_name = input("Enter the video name: ")

    try:
        (yt.download("../background_videos", filename=(video_name + ".mp4")),)
    except:
        print("Error")


video_url = input("enter the video URL: ")

download_background_video(video_url)
