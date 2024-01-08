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
isExit = False

while isExit is False:
    choiceIndex = get_inquirer_choice("What's we gonna do today?", choices)

    match choiceIndex:
        case 0:
            make_dir()
        case 1:
            make_story_files(get_reddit())
        case 2:
            set_file_to_make_voice()
        case 3:
            make_video_files()
        case 4:
            gets_id(get_subreddit())
        case 5:
            statuses()
        case 6:
            settings()
        case 7:
            isExit = True
