import os
import re
from ai_video_maker.directory import change_dir_name
from ai_video_maker.statuses import change_status_available_files

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def make_story_files(reddit):
    folders_in_dir = [
        folder
        for folder in os.listdir(dir_path)
        if os.path.isdir(os.path.join(dir_path, folder))
    ]

    # Get Title and selfText by ID's & put into file texts
    for directory in os.listdir("./stories"):
        if os.path.isdir(f"stories/{directory}"):
            with open("stories_id/stories_id.txt", "r+") as stories_id:
                first_line = stories_id.readline()
                lines = stories_id.readlines()

                with open("stories_id/used_stories_id.txt", "a") as used_stories_id:
                    used_stories_id.write(first_line)
                file_name = int(re.sub("[a-z]|[A-Z]", "", directory))

                with open(
                    f"stories/{directory}/story{file_name:04d}.txt", "wb"
                ) as story_file:
                    output = f"{reddit.submission(id=first_line).title}\n\n{reddit.submission(id=first_line).selftext}"

                    output = output.replace("AITA", "Am I The Asshole")
                    story_file.write(output.encode("utf-8"))

                    stories_id.seek(0)
                    stories_id.truncate()
                    stories_id.writelines(lines[1:])
            change_status_available_files(directory, "story file")
