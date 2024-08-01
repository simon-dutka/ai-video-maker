import requests
import json
import os

with open(".secret/keys.json", "r") as f:
    keys = json.load(f)

dir_path = "./stories"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

folders_in_dir = [
    folder
    for folder in os.listdir(dir_path)
    if os.path.isdir(os.path.join(dir_path, folder))
]


def make_audio_file(story_file_name):
    CHUNK_SIZE = 1024

    voice_model_id = "ErXwobaYiN019PkySvjV"
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_model_id

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": keys["ELEVEN_LABS_API_KEY"],
    }

    story_text = ""

    with open(f"stories/{story_file_name}/{story_file_name}.txt", "r") as story_file:
        story_text = story_file.read()

    stories_id = {
        "text": story_text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }

    response = requests.post(url, json=stories_id, headers=headers)
    with open(f"stories/{story_file_name}/{story_file_name}.mp3", "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
