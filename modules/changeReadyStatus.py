import inquirer, os
# import changeDirName

files = []

dir_path = './stories'

folders_in_dir = [
            folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
    ]

def change_ready_status():
    for i in range(len(folders_in_dir)):
        if 'check' in folders_in_dir[i]:
            files.append(folders_in_dir[i])
    print(files)

    choice = inquirer.list_input("Which files you checked?",
    choices=files)
