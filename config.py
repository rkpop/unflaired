from toml import load as lo
import os


class config:
    def __init__(self, filename):
        self.configfile = lo(filename)

    def reddit_config(self):
        return self.configfile["Reddit"]

    def db_config(self):
        return os.path.join(
            os.getcwd(),
            "scripts",
            "unflaired",
            self.configfile["sqlite3"]["filename"],
        )
