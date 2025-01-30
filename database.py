import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            connection.execute("""
            CREATE TABLE IF NOT EXISTS homeworks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200),
            num_of_dz TEXT,
            link_to_github TEXT
            )
            """)



    def save_home_works(self, data: dict):
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                """ 
                        INSERT INTO homeworks(name, num_of_dz, link_to_github)
                        VALUES (?, ?, ?)
                    """,
              (data["name"], (data["num_of_dz"]), data["link_to_github"])
                    )