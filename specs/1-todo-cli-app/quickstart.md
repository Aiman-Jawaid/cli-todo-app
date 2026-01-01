# Quickstart Guide: In-Memory Todo CLI Application (Phase I)

**Date**: 2026-01-01
**Feature**: 1-todo-cli-app

## Overview
This guide provides instructions for setting up and running the in-memory Python CLI Todo application. The application allows users to manage todos through a command-line interface with no external dependencies.

## Prerequisites
- Python 3.13+ installed on your system
- Basic command-line knowledge

## Setup Instructions

1. **Clone or create the project structure:**
   ```
   src/
   ├── models/
   │   └── todo.py
   ├── services/
   │   └── todo_service.py
   ├── cli/
   │   └── main.py
   └── lib/
       └── utils.py
   ```

2. **Install dependencies:**
   No external dependencies required - only built-in Python libraries

3. **Run the application:**
   ```bash
   cd src/cli
   python main.py
   ```

## Running the Application

1. Navigate to the project directory
2. Execute: `python src/cli/main.py`
3. The main menu will appear with options to manage todos
4. Follow the on-screen prompts to perform operations

## First Use Example
1. Run the application
2. Select "Add Todo" from the menu
3. Enter a title for your new todo
4. Optionally add a description
5. Return to the main menu
6. Select "View Todos" to see your new todo
7. Continue using other menu options as needed

## Expected Output
- The application should display a clear menu with numbered options
- All operations should complete without errors
- Todos should be maintained in memory during the session
- When the application exits, all data will be lost (in-memory only)

## Troubleshooting
- If you get "python: command not found", ensure Python 3.13+ is installed and in your PATH
- If the application crashes, verify all required files are present in the correct directories
- For input validation errors, follow the prompts carefully and provide valid input