import os
from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice

dir_path = './stories'

files = []

def get_status_to_set():
    choices = ['Check story', 'Ready to make audio', 'Check audio', 'Ready to make video', 'Check video', 'Ready to upload' ,'Exit']

    is_exit = False

    while is_exit == False:
        choiceIndex = get_inquirer_choice("Set type of status to set", choices)

        match choiceIndex:
            case 0:
                change_ready_status(change_ready_status(choices[choiceIndex]))
            case 2:
                is_exit == True
    

def change_ready_status(status_to_set):
    isExit = False

    while isExit == False:
        folders_in_dir = [
                folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
        ]

        for i in range(len(folders_in_dir)):
            if 'check' in folders_in_dir[i]:
                files.append(folders_in_dir[i])

        files.append('Exit')

        choiceIndex = get_inquirer_choice('Which files you checked?', files)

        print('selected' + files[choiceIndex])

        if files[choiceIndex] == 'Exit':
            isExit = True
        else:
            new_folder_name = 'stories/' + folders_in_dir[choiceIndex].replace('check', 'ready')
            os.rename('stories/' + folders_in_dir[choiceIndex], new_folder_name)
        
        files.clear()
