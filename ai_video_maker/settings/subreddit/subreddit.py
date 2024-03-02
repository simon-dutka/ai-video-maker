from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from .set_own_subreddit import set_own_subreddit
from .show_using_subreddits import show_using_subreddits


def subreddit():
    class exit_status:
        def __init__(self, is_exit):
            self.is_exit = is_exit

        def change_exit_status(self):
            self.is_exit = True

    is_exit = exit_status(False)

    choices = {
        "Set own subreddit": set_own_subreddit,
        "List of most popular subreddits to set": list_of_subreddits,
        "Show using subreddits": show_using_subreddits,
        "Exit": is_exit.change_exit_status,
    }

    is_exit = False

    while is_exit == False:
        choiceIndex = get_inquirer_choice("Subreddit settings", list(choices.keys()))

        choices[list(choices)[choiceIndex]]()
