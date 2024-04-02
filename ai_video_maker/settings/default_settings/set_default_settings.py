from .set_all_default import set_all_default
from .set_part_default import show_parts
from ai_video_maker.choice.set_choice import set_choice


def set_default_settings():
    choices = {
        "Set all of settings as default": set_all_default,
        "Set part of settings as default": show_parts,
        "Exit": None,
    }

    return set_choice(
        "Set settings as default",
        choices,
    )
