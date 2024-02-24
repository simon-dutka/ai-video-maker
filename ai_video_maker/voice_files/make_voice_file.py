import requests, json, os, re

with open(".secret/keys.json", "r") as f:
    keys = json.load(f)

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
    voice_file_name = re.sub(" - Ready to make audio", "", story_file_name)

    story_text = ""

    with open(f"stories/{story_file_name}/{voice_file_name}.txt", "r") as story_file:
        story_text = story_file.read()

    stories_id = {
        "text": story_text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }

    response = requests.post(url, json=stories_id, headers=headers)
    with open(f"stories/{story_file_name}/{voice_file_name}.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
