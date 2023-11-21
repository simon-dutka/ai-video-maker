import os
import re
def makeDirectory():
    dir_path = './stories'

    if len(os.listdir(dir_path)) == 0:
        os.makedirs(os.path.join(dir_path, "story0001 - empty"))

    folders_in_dir = [
        folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
    ]

    folders_in_dir_last = folders_in_dir[len(folders_in_dir) - 1]
    folders_in_dir_last = int(re.sub('[a-z]', '', folders_in_dir_last).replace(' - ', ''))

    # Allows get name of first created dir
    num_of_loop = 0

    for i in range(folders_in_dir_last, folders_in_dir_last + 6):
        num_of_loop += 1
        folders_in_dir_last = folders_in_dir_last + 1
        
        folder_name = f"story{str(folders_in_dir_last).zfill(4)} - empty"

        path = os.path.join(dir_path, folder_name)
        os.makedirs(path)