from toml import load as lo


class config:
    def __init__(self, filename):
        self.configfile = lo(filename)

    def reddit_config(self):
        return self.configfile["Reddit"]
