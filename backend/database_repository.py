"""Database repository for managing quotes and jokes using SQLite."""

import sqlite3
import random
from typing import Dict, List

class DatabaseRepository:
    """Class to handle database operations for quotes and jokes."""
    def __init__(self, db_path: str = "repository.db"):
        """Initialize the database connection and create table if not exists.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self._create_table()
        
    def _create_table(self) -> None:
        """Create the content table if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS content (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT NOT NULL CHECK(type IN ('quote', 'joke')),
                    content TEXT NOT NULL
                )
            """)
            conn.commit()
    
    def get_random_quote(self) -> Dict[str, str]:
        """Get a random quote from the database.
        
        Returns:
            Dict[str, str]: Dictionary containing the quote type and content
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT content FROM content WHERE type = 'quote' ORDER BY RANDOM() LIMIT 1")
            result = cursor.fetchone()
            
            if result:
                return {"type": "quote", "content": result[0]}
            return {"type": "quote", "content": "No quotes available"}
    
    def get_random_joke(self) -> Dict[str, str]:
        """Get a random joke from the database.
        
        Returns:
            Dict[str, str]: Dictionary containing the joke type and content
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT content FROM content WHERE type = 'joke' ORDER BY RANDOM() LIMIT 1")
            result = cursor.fetchone()
            
            if result:
                return {"type": "joke", "content": result[0]}
            return {"type": "joke", "content": "No jokes available"}
    
    def get_random_content(self) -> Dict[str, str]:
        """Get either a random quote or joke.
        
        Returns:
            Dict[str, str]: Dictionary containing the content type and text
        """
        content_type = random.choice(["quote", "joke"])
        if content_type == "quote":
            return self.get_random_quote()
        elif content_type == "joke":
            return self.get_random_joke()
    
    def add_content(self, content_type: str, content: str) -> bool:
        """Add new content to the database.
        
        Args:
            content_type (str): Type of content ('quote' or 'joke')
            content (str): The actual content text
            
        Returns:
            bool: True if content was added successfully, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO content (type, content) VALUES (?, ?)",
                    (content_type, content)
                )
                conn.commit()
                return True
        except sqlite3.Error:
            return False
    
    def get_all_content(self) -> List[Dict[str, str]]:
        """Get all content from the database.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing all content
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT type, content FROM content")
            results = cursor.fetchall()
            return [{"type": row[0], "content": row[1]} for row in results] 
