"""
Utility functions for input validation and formatting.
"""


def validate_title(title: str) -> bool:
    """
    Validate a todo title.

    Args:
        title: The title to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not title or len(title.strip()) == 0:
        return False
    if len(title) > 200:
        return False
    return True


def validate_description(description: str) -> bool:
    """
    Validate a todo description.

    Args:
        description: The description to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if description and len(description) > 1000:
        return False
    return True


def format_todo_display(todo) -> str:
    """
    Format a todo for display.

    Args:
        todo: The todo object to format

    Returns:
        str: Formatted string representation of the todo
    """
    status_str = "Complete" if todo.status else "Incomplete"
    desc_str = f"\n  Description: {todo.description}" if todo.description else ""
    return f"ID: {todo.id} - {todo.title}{desc_str}\n  Status: {status_str}"


def get_user_choice(prompt: str, valid_choices: list) -> str:
    """
    Get user choice from a list of valid choices.

    Args:
        prompt: The prompt to display to the user
        valid_choices: List of valid choices

    Returns:
        str: The user's choice
    """
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please select from: {', '.join(valid_choices)}")


def get_integer_input(prompt: str, min_value: int = None, max_value: int = None) -> int:
    """
    Get integer input from user with optional range validation.

    Args:
        prompt: The prompt to display to the user
        min_value: Minimum allowed value (optional)
        max_value: Maximum allowed value (optional)

    Returns:
        int: The user's integer input
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")


def confirm_action(prompt: str) -> bool:
    """
    Ask user to confirm an action.

    Args:
        prompt: The confirmation prompt

    Returns:
        bool: True if confirmed, False otherwise
    """
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")