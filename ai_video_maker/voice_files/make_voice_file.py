import requests, json, os, re

with open(".secret/keys.json", "r") as f:
    keys = json.load(f)

# my_file = open("stories/story0001 - empty/story0001.txt", "r")
# textFile = my_file.read()

dir_path = "stories"

folders_in_dir = [
    folder
    for folder in os.listdir(dir_path)
    if os.path.isdir(os.path.join(dir_path, folder))
]


def make_voice_file(story_file_name):
    CHUNK_SIZE = 1024

    voice_model_id = "dPfEIZvhnol9pjmS6M7F"
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_model_id

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": keys["ELEVEN_LABS_API_KEY"],
    }

    stories_id = {
        "text": "textFile",
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }

    voice_file_name = re.sub(" - Ready to make audio", "", story_file_name)

    response = requests.post(url, json=stories_id, headers=headers)
    with open(f"stories/{story_file_name}/{voice_file_name}.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
