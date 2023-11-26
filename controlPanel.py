import makeDir, makeFiles
import inquirer

choices = ['Make directory structure', 'Make files structure', 'Exit']
isExit = False

while isExit == False:
    choice = inquirer.list_input("What's we gonna do today?",
        choices=choices)

    choiceIndex = choices.index(choice)

    if choiceIndex == 0:
        makeDir.make_dir()
    elif choiceIndex == 1:
        makeFiles.make_files()
    elif choiceIndex == 2:
        isExit = True
