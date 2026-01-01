"""
Main CLI application for the Todo application.
"""
from src.services.todo_service import TodoService
from src.lib.utils import validate_title, validate_description, format_todo_display, get_integer_input, confirm_action
from src.lib.logger import logger
from typing import Optional


class TodoCLI:
    """
    Command-line interface for the Todo application.
    """

    def __init__(self):
        """Initialize the CLI with a TodoService."""
        self.service = TodoService()
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Mark Todo Complete/Incomplete")
        print("4. Update Todo")
        print("5. Delete Todo")
        print("6. Exit")
        print("="*40)

    def add_todo(self):
        """Handle adding a new todo."""
        print("\n--- Add New Todo ---")

        while True:
            title = input("Enter title: ").strip()
            if not validate_title(title):
                print("Title is required and must be 1-200 characters long.")
                continue
            break

        description_input = input("Enter description (optional, press Enter to skip): ").strip()
        description = description_input if description_input else None

        if description and not validate_description(description):
            print("Description must be 1000 characters or less.")
            return

        try:
            todo = self.service.add_todo(title, description)
            print(f"Successfully added todo: {todo.title}")
            logger.info(f"Added todo with ID {todo.id}: {todo.title}")
        except ValueError as e:
            print(f"Error adding todo: {e}")
            logger.error(f"Failed to add todo: {e}")

    def view_todos(self):
        """Handle viewing all todos."""
        print("\n--- All Todos ---")
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos found.")
            return

        for todo in todos:
            print(format_todo_display(todo))
            print("-" * 30)

    def mark_todo_status(self):
        """Handle marking a todo as complete/incomplete."""
        print("\n--- Mark Todo Status ---")
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos available to mark.")
            return

        print("Current todos:")
        for todo in todos:
            status = "Complete" if todo.status else "Incomplete"
            print(f"ID: {todo.id} - {todo.title} [{status}]")

        try:
            todo_id = get_integer_input("Enter the ID of the todo to update: ", min_value=1)

            # Check if the todo exists
            todo = self.service.get_todo(todo_id)
            if not todo:
                print(f"No todo found with ID {todo_id}")
                return

            # Ask for new status
            current_status = "Complete" if todo.status else "Incomplete"
            new_status = input(f"Current status is {current_status}. Set to (c)omplete or (i)ncomplete? ").strip().lower()

            if new_status in ['c', 'complete']:
                new_status_bool = True
            elif new_status in ['i', 'incomplete']:
                new_status_bool = False
            else:
                print("Invalid choice. Please enter 'c' for complete or 'i' for incomplete.")
                return

            updated_todo = self.service.update_todo_status(todo_id, new_status_bool)
            if updated_todo:
                new_status_str = "Complete" if new_status_bool else "Incomplete"
                print(f"Todo '{updated_todo.title}' marked as {new_status_str}")
                logger.info(f"Updated status for todo ID {todo_id} to {new_status_str}")
            else:
                print("Error updating todo status")
                logger.error(f"Failed to update status for todo ID {todo_id}")

        except ValueError:
            print("Please enter a valid ID.")

    def update_todo(self):
        """Handle updating an existing todo."""
        print("\n--- Update Todo ---")
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos available to update.")
            return

        print("Current todos:")
        for todo in todos:
            status = "Complete" if todo.status else "Incomplete"
            print(f"ID: {todo.id} - {todo.title} [{status}]")

        try:
            todo_id = get_integer_input("Enter the ID of the todo to update: ", min_value=1)

            # Check if the todo exists
            todo = self.service.get_todo(todo_id)
            if not todo:
                print(f"No todo found with ID {todo_id}")
                return

            print(f"Current todo: {todo.title}")
            if todo.description:
                print(f"Current description: {todo.description}")

            # Get new title (or keep current)
            new_title_input = input(f"Enter new title (current: '{todo.title}', press Enter to keep current): ").strip()
            new_title = new_title_input if new_title_input else None

            # Validate new title if provided
            if new_title and not validate_title(new_title):
                print("Title must be 1-200 characters long.")
                return

            # Get new description (or keep current)
            current_desc = todo.description if todo.description else ""
            new_desc_input = input(f"Enter new description (current: '{current_desc}', press Enter to keep current): ").strip()
            new_description = new_desc_input if new_desc_input != "" else None

            # If the user entered an empty string, they want to clear the description
            if new_desc_input == "":
                new_description = None

            # Validate new description if provided
            if new_description is not None and not validate_description(new_description):
                print("Description must be 1000 characters or less.")
                return

            # Update the todo
            updated_todo = self.service.update_todo(todo_id, new_title, new_description)
            if updated_todo:
                print(f"Todo updated successfully: {updated_todo.title}")
                logger.info(f"Updated todo with ID {todo_id}")
            else:
                print("Error updating todo")
                logger.error(f"Failed to update todo with ID {todo_id}")

        except ValueError:
            print("Please enter a valid ID.")

    def delete_todo(self):
        """Handle deleting a todo."""
        print("\n--- Delete Todo ---")
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos available to delete.")
            return

        print("Current todos:")
        for todo in todos:
            status = "Complete" if todo.status else "Incomplete"
            print(f"ID: {todo.id} - {todo.title} [{status}]")

        try:
            todo_id = get_integer_input("Enter the ID of the todo to delete: ", min_value=1)

            # Check if the todo exists
            todo = self.service.get_todo(todo_id)
            if not todo:
                print(f"No todo found with ID {todo_id}")
                return

            # Confirm deletion
            if confirm_action(f"Are you sure you want to delete '{todo.title}'?"):
                success = self.service.delete_todo(todo_id)
                if success:
                    print("Todo deleted successfully.")
                    logger.info(f"Deleted todo with ID {todo_id}")
                else:
                    print("Error deleting todo")
                    logger.error(f"Failed to delete todo with ID {todo_id}")
            else:
                print("Deletion cancelled.")

        except ValueError:
            print("Please enter a valid ID.")

    def exit_app(self):
        """Handle exiting the application."""
        print("Thank you for using the Todo application!")
        self.running = False

    def handle_choice(self, choice: str):
        """Handle the user's menu choice."""
        try:
            if choice == "1":
                self.add_todo()
            elif choice == "2":
                self.view_todos()
            elif choice == "3":
                self.mark_todo_status()
            elif choice == "4":
                self.update_todo()
            elif choice == "5":
                self.delete_todo()
            elif choice == "6":
                self.exit_app()
            else:
                print("Invalid choice. Please select a valid option (1-6).")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo CLI Application!")

        while self.running:
            try:
                self.display_menu()
                choice = input("Select an option (1-6): ").strip()
                self.handle_choice(choice)
            except KeyboardInterrupt:
                print("\n\nApplication interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")


def main():
    """Main entry point for the application."""
    logger.info("Todo application started")
    app = TodoCLI()
    app.run()
    logger.info("Todo application ended")


if __name__ == "__main__":
    main()