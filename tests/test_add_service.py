import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.add_service import AddSweetService  # Service to be implemented

class TestAddSweetService(unittest.TestCase):
    """
    Unit test class for testing the AddSweetService using unittest framework.
    This follows TDD — starting with a failing test before implementing the actual logic.
    """

    @classmethod
    def setUpClass(cls):
        """
        Called once before all test methods. Initializes the test database
        and sets up the AddSweetService instance.
        """
        cls.db = DBManager()  # Using a test-specific SQLite DB
        cls.db.connect()
        cls.service = AddSweetService(cls.db)  # Service under test (to be implemented)

    def setUp(self):
        """
        Runs before each test method.
        Ensures database table is cleaned to maintain test isolation.
        """
        cls = self.__class__
        cls.db.cursor.execute("DELETE FROM sweets")  # Delete existing rows
        cls.db.conn.commit()

    def test_add_sweet_inserts_record(self):
        """
        First minimal test to verify that a record is inserted into the database.
        Only checks if the record exists.
        """
        sweet = Sweet(
            id=1001,
            name="Kaju Katli",
            category="Nut-Based",
            price=50.0,
            quantity=20
        )

        # Act
        self.__class__.service.add_sweet(sweet)

        # Assert
        self.__class__.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (1001,))
        result = self.__class__.db.cursor.fetchone()

        self.assertIsNotNone(result, "Sweet was not inserted in the database.")


    @classmethod
    def tearDownClass(cls):
        """
        Called once after all test methods complete.
        Drops the table and closes the DB connection.
        """
        cls.db.clear_db()
        cls.db.close()
