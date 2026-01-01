# In-Memory Todo CLI Application (Phase I)

This is a simple, reliable command-line Todo application using in-memory data structures, following clean architecture principles and spec-driven development. The application provides CLI menu functionality for adding, viewing, updating, deleting, and marking todos as complete/incomplete.

## Features

- Add new todos with title and optional description
- View all todos with their completion status
- Mark todos as complete/incomplete
- Update existing todos (title and description)
- Delete todos by ID
- Input validation and error handling
- Logging for debugging

## Architecture

The application follows a clean architecture pattern with clear separation of concerns:

- **Models** (`src/models/`): Data representation and in-memory storage
- **Services** (`src/services/`): Business logic and operations
- **CLI** (`src/cli/`): User interface and input handling
- **Lib** (`src/lib/`): Utility functions and logging

## Files

- `src/models/todo.py`: Contains the Todo model and in-memory storage implementation
- `src/services/todo_service.py`: Contains business logic for todo operations
- `src/cli/main.py`: Main CLI application with menu system
- `src/lib/utils.py`: Utility functions for validation and formatting
- `src/lib/logger.py`: Simple logging implementation

## Usage

Run the application with:

```bash
python -m src.cli.main
```

The application will display a menu with options to manage your todos.

## Validation

All functionality has been tested and validated:
- Basic CRUD operations work correctly
- Input validation is properly implemented
- Error handling is in place
- All edge cases are handled appropriately

## Technical Details

- Built with Python 3.13+
- No external dependencies
- In-memory storage only (data is lost when the application exits)
- Beginner-friendly code structure