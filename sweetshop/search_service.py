"""
Service module responsible for searching sweets by name.
"""

from models.sweet import Sweet

class SearchSweetService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.
        """
        self.db = db_manager

    def search_by_name(self, name):
        """
        Searches for sweets with an exact name match (case-insensitive).

        Args:
            name (str): The name to search for.

        Returns:
            List[Sweet]: List of matching Sweet records.
        """
        self.db.cursor.execute("""
            SELECT * FROM sweets WHERE LOWER(name) = LOWER(?)
        """, (name,))
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
