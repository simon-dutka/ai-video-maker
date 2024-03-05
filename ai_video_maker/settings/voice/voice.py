from .set_own_voice import set_own_voice
from ai_video_maker.choice.set_choice import set_choice


def voice():
    choices = {
        "Set own voice": set_own_voice,
        # "List of voices to set": list_of_voices_to_set,
        # "List of using voices": list_of_using_voices,
        "Exit": None,
    }

    set_choice(choices, "Voice settings")
