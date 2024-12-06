import sqlite3

class Database:
    def __init__(self, db_name="finance_manager.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )"""
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            budget_limit REAL
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS savings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL
            )
            """
        )

        self.connection.commit()
    
    def close(self):
        self.connection.close()