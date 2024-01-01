from ai_video_maker.inquirer_files.get_inquirer_choice import get_inquirer_choice
from .set_own_subreddit import set_own_subreddit

def set_subreddit():
    choices = ['Set own subreddit', 'List of most popular subreddits to set', 'Show using subreddits', 'Exit']
    isExit = False

    while isExit == False:
        choiceIndex = get_inquirer_choice("Subreddit settings", choices)

        match choiceIndex:
            case 0:
                set_own_subreddit()
            case 1:
                list_of_subreddits()
            case 3:
                show_using_subreddits()
            case 4:
                isExit = True
