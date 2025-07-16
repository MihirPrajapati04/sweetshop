"""
Service module responsible for viewing sweets from the database.
"""

from models.sweet import Sweet

class ViewSweetService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.
        """
        self.db = db_manager

    def view_all_sweets(self):
        """
        Retrieves all sweets from the database and returns them as a list of Sweet instances.

        Returns:
            List[Sweet]: All sweet records from the database.
        """
        self.db.cursor.execute("SELECT * FROM sweets")
        rows = self.db.cursor.fetchall()

        return [
            Sweet(
                id=row[0],
                name=row[1],
                category=row[2],
                price=row[3],
                quantity=row[4]
            ) for row in rows
        ]

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
