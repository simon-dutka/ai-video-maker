import os
from ai_video_maker.choice import set_choice

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def change_status(file_to_change_status):
    print("works")
