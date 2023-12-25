import requests, json, os, re

with open ('.secret/keys.json', 'r') as f:
    keys = json.load(f)


def make_voice_files():
  dir_path = './stories'
    
  CHUNK_SIZE = 1024

  voice_model_id = 'dPfEIZvhnol9pjmS6M7F'
  url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_model_id

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": keys['ELEVEN_LABS_API_KEY']
  }

  data = {
    "text": "sample",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.5
    }
  }

  response = requests.post(url, json=data, headers=headers)
  with open('output.mp3', 'wb') as f:
      for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
          if chunk:
              f.write(chunk)
