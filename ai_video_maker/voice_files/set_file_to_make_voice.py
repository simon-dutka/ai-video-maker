import os
import json
from .make_voice_file import make_voice_file
from ai_video_maker.choice import set_choice


def set_file_to_make_voice():
    choices = {}

    for directory in os.listdir("./stories"):
        if os.path.isdir(f"stories/{directory}"):
            with open(f"stories/{directory}/info.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, dict):
                    if data.get("status") == "Ready to make audio":
                        choices[directory] = lambda: make_voice_file(directory)

    if (len(choices)) > 0:
        return set_choice("Set file to make audio", choices)
    else:
        print("No files to make audio")
