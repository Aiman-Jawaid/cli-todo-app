# Data Model: In-Memory Todo CLI Application (Phase I)

**Date**: 2026-01-01
**Feature**: 1-todo-cli-app

## Todo Entity

### Attributes
- **ID** (Integer): Unique identifier for each todo, auto-incremented
  - Required: Yes
  - Type: Integer
  - Constraints: Positive integer, unique across all todos
  - Example: 1, 2, 3, etc.

- **Title** (String): The main description of the task
  - Required: Yes
  - Type: String
  - Constraints: Non-empty string, maximum 200 characters
  - Example: "Buy groceries", "Complete homework assignment"

- **Description** (String): Additional details about the task
  - Required: No (optional)
  - Type: String
  - Constraints: Maximum 1000 characters, can be empty
  - Example: "Milk, bread, eggs, and fruits", "Due by Friday at 5pm"

- **Status** (Boolean): Completion status of the task
  - Required: Yes
  - Type: Boolean
  - Values: True (complete) or False (incomplete)
  - Default: False (incomplete)
  - Example: True, False

### Relationships
- No relationships with other entities (standalone entity)

### Validation Rules
- Title must be provided and not empty
- Title must be no more than 200 characters
- Description, if provided, must be no more than 1000 characters
- ID must be unique across all todos in memory
- Status must be a boolean value

### State Transitions
- Status can transition from False (incomplete) to True (complete)
- Status can transition from True (complete) to False (incomplete)
- All other attributes remain constant after creation except through update operations

## In-Memory Storage Structure

### Data Container
- **Type**: Dictionary (Python dict)
- **Key**: Todo ID (Integer)
- **Value**: Todo object containing all attributes
- **Example**:
```python
{
    1: {"id": 1, "title": "Buy groceries", "description": "Milk and bread", "status": False},
    2: {"id": 2, "title": "Call dentist", "description": "Schedule appointment", "status": True}
}
```

### ID Generation
- **Type**: Auto-incrementing integer
- **Starting value**: 1
- **Increment**: +1 for each new todo
- **Storage**: Class-level counter in the TodoService