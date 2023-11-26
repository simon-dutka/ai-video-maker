import makeDir, makeFiles
import inquirer

choices = ['Make directory structure', 'Make files structure', 'Exit']
isExit = False

while isExit == False:
    choice = inquirer.list_input("What's we gonna do today?",
        choices=choices)

    choiceIndex = choices.index(choice)

    if choiceIndex == 0:
        makeDir.makeDirectory()
    elif choiceIndex == 1:
        makeFiles.makeFiles()
    elif choiceIndex == 2:
        isExit = True
