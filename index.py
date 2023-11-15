import elevenlabs
story = open('./historyName.txt', "r").read()

storyArr = story.split()

count = 0
separatedStory = ''

for i in storyArr:
    separatedStory += i
    separatedStory += " "
    if(i[len(i) - 1] == "." or i[len(i) - 1] == "?" or i[len(i) - 1] == "!" and count > 20):
        separatedStory += "\n\n"
        count = 0
    else:
        count += 1
        
story = open('./historyName.txt', "w")

story.write(separatedStory)

# cutText = 

# audio = elevenlabs.generate(
#   text=story,
#   voice="Bella",
#   model="eleven_multilingual_v2"
# )

# elevenlabs.save(audio, "audio.mp3")