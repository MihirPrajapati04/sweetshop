import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.search_service import SearchSweetService  # To be implemented

class TestSearchSweetService(unittest.TestCase):
    """
    Unit tests for the SearchSweetService class.
    """

    def setUp(self):
        self.db = DBManager()
        self.db.connect()
        self.service = SearchSweetService(self.db)

        self.db.cursor.execute("DELETE FROM sweets")
        self.db.conn.commit()

        # Insert sample data
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (3001, "Gulab Jamun", "Milk-Based", 40.0, 25))
        self.db.conn.commit()

    def tearDown(self):
        self.db.clear_db()
        self.db.close()

    def test_search_sweet_by_exact_name(self):
        """
        Test that searching by exact name returns the correct sweet.
        """
        result = self.service.search_by_name("Gulab Jamun")

        self.assertIsInstance(result, list, "Expected result to be a list.")
        self.assertEqual(len(result), 1, "Expected exactly one matching sweet.")
        self.assertIsInstance(result[0], Sweet, "List item is not a Sweet instance.")
        self.assertEqual(result[0].name, "Gulab Jamun", "Sweet name does not match.")

    def test_search_sweet_by_partial_name(self):
        """
        Test that searching by partial name returns matching sweets.
        """
        result = self.service.search_by_name("Jamun")

        self.assertIsInstance(result, list, "Expected result to be a list.")
        self.assertGreaterEqual(len(result), 1, "Expected at least one matching sweet.")
        self.assertTrue(any("Jamun" in sweet.name for sweet in result), "No sweet contains 'Jamun' in the name.")
