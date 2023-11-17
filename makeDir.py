import os

dir_path = './stories'

if len(os.listdir(dir_path)) == 0:
    path = os.path.join(dir_path, "story0001")
    os.makedirs(os.path.join(dir_path, "story0001"))

folders_in_dir = [
    folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
]

folders_in_dir_last = folders_in_dir[len(folders_in_dir) - 1].replace("story", "")
temp = int(folders_in_dir_last)
for i in range(temp + 1, temp + 6):
    temp = temp + 1

    folder_name = f"story{str(temp).zfill(4)}"
    path = os.path.join(dir_path, folder_name)
    os.makedirs(path)

