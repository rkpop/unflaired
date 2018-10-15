import sqlite3


class database:
    def __init__(self, filename):
        self.db = sqlite3.connect(filename)
        self.cursor = self.db.cursor()

    def check(self, submission_id):
        query = """SELECT count(*) FROM {table} WHERE ID=?""".format(
            table="REPORTS"
        )
        self.cursor.execute(query, (submission_id,))
        (row_count,) = self.cursor.fetchone()
        return row_count == 0

    def write(self, submission_id):
        query = """INSERT INTO {table} VALUES(?)""".format(table="REPORTS")
        self.cursor.execute(query, (submission_id,))
        self.db.commit()

    @staticmethod
    def generate_file(filename):
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS {table}(ID TEXT)
            """.format(
                table="REPORTS"
            )
        )
        db.commit()
        cursor.close()
        db.close()
