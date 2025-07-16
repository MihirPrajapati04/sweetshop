import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.view_service import ViewSweetService

class TestViewSweetService(unittest.TestCase):
    """
    Unit tests for the ViewSweetService class.
    """

    def setUp(self):
        """
        Runs before each test. Connects to the DB and clears the sweets table.
        """
        self.db = DBManager()
        self.db.connect()
        self.service = ViewSweetService(self.db)

        self.db.cursor.execute("DELETE FROM sweets")
        self.db.conn.commit()

    def tearDown(self):
        """
        Runs after each test. Drops the table and closes the DB.
        """
        self.db.clear_db()
        self.db.close()

    def _insert_sample_sweet(self, sweet: Sweet):
        """
        Helper method to insert a Sweet into the database.
        """
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (sweet.id, sweet.name, sweet.category, sweet.price, sweet.quantity))
        self.db.conn.commit()

    def test_view_all_sweets_returns_list(self):
        """
        Test that view_all_sweets returns a non-empty list of Sweet instances.
        """
        sweet = Sweet(
            id=2001,
            name="Imarti",
            category="Fried",
            price=25.0,
            quantity=30
        )
        self._insert_sample_sweet(sweet)

        sweets = self.service.view_all_sweets()

        self.assertIsInstance(sweets, list, "Returned value is not a list.")
        self.assertEqual(len(sweets), 1, "Expected exactly one sweet in the list.")
        self.assertIsInstance(sweets[0], Sweet, "List item is not a Sweet instance.")
        self.assertEqual(sweets[0].name, "Imarti", "Sweet name does not match expected value.")

    def test_view_all_sweets_returns_empty_list_when_no_records(self):
        """
        Test that view_all_sweets returns an empty list when no sweets exist in the database.
        """
        sweets = self.service.view_all_sweets()

        self.assertIsInstance(sweets, list, "Returned value is not a list.")
        self.assertEqual(len(sweets), 0, "Expected an empty list when no sweets exist.")
