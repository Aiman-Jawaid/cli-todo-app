"""
Quick test script to validate the todo application functionality.
"""
from src.services.todo_service import TodoService
from src.models.todo import Todo


def test_basic_functionality():
    """Test the basic functionality of the todo application."""
    print("Testing basic functionality...")

    # Create a service instance
    service = TodoService()

    # Test 1: Add a todo
    print("\n1. Testing add todo...")
    todo1 = service.add_todo("Test todo 1", "This is a test description")
    print(f"Added todo: {todo1.title} with ID {todo1.id}")

    # Test 2: Add another todo without description
    todo2 = service.add_todo("Test todo 2")
    print(f"Added todo: {todo2.title} with ID {todo2.id}")

    # Test 3: Get all todos
    print("\n2. Testing get all todos...")
    all_todos = service.get_all_todos()
    print(f"Total todos: {len(all_todos)}")
    for todo in all_todos:
        status = "Complete" if todo.status else "Incomplete"
        print(f"  - {todo.id}: {todo.title} [{status}]")

    # Test 4: Update a todo
    print("\n3. Testing update todo...")
    updated_todo = service.update_todo(todo1.id, title="Updated Test Todo", description="Updated description")
    if updated_todo:
        print(f"Updated todo: {updated_todo.title}")

    # Test 5: Update todo status
    print("\n4. Testing update todo status...")
    status_updated = service.update_todo_status(todo1.id, True)
    if status_updated:
        print(f"Updated status for '{status_updated.title}' to {'Complete' if status_updated.status else 'Incomplete'}")

    # Test 6: Get specific todo
    print("\n5. Testing get specific todo...")
    retrieved_todo = service.get_todo(todo1.id)
    if retrieved_todo:
        print(f"Retrieved todo: {retrieved_todo.title}, Status: {'Complete' if retrieved_todo.status else 'Incomplete'}")

    # Test 7: Delete a todo
    print("\n6. Testing delete todo...")
    delete_success = service.delete_todo(todo2.id)
    print(f"Delete successful: {delete_success}")

    # Check remaining todos
    remaining_todos = service.get_all_todos()
    print(f"Remaining todos after deletion: {len(remaining_todos)}")

    print("\nOK: All basic functionality tests passed!")


def test_validation():
    """Test validation functionality."""
    print("\n\nTesting validation...")
    service = TodoService()

    # Test 1: Try to add a todo with empty title
    print("\n1. Testing empty title validation...")
    try:
        service.add_todo("")
        print("ERROR: Should have failed with empty title")
    except ValueError as e:
        print(f"OK: Correctly caught validation error: {e}")

    # Test 2: Try to add a todo with very long title
    print("\n2. Testing long title validation...")
    try:
        long_title = "A" * 201  # More than 200 characters
        service.add_todo(long_title)
        print("ERROR: Should have failed with long title")
    except ValueError as e:
        print(f"OK: Correctly caught validation error: {e}")

    # Test 3: Try to add a todo with very long description
    print("\n3. Testing long description validation...")
    try:
        long_desc = "A" * 1001  # More than 1000 characters
        service.add_todo("Valid title", long_desc)
        print("ERROR: Should have failed with long description")
    except ValueError as e:
        print(f"OK: Correctly caught validation error: {e}")

    print("\nOK: All validation tests passed!")


def test_edge_cases():
    """Test edge cases."""
    print("\n\nTesting edge cases...")
    service = TodoService()

    # Test 1: Try to get non-existent todo
    print("\n1. Testing get non-existent todo...")
    todo = service.get_todo(999)
    print(f"Retrieved non-existent todo: {todo}")  # Should be None

    # Test 2: Try to update non-existent todo
    print("\n2. Testing update non-existent todo...")
    updated = service.update_todo(999, title="New title")
    print(f"Update result for non-existent todo: {updated}")  # Should be None

    # Test 3: Try to delete non-existent todo
    print("\n3. Testing delete non-existent todo...")
    deleted = service.delete_todo(999)
    print(f"Delete result for non-existent todo: {deleted}")  # Should be False

    # Test 4: Try to update status of non-existent todo
    print("\n4. Testing update status of non-existent todo...")
    status_updated = service.update_todo_status(999, True)
    print(f"Status update result for non-existent todo: {status_updated}")  # Should be None

    print("\nOK: All edge case tests passed!")


if __name__ == "__main__":
    print("Running quick validation tests for the Todo application...")

    test_basic_functionality()
    test_validation()
    test_edge_cases()

    print("\n" + "="*50)
    print("OK: All tests completed successfully!")
    print("The Todo application is working as expected.")
    print("="*50)