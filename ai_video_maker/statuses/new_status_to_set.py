from .change_status import change_status
from ai_video_maker.choice import set_choice


def new_status_to_set(dir):
    choices = {}

    statuses = ["Ready to create audio"]

    for status in statuses:
        choices[status] = lambda dir=dir: change_status(dir, status)

    return set_choice("Set new status", choices)
