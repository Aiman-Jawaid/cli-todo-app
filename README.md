# The Evolution of Todo – Phase I: In-Memory Python Console App

## Overview
This project implements a simple in-memory command-line Todo application written in Python. It serves as an educational example of spec-driven development, progressing from simple CLI scripts to future cloud-native, distributed AI systems.

## Project Principles
This project follows the principles outlined in the [Constitution](.specify/memory/constitution.md):
- Spec-Driven Development: All features must be defined in specifications before implementation
- Clean Architecture & Code Quality: Readable, maintainable, beginner-friendly Python code
- In-Memory Data Only: No database or file persistence
- CLI-First Design: Text-based menu system with user-friendly messages
- Educational Focus: Prioritizes clarity over optimization

## Technology Stack
- Python 3.13+
- UV for environment management
- Spec-Kit Plus for spec-driven development

## Setup and Installation

1. Ensure Python 3.13+ is installed on your system
2. Install UV for environment management
3. Clone the repository
4. Navigate to the project directory
5. Run the application from the src directory

## Features
- Add a todo (title + description)
- View all todos with status (completed / incomplete)
- Update an existing todo
- Delete a todo by ID
- Mark a todo as complete or incomplete

## Project Structure
```
├── src/                    # Python source code
├── specs/                  # Specification files
├── .specify/              # Spec-Kit Plus configuration
│   ├── memory/            # Project memory (constitution, etc.)
│   ├── templates/         # Template files
│   └── scripts/           # Utility scripts
└── README.md             # This file
```

## Non-Goals
- No GUI implementation
- No web framework usage
- No database integration
- No authentication system
- No external API connections
- No file persistence mechanisms"# cli-todo-app" 
