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
