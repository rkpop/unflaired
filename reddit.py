from praw import Reddit
from pendulum import from_timestamp, now


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
        self.current_time = now("UTC")

    def return_new_instance(self):
        return self.subreddit.new()

    def check_submission_time(self, submission):
        return self._time_difference(submission.created_utc) > 1

    def check_submission_flair(self, submission):
        return submission.link_flair_text is None

    def report_submission(self, submission):
        submission.report("Post is not flaired after one hour.")
        return submission

    def _time_difference(self, submission_time):
        return self.current_time.diff(from_timestamp(submission_time)).in_hours()
