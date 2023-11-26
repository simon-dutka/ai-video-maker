# Get last (first of five) created folder
# print(dir_to_upload_files)
import os
dir_path = './stories'

folders_in_dir = [
        folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
]

def change_dir_name(nameToChange, newName):
    for i in range(len(folders_in_dir)):
        if nameToChange in folders_in_dir[i]:
            folder_name = folders_in_dir[i]
            new_folder_name = 'stories/' + folders_in_dir[i].replace(nameToChange, newName)
            os.rename('stories/' + folders_in_dir[i], new_folder_name)

change_dir_name('empty', 'check')
