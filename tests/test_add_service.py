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


    def test_add_sweet_stores_correct_name(self):
        """
        Test to verify that the sweet name is correctly stored in the database.
        """
        sweet = Sweet(
            id=1002,
            name="Rasgulla",
            category="Milk-Based",
            price=30.0,
            quantity=10
        )

        # Act
        self.service.add_sweet(sweet)

        # Assert
        result = self.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (1002,)).fetchone()
        self.assertEqual(result[1], "Rasgulla", "Stored sweet name does not match expected name.")

    def test_add_sweet_stores_correct_category(self):
        """
        Test to verify that the sweet category is correctly stored in the database.
        """
        sweet = Sweet(
            id=1003,
            name="Soan Papdi",
            category="Flaky",
            price=35.0,
            quantity=15
        )

        # Act
        self.service.add_sweet(sweet)

        # Assert
        result = self.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (1003,)).fetchone()
        self.assertEqual(result[2], "Flaky", "Stored sweet category does not match expected category.")


    def test_add_sweet_stores_correct_price(self):
        """
        Test to verify that the sweet price is correctly stored in the database.
        """
        sweet = Sweet(
            id=1004,
            name="Barfi",
            category="Milk-Based",
            price=45.5,
            quantity=12
        )

        # Act
        self.service.add_sweet(sweet)

        # Assert
        result = self.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (1004,)).fetchone()
        self.assertEqual(result[3], 45.5, "Stored sweet price does not match expected price.")

    def test_add_sweet_stores_correct_quantity(self):
        """
        Test to verify that the sweet quantity is correctly stored in the database.
        """
        sweet = Sweet(
            id=1005,
            name="Ladoo",
            category="Gram Flour",
            price=20.0,
            quantity=50
        )

        # Act
        self.service.add_sweet(sweet)

        # Assert
        result = self.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (1005,)).fetchone()
        self.assertEqual(result[4], 50, "Stored sweet quantity does not match expected quantity.")
