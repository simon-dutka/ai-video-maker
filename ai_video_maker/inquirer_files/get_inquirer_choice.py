import inquirer


def get_inquirer_choice(message, list_with_choices):
    choice = inquirer.list_input(message, choices=list_with_choices)
    return list_with_choices.index(choice)
