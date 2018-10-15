from reddit import reddit as r
from config import config as c
from database import database as db
import os


def main():
    config = c(os.path.join(os.getcwd(), "scripts", "unflaired", "config.toml"))
    reddit = r(config.reddit_config())
    database = db(config.db_config())
    while True:
        submissions = reddit.return_new_instance()
        for submission in submissions:
            if (
                reddit.check_submission_time(submission)
                and reddit.check_submission_flair(submission)
                and database.check(submission.id)
            ):
                reddit.report_submission(submission)
                database.write(submission.id)
        reddit.new_time()


if __name__ == "__main__":
    main()
