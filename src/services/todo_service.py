"""
TodoService providing business logic for todo operations.
"""
from typing import List, Optional
from src.models.todo import Todo, InMemoryTodoStorage


class TodoService:
    """
    Service class handling business logic for todo operations.
    """

    def __init__(self):
        """Initialize the TodoService with in-memory storage."""
        self.storage = InMemoryTodoStorage()

    def add_todo(self, title: str, description: Optional[str] = None) -> Todo:
        """
        Add a new todo.

        Args:
            title: Title of the todo (required, 1-200 characters)
            description: Optional description of the todo (0-1000 characters)

        Returns:
            Todo: The newly created Todo instance

        Raises:
            ValueError: If title validation fails
        """
        # Validation is handled in the Todo constructor
        return self.storage.add_todo(title, description)

    def get_todo(self, id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            id: The ID of the todo to retrieve

        Returns:
            Todo: The todo if found, None otherwise
        """
        try:
            return self.storage.get_todo(id)
        except Exception:
            return None

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos.

        Returns:
            List[Todo]: List of all todos
        """
        try:
            return self.storage.get_all_todos()
        except Exception:
            return []

    def update_todo(self, id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Todo]:
        """
        Update an existing todo.

        Args:
            id: ID of the todo to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            Todo: Updated todo if successful, None if todo doesn't exist

        Raises:
            ValueError: If title validation fails
        """
        try:
            return self.storage.update_todo(id, title, description)
        except Exception:
            return None

    def update_todo_status(self, id: int, status: bool) -> Optional[Todo]:
        """
        Update the status of a todo.

        Args:
            id: ID of the todo to update
            status: New status for the todo

        Returns:
            Todo: Updated todo if successful, None if todo doesn't exist
        """
        try:
            return self.storage.update_todo_status(id, status)
        except Exception:
            return None

    def delete_todo(self, id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            id: ID of the todo to delete

        Returns:
            bool: True if deleted, False if todo didn't exist
        """
        try:
            return self.storage.delete_todo(id)
        except Exception:
            return False

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            int: The next available ID
        """
        return self.storage.get_next_id()