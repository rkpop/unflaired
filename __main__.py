from reddit import reddit as r
from config import config as c


def main():
    config = c("config.toml")
    reddit = r(config.reddit_config())
    for submission in reddit.return_new_instance():
        print(reddit.check_submission_time(submission))


if __name__ == "__main__":
    main()
