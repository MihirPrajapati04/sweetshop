"""
Service module responsible for deleting sweets by ID.
"""

class DeleteSweetService:
    def __init__(self, db_manager):
        """
        Initializes the service with a DBManager instance.
        """
        self.db = db_manager

    def delete_sweet(self, sweet_id):
        """
        Deletes a sweet record by its ID.

        Args:
            sweet_id (int): The ID of the sweet to be deleted.
        """
        self.db.cursor.execute("DELETE FROM sweets WHERE id = ?", (sweet_id,))
        self.db.conn.commit()
