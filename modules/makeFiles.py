# Get last (first of five) created folder
# print(dir_to_upload_files)
import os, re
dir_path = './stories'

def make_files():
    folders_in_dir = [
            folder for folder in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, folder))
    ]
    
    # print(os.listdir('./stories'))
    print(folders_in_dir)
    # story_file = open("stories/story", "w")
    def create_story_file():
        for directory in os.listdir('./stories'):
            # print(directory)

            if 'empty' in directory:
                
                file_name = int(re.sub('[a-z]', '', directory).replace(' - ', ''))
                print(file_name)
                story_file = open(f'stories/{directory}/story{str(file_name).zfill(4)}.txt', "w")

    create_story_file()

    def change_dir_name(nameToChange, newName):
        for i in range(len(folders_in_dir)):
            if nameToChange in folders_in_dir[i]:
                folder_name = folders_in_dir[i]
                new_folder_name = 'stories/' + folders_in_dir[i].replace(nameToChange, newName)
                os.rename('stories/' + folders_in_dir[i], new_folder_name)

    change_dir_name('empty', 'check')

# Path('stories/file.txt').touch()