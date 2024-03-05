from .story_files.make_story_files import make_story_files
from .voice_files.set_file_to_make_voice import set_file_to_make_voice
from .video_files.make_video_files import make_video_files
from .api.get_reddit_api import get_reddit
from .api.gets_id import gets_id
from .directory.make_dir import make_dir
from .api.get_reddit_api import get_subreddit
from .settings.settings import settings
from .statuses.statuses import statuses
from .manual.manual import manual
from .one_click_video.one_click_video import one_click_video
from .download_background_video.download_background_video import (
    download_background_video,
)
from .choice.set_choice import set_choice


choices = {
    "One click video": one_click_video,
    "Make directory structure": make_dir,
    "Make story files": lambda: make_story_files(get_reddit()),
    "Make audio files": set_file_to_make_voice,
    "Make video files": make_video_files,
    "Download background": lambda: download_background_video(
        input("Enter the video URL: ")
    ),
    "Get posts ID's": lambda: gets_id(get_subreddit()),
    "Statuses": statuses,
    "Settings": settings,
    "Manual": manual,
    "Exit": None,
}

set_choice(choices, "What's we gonna do today?")
