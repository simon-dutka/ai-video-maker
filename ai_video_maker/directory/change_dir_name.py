import os

def change_dir_name(oldName, newName, dir, dir_path):
    for i in range(len(dir)):
        if oldName in dir[i]:
            folder_name = dir[i]
            new_folder_name = dir_path + dir[i].replace(oldName, newName)
            os.rename(dir_path + dir[i], new_folder_name)
