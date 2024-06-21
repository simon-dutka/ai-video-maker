def get_id(subreddit):
    id_to_check = []
    with open("stories_id/used_stories_id.txt", "r+") as used_stories_id:
        # ToDo: Add match new id's to this str
        all_id = used_stories_id.readlines()

    #     for i in range(0, len(all_id)):
    #         id_to_check.append(all_id[i])

    def check_if_was_used(word, list):
        if word in list:
            print("The word is in the list!")
        else:
            print("The word is not in the list!")

    print(all_id)
    check_if_was_used("192ziqg\n", all_id)

    with open("stories_id/stories_id.txt", "w") as stories_id:
        for post in subreddit.top(time_filter="day", limit=100):
            stories_id.write(post.id + "\n")
