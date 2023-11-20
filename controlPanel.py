import makeDir
import inquirer

choices = ['Make directory structure']

choice = inquirer.list_input("What's we gonna do today?",
    choices=choices)
choiceIndex = choices.index(choice)
print(choiceIndex)

if choiceIndex == 0:
    makeDir.makeDirectory()
