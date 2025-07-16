"""
Service module responsible for searching sweets by price range.
"""

from models.sweet import Sweet

class PriceSearchService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.
        """
        self.db = db_manager

    def search_by_price_range(self, min_price, max_price):
        """
        Retrieves sweets whose prices fall within the given range (inclusive).

        Args:
            min_price (float): Minimum price.
            max_price (float): Maximum price.

        Returns:
            List[Sweet]: Matching sweets in the given price range.
        """
        self.db.cursor.execute("""
            SELECT * FROM sweets
            WHERE price BETWEEN ? AND ?
        """, (min_price, max_price))
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
