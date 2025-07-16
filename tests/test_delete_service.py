import unittest
from database.db import DBManager
from models.sweet import Sweet
from sweetshop.delete_service import DeleteSweetService  # To be implemented

class TestDeleteSweetService(unittest.TestCase):
    """
    Unit tests for the DeleteSweetService class.
    """

    def setUp(self):
        self.db = DBManager()
        self.db.connect()
        self.service = DeleteSweetService(self.db)

        self.db.cursor.execute("DELETE FROM sweets")

        # Insert one record to delete
        self.db.cursor.execute("""
            INSERT INTO sweets (id, name, category, price, quantity)
            VALUES (?, ?, ?, ?, ?)
        """, (6001, "Jalebi", "Fried", 28.0, 40))
        self.db.conn.commit()

    def tearDown(self):
        self.db.clear_db()
        self.db.close()

    def test_delete_sweet_removes_record_by_id(self):
        """
        Test that delete_sweet removes the sweet with the given ID.
        """
        self.service.delete_sweet(6001)

        result = self.db.cursor.execute("SELECT * FROM sweets WHERE id = ?", (6001,)).fetchone()
        self.assertIsNone(result, "Sweet record was not deleted.")

    def test_delete_sweet_does_not_fail_for_nonexistent_id(self):
        """
        Test that deleting a non-existent sweet ID does not raise an error.
        """
        try:
            self.service.delete_sweet(9999)  # ID not in DB
        except Exception as e:
            self.fail(f"delete_sweet raised an exception for non-existent ID: {e}")
