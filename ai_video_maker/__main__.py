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


class exit_status:
    def __init__(self, is_exit):
        self.is_exit = is_exit

    def change_exit_status(self):
        self.is_exit = True


is_exit = exit_status(False)

choices = [
    "Make directory structure",
    "Make story files",
    "Make voice files",
    "Make video files",
    "Get posts ID's",
    "Statuses",
    "Settings",
    "Exit",
]

choices_functions = [
    make_dir,
    lambda: make_story_files(get_reddit()),
    set_file_to_make_voice,
    make_video_files,
    lambda: gets_id(get_subreddit()),
    statuses,
    settings,
    is_exit.change_exit_status,
]

while is_exit.is_exit == False:
    choiceIndex = get_inquirer_choice("What's we gonna do today?", choices)

    choices_functions[choiceIndex]()
