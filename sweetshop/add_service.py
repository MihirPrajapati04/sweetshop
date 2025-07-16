"""
Service module responsible for adding sweets to the database.
"""

class AddSweetService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.

        Args:
            db_manager (DBManager): An instance to manage SQLite DB connection.
        """
        self.db = db_manager

    def add_sweet(self, sweet):
        """
        Inserts a sweet into the sweets table.

        Args:
            sweet (Sweet): The Sweet dataclass instance to be added to the database.
        """
        self.db.cursor.execute("""
        INSERT INTO sweets (id, name, category, price, quantity)
        VALUES (?, ?, ?, ?, ?)
        """, (sweet.id, sweet.name, sweet.category, sweet.price, sweet.quantity))
        self.db.conn.commit()
