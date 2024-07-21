import os
import json
from .make_video_files import make_video_files
from ai_video_maker.choice import set_choice


def set_file_to_make_video():
    choices = {}

    for directory in os.listdir("./stories"):
        if os.path.isdir(f"stories/{directory}"):
            with open(f"stories/{directory}/info.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, dict):
                    if data.get("status") == "Ready to make video":
                        choices[directory] = lambda: make_video_files(directory)

    if (len(choices)) > 0:
        return set_choice("Set file to make video", choices)
    else:
        print("No files to make video")
