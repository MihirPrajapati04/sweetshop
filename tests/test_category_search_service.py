import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.category_search_service import CategorySearchService  # To be created

class TestCategorySearchService(unittest.TestCase):
    """
    Unit tests for the CategorySearchService class.
    """

    def setUp(self):
        self.db = DBManager()
        self.db.connect()
        self.service = CategorySearchService(self.db)

        self.db.cursor.execute("DELETE FROM sweets")
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (4001, "Rabdi", "Milk-Based", 60.0, 12))
        self.db.conn.commit()

    def tearDown(self):
        self.db.clear_db()
        self.db.close()

    def test_search_sweet_by_category_exact_match(self):
        """
        Test that searching by exact category returns the correct sweet.
        """
        result = self.service.search_by_category("Milk-Based")

        self.assertIsInstance(result, list, "Expected result to be a list.")
        self.assertEqual(len(result), 1, "Expected one matching sweet.")
        self.assertIsInstance(result[0], Sweet, "Result item is not a Sweet instance.")
        self.assertEqual(result[0].category, "Milk-Based", "Category does not match expected.")
