import os
import json
import re

from .create_info import create_info

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def update_statuses_statistics():
    statistics_file = "./statistics.md"

    def not_exists(file_name, else_func_name):
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                pass
        else:
            else_func_name()

    def get_statistics_md():
        with open(statistics_file, "r") as f:
            statuses_markdown_data = f.read()
            numbers = re.findall(r"\d+", statuses_markdown_data)
            numbers = [int(num) for num in numbers]
            return numbers

    def get_statistics_json():
        with open("statistics.json", "r") as f:
            statuses_json_data = json.load(f)
            return statuses_json_data

    not_exists("statistics.md", get_statistics_md)
    not_exists("statistics.json", get_statistics_json)

    def check_statuses():
        stories_path = "./stories"
        story_dirs = [
            d
            for d in os.listdir(stories_path)
            if os.path.isdir(os.path.join(stories_path, d))
        ]

        finded_statuses = []

        for story in story_dirs:
            info_json_path = os.path.join(stories_path, story, "info.json")

            if os.path.exists(info_json_path):
                with open(info_json_path, "r") as f:
                    data = f.read()
                    pattern = r"\"status\"\s*:\s*\"([^\"]*)\""
                    match = re.search(pattern, data)
                    if match:
                        status_value = match.group(1)
                        finded_statuses.append(status_value)
            else:
                create_info(info_json_path, story)

        statuses_counts = {}

        for status in finded_statuses:
            if status in statuses_counts:
                statuses_counts[status] += 1
            else:
                statuses_counts[status] = 1

        print(statuses_counts)

        # ToDo: Print statuses with 0 value

    check_statuses()
