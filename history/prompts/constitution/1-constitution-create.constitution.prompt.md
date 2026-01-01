---
id: 1
title: constitution-create
stage: constitution
date: 2026-01-01
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: sp.constitution
labels: [constitution, setup, initial]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - README.md
tests:
  - none
---

## Prompt

You are a senior software architect and spec-driven development expert.

Your task is to generate a Constitution file for a project using Spec-Kit Plus.

Project Title:
The Evolution of Todo – Phase I: In-Memory Python Console App

Project Theme:
From simple CLI scripts to future cloud-native, distributed AI systems.

Project Purpose:
This project is designed for students to act as Product Architects.
They will build software progressively using AI and specifications instead of writing boilerplate code.

Phase Scope:
Phase I focuses ONLY on a simple in-memory command-line Todo application written in Python.

Technology Stack:
- Python 3.13+
- UV for environment management
- Spec-Kit Plus for spec-driven development

Core Principles to Include in the Constitution:
1. Spec-Driven Development
   - All features must be defined in specifications before implementation
   - No code should be written without an approved spec
   - Specs act as the single source of truth

2. Clean Architecture & Code Quality
   - Clear separation of concerns
   - Readable, maintainable, beginner-friendly Python code
   - No unnecessary complexity
   - Follow basic clean code principles

3. In-Memory Data Only
   - No database or file persistence
   - All todos exist only during program runtime
   - Data resets when the program restarts

4. Required Features (Must Be Enforced)
   - Add a todo (title + description)
   - View all todos with status (completed / incomplete)
   - Update an existing todo
   - Delete a todo by ID
   - Mark a todo as complete or incomplete

5. CLI-First Design
   - Text-based menu system
   - Clear prompts and user-friendly messages
   - Graceful handling of invalid input

6. Educational Focus
   - Designed for learning and demonstration
   - Prioritize clarity over optimization
   - Code should be easy to understand for students

7. Project Structure Rules
   - /src folder for Python source code
   - specs history folder for all specification files
   - Constitution file must guide all development decisions
   - README.md required with setup and run instructions

8. Non-Goals (Explicitly Mention)
   - No GUI
   - No web framework
   - No database
   - No authentication
   - No external APIs

Output Requirements:
- Produce a well-structured `constitution.md`
- Use clear headings and bullet points
- Write in simple, professional language
- Make it strict enough to guide AI agents and students consistently

The output should ONLY be the content of the Constitution file.

## Response snapshot

# The Evolution of Todo – Phase I: In-Memory Python Console App Constitution

## Core Principles

### I. Spec-Driven Development
All features must be defined in specifications before implementation; no code should be written without an approved spec; specs act as the single source of truth for all development decisions.

### II. Clean Architecture & Code Quality
Clear separation of concerns; readable, maintainable, beginner-friendly Python code; no unnecessary complexity; follow basic clean code principles with emphasis on educational clarity.

### III. In-Memory Data Only
No database or file persistence; all todos exist only during program runtime; data resets when the program restarts; all data operations are performed in memory only.

### IV. Required Features Implementation
Must implement: Add a todo (title + description), View all todos with status (completed/incomplete), Update an existing todo, Delete a todo by ID, Mark a todo as complete or incomplete.

### V. CLI-First Design
Text-based menu system; clear prompts and user-friendly messages; graceful handling of invalid input; prioritize console interaction over any other interface patterns.

### VI. Educational Focus
Designed for learning and demonstration; prioritize clarity over optimization; code should be easy to understand for students; educational value takes precedence over performance optimizations.

## Project Structure Rules

- /src folder for Python source code
- specs folder for all specification files
- Constitution file must guide all development decisions
- README.md required with setup and run instructions
- Follow consistent naming and organization patterns for maintainability

## Non-Goals

- No GUI implementation
- No web framework usage
- No database integration
- No authentication system
- No external API connections
- No file persistence mechanisms

## Governance

This Constitution serves as the governing document for all development decisions in this project. All code, specifications, and development activities must comply with these principles. Amendments to this Constitution require explicit approval and must be documented with clear rationale. Development workflow must follow the spec-driven approach outlined in this document, with all features requiring specification before implementation.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01

## Outcome

- ✅ Impact: Created project constitution and README files that establish governance and principles
- 🧪 Tests: none
- 📁 Files: 2 files created (.specify/memory/constitution.md, README.md)
- 🔁 Next prompts: Implement the required todo features following the constitution
- 🧠 Reflection: Constitution provides clear guidance for future development

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing the todo application features