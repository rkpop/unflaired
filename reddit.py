from praw import Reddit
from pprint import pprint as pp


class reddit:
    def __init__(self, configuration_details):
        self.instance = Reddit(
            client_id=configuration_details["client_id"],
            client_secret=configuration_details["client_secret"],
            username=configuration_details["username"],
            password=configuration_details["password"],
            user_agent="/r/kpop Unflaired 0.1 by /u/jonicrecis",
        )
        self.subreddit = self.instance.subreddit("kpop+kpophelp+kpoppers")

    def return_new_instance(self):
        return self.subreddit.new()

    def check_instance(self, submission):
        pp(submission.link_flair_text)
