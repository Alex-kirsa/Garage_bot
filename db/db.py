import os
import sqlite3

from config.conf import DEBUG


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
                        User_tg TEXT,
                        Phone TEXT)"""
            cursor.execute(users)
            payments = """CREATE TABLE IF NOT EXISTS Payments
                                    (User_id INTEGER,
                                     Status TEXT CHECK (Status IN ('Open', 'Close', 'Paid')),
                                     link TEXT,
                                     Amount INTEGER,
                                     Name Text,
                                     Order_id TEXT, 
                                     DateField TEXT DEFAULT (strftime('%m-%Y', 'now', 'localtime')),
                                     FOREIGN KEY (User_id) REFERENCES Users(User_id)
                                     );"""
            cursor.execute(payments)

    def check_user(self, user_id):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'SELECT * FROM Users WHERE User_id = ?'
            cursor.execute(query, [user_id])
            return cursor.fetchone()

    def add_user(self, data):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'INSERT INTO Users(User_id, Active, User_name, User_tg, Phone) VALUES(?,?,?,?,?)'
            cursor.execute(query, data)

    def get_user(self, data):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'SELECT * FROM Users WHERE Phone=? or User_tg=?'
            cursor.execute(query, data)
            return cursor.fetchone()

    def add_receipts(self, data):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'UPDATE Payments SET Status=? WHERE User_id=?;'
            cursor.execute(query, ['Close', data[0]])
            query = 'INSERT INTO Payments (User_id, Status, link, Amount, Name, Order_id) VALUES(?,?,?,?,?,?);'
            cursor.execute(query, data)

    def get_user_receipts(self, user_id):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'SELECT * FROM Payments WHERE User_id=? and Status=?'
            cursor.execute(query, [user_id, 'Open'])
            return cursor.fetchone()

    def get_receipts(self):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'SELECT * FROM Payments WHERE Status=?'
            cursor.execute(query, ['Open'])
            return cursor.fetchall()

    def update_receipts(self, order_id, status):
        with sqlite3.connect(self.db_path) as db_connect:
            cursor = db_connect.cursor()
            query = 'UPDATE Payments SET Status=? WHERE Order_id=? and Status=?;'
            cursor.execute(query, ['Paid' if status == 'success' else 'Close', order_id, 'Open'])
            return cursor.fetchall()

