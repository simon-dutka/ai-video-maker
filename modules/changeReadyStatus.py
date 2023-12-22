import inquirer, os

dir_path = './stories'

def change_ready_status():
    is_exit = False

    while is_exit == False:
        files = []
        folders_in_dir = [
                folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
        ]

        for i in range(len(folders_in_dir)):
            if 'check' in folders_in_dir[i]:
                files.append(folders_in_dir[i])

        files.append('Exit')

        choice = inquirer.list_input("Which files you checked?",
        choices=files)

        if choice == 'Exit':
             is_exit = True
        else:
            choiceIndex = folders_in_dir.index(choice)
            new_folder_name = 'stories/' + folders_in_dir[choiceIndex].replace('check', 'ready')
            os.rename('stories/' + folders_in_dir[choiceIndex], new_folder_name)
            files.clear()