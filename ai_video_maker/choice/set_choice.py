import inquirer


def set_choice(title, choices):
    while True:
        choice_keys = []
        choice_values = []

        for key, value in choices.items():
            choice_keys.append(key)
            choice_values.append(value)

        choice = inquirer.list_input(title, choices=choice_keys)

        # Execute function based on selected choice
        func = choice_values[choice_keys.index(choice)]

        if func is not None:
            func()
