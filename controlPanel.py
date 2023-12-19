import inquirer
from modules import makeDir, makeFiles, getsId, getRedditApi

choices = ['Make directory structure', 'Make files structure', 'Get posts ID\'s', 'Exit']
isExit = False

while isExit == False:
    choice = inquirer.list_input("What's we gonna do today?",
        choices=choices)

    choiceIndex = choices.index(choice)

    if choiceIndex == 0:
        makeDir.make_dir()
    elif choiceIndex == 1:
        makeFiles.make_files(getRedditApi.get_reddit_api())
    elif choiceIndex == 2:
        getsId.gets_id(getRedditApi.get_reddit_api())
    elif choiceIndex == 3:
        isExit = True
