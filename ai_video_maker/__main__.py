import os
from .story_files import make_story_files
from .audio_files import set_file_to_make_voice
from .make_video_files import choose_video_length
from .api import get_reddit, get_id, get_subreddit
from .directory import make_dir
from .settings import settings
from .statuses import statuses
from .manual import manual
from .one_click_video import one_click_video
from .download_background_video import download_background_video
from .choice import set_choice

choices = {
    "One click video": one_click_video,
    "Make directory structure": make_dir,
    "Make story files": lambda: make_story_files(get_reddit()),
    "Make audio files": set_file_to_make_voice,
    "Make video files": choose_video_length,
    "Download background": lambda: download_background_video(
        input("Enter the video URL: ")
    ),
    "Get posts ID's": lambda: get_id(get_subreddit()),
    "Statuses": statuses,
    "Settings": settings,
    "Manual": manual,
    "Exit": None,
}

# Clear console
os.system("cls")

set_choice(
    "What's we gonna do today?",
    choices,
)
