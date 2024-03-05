from .set_own_subreddit import set_own_subreddit
from .show_using_subreddits import show_using_subreddits
from ai_video_maker.choice.set_choice import set_choice


def subreddit():
    choices = {
        "Set own subreddit": set_own_subreddit,
        # "List of most popular subreddits to set": list_of_subreddits,
        "Show using subreddits": show_using_subreddits,
        "Exit": None,
    }
    set_choice(choices, "Subreddit settings")
