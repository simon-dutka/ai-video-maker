import inquirer
from modules import makeDir, getsId, getRedditApi, changeReadyStatus, makeStoryFiles

choices = ['Make directory structure', 'Make files structure', 'Get posts ID\'s', 'Set ready status', 'Exit']
isExit = False

def get_choice():
    choice = inquirer.list_input("What's we gonna do today?",
        choices=choices)
    return  choices.index(choice)
    

while isExit == False:
    choiceIndex = get_choice()


    match choiceIndex:
        case 0:
            makeDir.make_dir()
        case 1:
            makeStoryFiles.make_story_files(getRedditApi.get_reddit())
        case 2:
            getsId.gets_id(getRedditApi.get_subreddit())
        case 3:
            changeReadyStatus.change_ready_status()
        case 4:
            isExit = True
