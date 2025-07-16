"""
Service module for handling inventory-related operations like purchasing and restocking.
"""

class InventoryService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.
        """
        self.db = db_manager

    def purchase_sweet(self, sweet_id, quantity):
        """
        Purchases a sweet by reducing its quantity in stock.

        Args:
            sweet_id (int): The ID of the sweet to purchase.
            quantity (int): The quantity to purchase.

        Raises:
            ValueError: If stock is insufficient or sweet ID is invalid.
        """
        self.db.cursor.execute("SELECT quantity FROM sweets WHERE id = ?", (sweet_id,))
        row = self.db.cursor.fetchone()

        if row is None:
            raise ValueError("Sweet with the given ID does not exist.")

        current_quantity = row[0]
        if quantity > current_quantity:
            raise ValueError("Not enough stock available.")

        new_quantity = current_quantity - quantity
        self.db.cursor.execute(
            "UPDATE sweets SET quantity = ? WHERE id = ?",
            (new_quantity, sweet_id)
        )
        self.db.conn.commit()

    def restock_sweet(self, sweet_id, quantity):
            """
            Increases the quantity of a sweet in stock.

            Args:
                sweet_id (int): The ID of the sweet to restock.
                quantity (int): The quantity to add to stock.

            Raises:
                ValueError: If the sweet ID does not exist.
            """
            self.db.cursor.execute("SELECT quantity FROM sweets WHERE id = ?", (sweet_id,))
            row = self.db.cursor.fetchone()

            if row is None:
                raise ValueError("Sweet with the given ID does not exist.")

            current_quantity = row[0]
            new_quantity = current_quantity + quantity

            self.db.cursor.execute(
                "UPDATE sweets SET quantity = ? WHERE id = ?",
                (new_quantity, sweet_id)
            )
            self.db.conn.commit()

