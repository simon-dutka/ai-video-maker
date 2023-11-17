import os

dir_path = './'

folders_in_dir = [
    folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
]

folders_in_dir_last = folders_in_dir[len(folders_in_dir) - 1].replace("story", "")

temp = int(folders_in_dir_last)
for i in range(temp + 1, temp + 6):
    temp = temp + 1
    os.mkdir("story" + str(temp).zfill(3))

