"""
Todo model representing a task with an ID, title, description, and completion status.
"""
from typing import Dict, List, Optional


class Todo:
    """
    Represents a todo item with ID, title, description, and status.
    """

    def __init__(self, id: int, title: str, description: Optional[str] = None, status: bool = False):
        """
        Initialize a Todo instance.

        Args:
            id: Unique identifier for the todo
            title: Required title of the todo (1-200 characters)
            description: Optional description of the todo (0-1000 characters)
            status: Boolean indicating completion status (default: False)
        """
        if not title or len(title.strip()) == 0:
            raise ValueError("Title is required and cannot be empty")
        if len(title) > 200:
            raise ValueError("Title must be 200 characters or less")
        if description and len(description) > 1000:
            raise ValueError("Description must be 1000 characters or less")

        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.status = status  # False = incomplete, True = complete

    def __str__(self) -> str:
        """String representation of the Todo."""
        status_str = "Complete" if self.status else "Incomplete"
        desc_str = f" - {self.description}" if self.description else ""
        return f"{self.id}: {self.title}{desc_str} - [{status_str}]"

    def to_dict(self) -> Dict:
        """Convert the Todo to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }


class InMemoryTodoStorage:
    """
    In-memory storage for todos using a dictionary.
    """

    def __init__(self):
        """Initialize the in-memory storage."""
        self._todos: Dict[int, Todo] = {}
        self._next_id = 1

    def add_todo(self, title: str, description: Optional[str] = None, status: bool = False) -> Todo:
        """
        Add a new todo to storage.

        Args:
            title: Title of the todo
            description: Optional description of the todo
            status: Initial status of the todo (default: False)

        Returns:
            Todo: The newly created Todo instance
        """
        todo = Todo(self._next_id, title, description, status)
        self._todos[todo.id] = todo
        self._next_id += 1
        return todo

    def get_todo(self, id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            id: The ID of the todo to retrieve

        Returns:
            Todo: The todo if found, None otherwise
        """
        return self._todos.get(id)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in storage.

        Returns:
            List[Todo]: List of all todos
        """
        return list(self._todos.values())

    def update_todo(self, id: int, title: Optional[str] = None, description: Optional[str] = None,
                   status: Optional[bool] = None) -> Optional[Todo]:
        """
        Update an existing todo.

        Args:
            id: ID of the todo to update
            title: New title (optional)
            description: New description (optional)
            status: New status (optional)

        Returns:
            Todo: Updated todo if successful, None if todo doesn't exist
        """
        if id not in self._todos:
            return None

        todo = self._todos[id]

        if title is not None:
            if not title or len(title.strip()) == 0:
                raise ValueError("Title is required and cannot be empty")
            if len(title) > 200:
                raise ValueError("Title must be 200 characters or less")
            todo.title = title.strip()

        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description must be 1000 characters or less")
            todo.description = description.strip() if description else None

        if status is not None:
            todo.status = status

        return todo

    def update_todo_status(self, id: int, status: bool) -> Optional[Todo]:
        """
        Update the status of a todo.

        Args:
            id: ID of the todo to update
            status: New status for the todo

        Returns:
            Todo: Updated todo if successful, None if todo doesn't exist
        """
        if id not in self._todos:
            return None

        todo = self._todos[id]
        todo.status = status
        return todo

    def delete_todo(self, id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            id: ID of the todo to delete

        Returns:
            bool: True if deleted, False if todo didn't exist
        """
        if id in self._todos:
            del self._todos[id]
            return True
        return False

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            int: The next available ID
        """
        return self._next_id