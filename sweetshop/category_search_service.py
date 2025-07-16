"""
Service module responsible for searching sweets by category.
"""

from models.sweet import Sweet

class CategorySearchService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.
        """
        self.db = db_manager

    def search_by_category(self, category):
        """
        Searches for sweets with a matching (case-insensitive) category.

        Args:
            category (str): The category to search by.

        Returns:
            List[Sweet]: List of matching Sweet records.
        """
        self.db.cursor.execute("""
            SELECT * FROM sweets
            WHERE LOWER(category) = LOWER(?)
        """, (category,))
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
