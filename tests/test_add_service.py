import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.add_service import AddSweetService

class TestAddSweetService(unittest.TestCase):
    """
    Unit test class for testing the AddSweetService using unittest framework.
    Follows the TDD cycle with one assertion per test method.
    """

    def setUp(self):
        """
        Runs before each test method.
        Creates a fresh DB connection and service instance, and clears the sweets table.
        """
        self.db = DBManager()
        self.db.connect()
        self.service = AddSweetService(self.db)
        self.db.cursor.execute("DELETE FROM sweets")
        self.db.conn.commit()

    def tearDown(self):
        """
        Runs after each test method.
        Drops the sweets table and closes the database connection.
        """
        self.db.clear_db()
        self.db.close()

    def test_add_sweet_inserts_record(self):
        """
        Test to verify that a sweet record is inserted into the database.
        """
        sweet = Sweet(
            id=1001,
            name="Kaju Katli",
            category="Nut-Based",
            price=50.0,
            quantity=20
        )

        # Act
        self.service.add_sweet(sweet)

        # Assert
        result = self.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (1001,)).fetchone()
        self.assertIsNotNone(result, "Sweet was not inserted into the database.")
