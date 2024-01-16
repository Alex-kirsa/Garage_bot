import os
import sqlite3

from conf import DEBUG


class DB:
    db_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "db.db" if not DEBUG else "test_db.sqlite", )

    def init_table(self):
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            users = """CREATE TABLE IF NOT EXISTS Users
                        (Id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                        User_id INTEGER UNIQUE,
                        Active INTEGER DEFAULT True, 
                        User_name TEXT,
                        User_tg TEXT)"""
            cursor.execute(users)

    def check_user(self, user_id):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'SELECT * FROM Users WHERE User_id=?'
            cursor.execute(query, [user_id])
            return cursor.fetchone()

    def add_user(self, data):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'INSERT INTO Users(User_id, Active, User_name, User_tg) VALUES(?,?,?,?)'
            cursor.execute(query, data)
