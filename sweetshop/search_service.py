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
        Searches for sweets by partial (case-insensitive) name match.

        Args:
            name (str): The name or part of name to search for.

        Returns:
            List[Sweet]: List of matching Sweet records.
        """
        query = """
            SELECT * FROM sweets
            WHERE LOWER(name) LIKE LOWER(?)
        """
        self.db.cursor.execute(query, (f"%{name}%",))
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
