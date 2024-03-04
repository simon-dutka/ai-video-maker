from .story_files.make_story_files import make_story_files
from .inquirer_files.get_inquirer_choice import get_inquirer_choice
from .voice_files.set_file_to_make_voice import set_file_to_make_voice
from .video_files.make_video_files import make_video_files
from .api.get_reddit_api import get_reddit
from .api.gets_id import gets_id
from .directory.make_dir import make_dir
from .api.get_reddit_api import get_subreddit
from .settings.settings import settings
from .statuses.statuses import statuses
from .manual.manual import manual
from one_click_video.one_click_video import one_click_video
from .download_background_video.download_background_video import (
    download_background_video,
)


class exit_status:
    def __init__(self, is_exit):
        self.is_exit = is_exit

    def change_exit_status(self):
        self.is_exit = True


is_exit = exit_status(False)

choices = {
    "One click video": one_click_video,
    "Make directory structure": make_dir,
    "Make story files": lambda: make_story_files(get_reddit()),
    "Make voice files": set_file_to_make_voice,
    "Make video files": make_video_files,
    "Download background": lambda: download_background_video(
        input("Enter the video URL: ")
    ),
    "Get posts ID's": lambda: gets_id(get_subreddit()),
    "Statuses": statuses,
    "Settings": settings,
    "Manual": manual,
    "Exit": is_exit.change_exit_status,
}

while is_exit.is_exit == False:
    choiceIndex = get_inquirer_choice("What's we gonna do today?", list(choices.keys()))

    choices[list(choices)[choiceIndex]]()
