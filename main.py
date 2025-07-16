from database.db import DBManager

if __name__ == "__main__":
    db = DBManager()
    db.connect()
    print("Database connected and table created.")
    db.clear_db()
    db.close()
    print("Database cleared and closed.")
