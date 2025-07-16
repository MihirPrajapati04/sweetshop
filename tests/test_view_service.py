import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.view_service import ViewSweetService  # To be created

class TestViewSweetService(unittest.TestCase):
    """
    Unit tests for the ViewSweetService class.
    """

    def setUp(self):
        self.db = DBManager()
        self.db.connect()
        self.service = ViewSweetService(self.db)

        # Insert sample data
        self.db.cursor.execute("DELETE FROM sweets")
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (2001, "Imarti", "Fried", 25.0, 30))
        self.db.conn.commit()

    def tearDown(self):
        self.db.clear_db()
        self.db.close()

    def test_view_all_sweets_returns_list(self):
        """
        Test that view_all_sweets returns a non-empty list of Sweet instances.
        """
        sweets = self.service.view_all_sweets()  # Method to be implemented

        self.assertIsInstance(sweets, list, "Returned value is not a list.")
        self.assertEqual(len(sweets), 1, "Expected exactly one sweet in the list.")
        self.assertIsInstance(sweets[0], Sweet, "List item is not a Sweet instance.")
        self.assertEqual(sweets[0].name, "Imarti", "Sweet name does not match expected value.")

    def test_view_all_sweets_returns_empty_list_when_no_records(self):
        """
        Test that view_all_sweets returns an empty list when no sweets exist in the database.
        """
        # Clean DB explicitly to ensure it's empty
        self.db.cursor.execute("DELETE FROM sweets")
        self.db.conn.commit()

        sweets = self.service.view_all_sweets()

        self.assertIsInstance(sweets, list, "Returned value is not a list.")
        self.assertEqual(len(sweets), 0, "Expected an empty list when no sweets exist.")
