from ai_video_maker.story_files.make_story_files import make_story_files
from ai_video_maker.api.get_reddit_api import get_reddit
from ai_video_maker.audio_files.make_audio_file import make_audio_file


def one_click_video():
    make_story_files(get_reddit())
    # Argument bro
    make_audio_file()


# ToDo:
# Make story
# Make voice
# Make video
# Change status to ready to upload
