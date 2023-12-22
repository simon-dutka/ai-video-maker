# Get last (first of five) created folder
import os, re

dir_path = './stories'

def make_story_files(reddit):
    folders_in_dir = [
            folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
    ]
    
    def create_story_file():
        # Get Title and selfText by ID's & put into file texts
        for directory in os.listdir('./stories'):
     
            if 'empty' in directory:
                with open("data/stories_id.txt", "r+") as stories_id:
                    first_line = stories_id.readline()
                    lines = stories_id.readlines()
                    
                    file_name = int(re.sub('[a-z]', '', directory).replace(' - ', ''))
                    with open(f'stories/{directory}/story{file_name:04d}.txt', "wb") as story_file:
                        output = f"{reddit.submission(id=first_line).title + '\n\n' +  reddit.submission(id=first_line).selftext}"

                        output = output.replace('AITA', 'Am I The Asshole')
                        story_file.write(output.encode("utf-8"))

                        stories_id.seek(0)
                        stories_id.truncate()
                        stories_id.writelines(lines[1:])

    create_story_file()

    def change_dir_name(nameToChange, newName):
        for i in range(len(folders_in_dir)):
            if nameToChange in folders_in_dir[i]:
                folder_name = folders_in_dir[i]
                new_folder_name = 'stories/' + folders_in_dir[i].replace(nameToChange, newName)
                os.rename('stories/' + folders_in_dir[i], new_folder_name)

    change_dir_name('empty', 'check')
