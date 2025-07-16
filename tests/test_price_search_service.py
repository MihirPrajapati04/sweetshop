import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.price_search_service import PriceSearchService  # To be implemented

class TestPriceSearchService(unittest.TestCase):
    """
    Unit tests for the PriceSearchService class.
    """

    def setUp(self):
        self.db = DBManager()
        self.db.connect()
        self.service = PriceSearchService(self.db)

        self.db.cursor.execute("DELETE FROM sweets")

        # Insert test data
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (5001, "Kheer", "Milk-Based", 45.0, 10))
        self.db.conn.commit()

    def tearDown(self):
        self.db.clear_db()
        self.db.close()

    def test_search_by_price_range_returns_matching_sweets(self):
        """
        Test that sweets within a price range are returned.
        """
        result = self.service.search_by_price_range(30.0, 50.0)

        self.assertIsInstance(result, list, "Expected result to be a list.")
        self.assertEqual(len(result), 1, "Expected one matching sweet.")
        self.assertEqual(result[0].name, "Kheer", "Sweet name does not match expected.")
        self.assertGreaterEqual(result[0].price, 30.0, "Price is below minimum range.")
        self.assertLessEqual(result[0].price, 50.0, "Price is above maximum range.")
