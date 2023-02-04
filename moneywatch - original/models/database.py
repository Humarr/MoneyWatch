import sqlite3
from models.androidly import Storage


class DatabaseManager:
    def __init__(self):
        self.integrity_error = sqlite3.IntegrityError()
        self.operational_error = sqlite3.OperationalError()
        self.path = Storage().storage()
        print(self.path)
        if self.path:
            # Notification().notification(title="title", text="text", icon_path="")
        # self.conn = sqlite3.connect("moneys.db")s
            self.conn = sqlite3.connect(f"{self.path}/money.db")
            self.cursor = self.conn.cursor()
        else:
            print("Not connecting database")
        # else:
        #     assert sqlite3.connect(f"{self.path}/money.db")
        #     self.cursor = self.conn.cursor()
        

    def build_tables(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS user_info (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(25) NOT NULL)")

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS budget (budget_id INTEGER PRIMARY KEY AUTOINCREMENT,email VARCHAR(255), budget INT NOT NULL, date DATE)")

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS categories (category_id INTEGER PRIMARY KEY AUTOINCREMENT, category_name VARCHAR(255))")

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT, email VARCHAR(255), item_bought VARCHAR(255), price VARCHAR(255), category_name VARCHAR(255), date DATE)")

        # self.cursor.execute("UPDATE  budget SET budget = ? WHERE email=? AND date LIKE '%2023-02%'", (27,000, "h@g.com"))
        # self.cursor.execute("DROP table budget")
        # self.cursor.execute("DROP table expenses")
        self.conn.commit()
DatabaseManager().build_tables()
