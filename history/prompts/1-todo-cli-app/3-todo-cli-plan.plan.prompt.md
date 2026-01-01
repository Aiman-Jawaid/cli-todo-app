---
id: 3
title: todo-cli-plan
stage: plan
date: 2026-01-01
surface: agent
model: Claude Sonnet 4.5
feature: 1-todo-cli-app
branch: 1-todo-cli-app
user: user
command: sp.plan
labels: [plan, todo, cli, architecture]
links:
  spec: specs/1-todo-cli-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-todo-cli-app/plan.md
  - specs/1-todo-cli-app/research.md
  - specs/1-todo-cli-app/data-model.md
  - specs/1-todo-cli-app/quickstart.md
  - specs/1-todo-cli-app/contracts/cli-contract.md
tests:
  - none
---

## Prompt

Create:
- High-level architecture sketch for an in-memory Python CLI Todo application
- Project section structure aligned with spec-driven development
- Development approach for implementing features incrementally
- Quality validation approach to ensure specs are correctly implemented

Decisions needing documentation:
- Choice of in-memory data structure (list vs dictionary)
- Todo ID generation strategy
- CLI menu flow and user interaction model
- Separation of concerns between UI, logic, and data
- Error handling and input validation strategy

Testing strategy:
- Validation checks derived from acceptance criteria in each feature spec
- Manual CLI testing scenarios for:
  - Adding a todo
  - Viewing todos
  - Updating todos
  - Deleting todos
  - Marking todos complete/incomplete
- Edge case validation (empty todo list, invalid IDs, invalid input types)

Technical details:
- Follow strict spec-driven development (no implementation before specs)
- Use an incremental build approach (one feature at a time)
- Keep architecture simple and beginner-friendly
- Organize work by phases:
  - Planning → Specification → Implementation → Validation
- No persistence, no external services, no frameworks

## Response snapshot

# Implementation Plan: In-Memory Todo CLI Application (Phase I)

**Branch**: `1-todo-cli-app` | **Date**: 2026-01-01 | **Spec**: [specs/1-todo-cli-app/spec.md](spec.md)
**Input**: Feature specification from `/specs/1-todo-cli-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a simple, reliable command-line Todo application using in-memory data structures, following clean architecture principles and spec-driven development. The application will provide CLI menu functionality for adding, viewing, updating, deleting, and marking todos as complete/incomplete. Built with Python 3.13+ for educational purposes with focus on beginner-friendly code structure.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Built-in Python libraries only (no external dependencies)
**Storage**: In-memory only using Python dictionaries and lists
**Testing**: Manual testing based on acceptance criteria from spec
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single project CLI application
**Performance Goals**: Fast operations (sub-second response time for all operations)
**Constraints**: No external dependencies, no file persistence, educational focus
**Scale/Scope**: Single-user, in-memory application with no concurrent access

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-Driven Development: All features defined in spec before implementation
- ✅ Clean Architecture & Code Quality: Clear separation of concerns planned
- ✅ In-Memory Data Only: Confirmed no database or file persistence
- ✅ Required Features Implementation: All 5 core features covered
- ✅ CLI-First Design: Text-based menu system planned
- ✅ Educational Focus: Beginner-friendly architecture planned

## Project Structure

### Documentation (this feature)
```text
specs/1-todo-cli-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
src/
├── models/
│   └── todo.py          # Todo entity and in-memory storage
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── cli/
│   └── main.py          # Main CLI application with menu system
└── lib/
    └── utils.py         # Utility functions (validation, formatting, etc.)

tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: Single project structure selected with clear separation of concerns. Models handle data representation and storage, services contain business logic, CLI contains user interface, and lib contains utility functions. This follows clean architecture principles while remaining beginner-friendly.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [N/A] | [No violations identified] | [All constitution requirements met] |

# Research: In-Memory Todo CLI Application (Phase I)

**Date**: 2026-01-01
**Feature**: 1-todo-cli-app

## Research Summary

This research document addresses the key technical decisions needed for implementing the in-memory Python CLI Todo application based on the feature specification.

## Decision: In-memory data structure choice

**Rationale**: For the in-memory storage of todos, Python dictionaries are the optimal choice because:
- Provide O(1) average time complexity for lookups, insertions, and deletions
- Allow for easy mapping of unique IDs to todo objects
- Are beginner-friendly and intuitive to work with
- Offer built-in methods for iteration, checking existence, and management
- Support the required functionality of the Todo entity with ID, title, description, and status

**Alternatives considered**:
- Lists: Less efficient for ID-based lookups (O(n) time complexity)
- Sets: Don't maintain key-value relationships needed for ID mapping
- Custom data structures: Unnecessarily complex for this educational project

## Decision: Todo ID generation strategy

**Rationale**: Using a simple auto-incrementing integer ID is the most appropriate approach because:
- It's simple and predictable for educational purposes
- Requires minimal implementation complexity
- Provides unique identification for each todo
- Follows common patterns seen in many applications
- Is easy to understand for beginner developers

**Implementation**: Maintain a class-level counter that increments with each new todo creation, starting from 1.

**Alternatives considered**:
- UUIDs: More complex and not necessary for this simple application
- Random numbers: Potential for collisions and harder to understand
- String-based IDs: More complex and unnecessary for this use case

## Decision: CLI menu flow and user interaction model

**Rationale**: A text-based menu system with numbered options provides the best balance of:
- Simplicity for beginners to understand and use
- Clear navigation and operation selection
- Consistent user experience across all operations
- Easy implementation with Python's built-in input() function
- Alignment with CLI-first design principle from constitution

**Menu structure**:
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete/Incomplete
6. Exit

**Alternatives considered**:
- Command-line arguments: Less user-friendly for interactive use
- Natural language processing: Overly complex for this educational project
- Sub-menus: Would add unnecessary complexity

## Decision: Separation of concerns between UI, logic, and data

**Rationale**: Separating the application into distinct layers improves:
- Code maintainability and readability
- Testability of business logic separate from UI
- Clear understanding of responsibilities for educational purposes
- Ability to modify one layer without affecting others
- Alignment with clean architecture principles from constitution

**Layers**:
- Models (`todo.py`): Data representation and in-memory storage
- Services (`todo_service.py`): Business logic and operations
- CLI (`main.py`): User interface and input handling
- Utils (`utils.py`): Shared utility functions

**Alternatives considered**:
- Single file approach: Would not follow clean architecture principles
- More complex layering: Would be unnecessarily complex for this project

## Decision: Error handling and input validation strategy

**Rationale**: Graceful error handling using Python's try-except blocks and input validation functions ensures:
- Users receive helpful error messages when providing invalid input
- Application continues running after errors rather than crashing
- Educational value in showing proper error handling techniques
- Compliance with requirement FR-008 (handle invalid input gracefully)

**Strategy**:
- Validate user input before processing
- Use try-except blocks for error-prone operations
- Provide clear, user-friendly error messages
- Return to main menu after displaying errors

**Alternatives considered**:
- No error handling: Would result in crashes and poor user experience
- Complex exception hierarchy: Unnecessarily complex for this project

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

## Outcome

- ✅ Impact: Created comprehensive implementation plan with architecture, research, data model, quickstart, and contracts
- 🧪 Tests: none
- 📁 Files: 5 files created (specs/1-todo-cli-app/plan.md, research.md, data-model.md, quickstart.md, contracts/cli-contract.md)
- 🔁 Next prompts: Proceed to task creation with /sp.tasks
- 🧠 Reflection: Plan addresses all requested technical decisions and provides complete architecture for implementation

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): All constitution checks passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task creation with /sp.tasks