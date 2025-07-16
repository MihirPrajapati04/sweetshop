import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.inventory_service import InventoryService  # To be implemented

class TestInventoryService(unittest.TestCase):
    """
    Unit tests for the InventoryService class, focused on purchasing sweets.
    """

    def setUp(self):
        self.db = DBManager()
        self.db.connect()
        self.service = InventoryService(self.db)

        self.db.cursor.execute("DELETE FROM sweets")
        self.db.conn.commit()

        # Insert a sweet with stock
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (7001, "Peda", "Milk-Based", 15.0, 50))
        self.db.conn.commit()

    def tearDown(self):
        self.db.clear_db()
        self.db.close()

    def test_purchase_sweet_decreases_quantity(self):
        """
        Test that purchasing a sweet reduces its quantity in stock.
        """
        self.service.purchase_sweet(7001, 10)

        updated_quantity = self.db.cursor.execute(
            "SELECT quantity FROM sweets WHERE id = ?", (7001,)
        ).fetchone()[0]

        self.assertEqual(updated_quantity, 40, "Quantity not correctly reduced after purchase.")

    def test_purchase_raises_error_when_stock_insufficient(self):
        """
        Test that purchasing more than available stock raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.service.purchase_sweet(7001, 60)  # Only 50 in stock

        self.assertEqual(
            str(context.exception),
            "Not enough stock available.",
            "Incorrect error message for insufficient stock."
        )

    def test_purchase_raises_error_when_sweet_id_invalid(self):
        """
        Test that purchasing a non-existent sweet raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.service.purchase_sweet(9999, 5)  # No such ID

        self.assertEqual(
            str(context.exception),
            "Sweet with the given ID does not exist.",
            "Incorrect error message for invalid sweet ID."
        )

    def test_restock_sweet_increases_quantity(self):
        """
        Test that restocking a sweet increases its quantity.
        """
        self.service.restock_sweet(7001, 20)  # Original quantity was 50

        updated_quantity = self.db.cursor.execute(
            "SELECT quantity FROM sweets WHERE id = ?", (7001,)
        ).fetchone()[0]

        self.assertEqual(updated_quantity, 70, "Quantity was not correctly increased after restocking.")
