# CLI Interface Contract: In-Memory Todo CLI Application (Phase I)

**Date**: 2026-01-01
**Feature**: 1-todo-cli-app

## Overview
This contract defines the command-line interface behavior for the Todo application. The interface follows a menu-driven approach with numbered options for different operations.

## Main Menu Interface

### Input Requirements
- The application accepts integer input corresponding to menu options
- Input validation ensures only valid menu numbers are processed
- Invalid input results in an error message and menu re-display

### Menu Options
1. **Add Todo**
   - Prompts for: Title (required), Description (optional)
   - Validation: Title must not be empty
   - Success: Todo added to in-memory list, returns to main menu
   - Error: Displays error message, returns to main menu

2. **View Todos**
   - Input: None required after selection
   - Output: Lists all todos with ID, Title, Description, and Status
   - Format: "ID: [id] - [Title] - [Description] - [Status: Complete/Incomplete]"
   - If no todos: Displays "No todos found" message

3. **Update Todo**
   - Input: Todo ID to update
   - Prompts for: New Title (optional), New Description (optional)
   - Validation: Todo with given ID must exist
   - Success: Updates specified fields, returns to main menu
   - Error: Displays error message, returns to main menu

4. **Delete Todo**
   - Input: Todo ID to delete
   - Validation: Todo with given ID must exist
   - Confirmation: Asks for confirmation before deletion
   - Success: Removes todo from list, returns to main menu
   - Error: Displays error message, returns to main menu

5. **Mark Todo Complete/Incomplete**
   - Input: Todo ID to update
   - Prompts for: New status (Complete/Incomplete)
   - Validation: Todo with given ID must exist
   - Success: Updates status, returns to main menu
   - Error: Displays error message, returns to main menu

6. **Exit**
   - Terminates the application
   - All in-memory data is lost upon exit

## Error Handling Contract
- All invalid inputs result in user-friendly error messages
- Application continues running after errors (does not crash)
- Error messages clearly explain what went wrong and how to proceed

## Data Validation Contract
- Title: Required, 1-200 characters
- Description: Optional, 0-1000 characters
- ID: Positive integer that exists in the current todo list
- Status: Boolean value (complete/incomplete)

## State Management Contract
- All todos exist only in memory during application runtime
- Data persists only while the application is running
- All data is lost when the application exits
- No persistence to files, databases, or external systems