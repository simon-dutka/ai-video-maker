import makeDir
import inquirer

choices = ['Make directory structure', 'Exit']
isExit = False

while isExit == False:
    choice = inquirer.list_input("What's we gonna do today?",
        choices=choices)

    choiceIndex = choices.index(choice)

    if choiceIndex == 0:
        makeDir.makeDirectory()
    elif choiceIndex == 1:
        isExit = True
