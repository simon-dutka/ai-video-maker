import os
import json
from ai_video_maker.choice import set_choice

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def change_status(file_to_change_status, new_status):
    with open(f"./stories/{file_to_change_status}/info.json", "r") as file:
        data = json.load(file)

    data["status"] = new_status

    with open(f"./stories/{file_to_change_status}/info.json", "w") as file:
        json.dump(data, file, indent=4)
