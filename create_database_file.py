from config import config as cf
from database import database as db

db.generate_file(cf("config.toml").db_config()["filename"])
