import sqlite3
import os

class DBManager:
    def __init__(self, db_name="sweetshop_test.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sweets (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    def clear_db(self):
        self.cursor.execute("DROP TABLE IF EXISTS sweets")
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
