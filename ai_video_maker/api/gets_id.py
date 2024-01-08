def gets_id(subreddit):
    with open("stories_id/stories_id.txt", "w") as stories_id:
        for post in subreddit.top(time_filter="day", limit=100):
            stories_id.write(post.id + "\n")
