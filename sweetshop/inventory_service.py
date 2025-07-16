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
        """
        self.db.cursor.execute("SELECT quantity FROM sweets WHERE id = ?", (sweet_id,))
        row = self.db.cursor.fetchone()

        if row:
            current_quantity = row[0]
            new_quantity = current_quantity - quantity
            self.db.cursor.execute(
                "UPDATE sweets SET quantity = ? WHERE id = ?",
                (new_quantity, sweet_id)
            )
            self.db.conn.commit()
