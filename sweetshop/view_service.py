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

    