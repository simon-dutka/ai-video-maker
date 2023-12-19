import os, re

def make_dir():
    dir_path = './stories'

    # If /story is empty make first dir
    if not os.listdir(dir_path):
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
        
        folder_name = f"story{folders_in_dir_last:04d} - empty"

        path = os.path.join(dir_path, folder_name)
        os.makedirs(path)