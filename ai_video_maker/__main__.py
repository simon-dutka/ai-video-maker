import inquirer

from story_files.make_story_files import make_story_files
from inquirer_files.get_inquirer_choice import get_inquirer_choice
from voice_files.make_voice_files import make_voice_files
from video_files.make_video_files import make_video_files
from api.get_reddit_api import get_reddit
from api.gets_id import gets_id
from directory.change_ready_status import change_ready_status
from directory.make_dir import make_dir
from api.get_reddit_api import get_subreddit

choices = ['Make directory structure', 'Make story files', 'Make voice files', 'make video files', 'Get posts ID\'s', 'Set ready status', 'Exit']
isExit = False

def get_choice():
    choice = inquirer.list_input("What's we gonna do today?",
        choices=choices)
    return  choices.index(choice)
    
while isExit == False:
    choiceIndex = get_choice()

    match choiceIndex:
        case 0:
            make_dir()
        case 1:
            make_story_files(get_reddit())
        case 2:
            make_voice_files()
        case 3:
            make_video_files()
        case 4:
            gets_id(get_subreddit())
        case 5:
            change_ready_status()
        case 6:
            isExit = True
