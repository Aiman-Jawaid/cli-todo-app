---
id: 4
title: todo-cli-tasks
stage: tasks
date: 2026-01-01
surface: agent
model: Claude Sonnet 4.5
feature: 1-todo-cli-app
branch: 1-todo-cli-app
user: user
command: sp.tasks
labels: [tasks, todo, cli, implementation]
links:
  spec: specs/1-todo-cli-app/spec.md
  plan: specs/1-todo-cli-app/plan.md
  adr: null
  pr: null
files:
  - specs/1-todo-cli-app/tasks.md
tests:
  - none
---

## Prompt

$ARGUMENTS

## Response snapshot

---
description: "Task list for In-Memory Todo CLI Application (Phase I)"
---

# Tasks: In-Memory Todo CLI Application (Phase I)

**Input**: Design documents from `/specs/1-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 [P] Create models directory in src/models/
- [ ] T003 [P] Create services directory in src/services/
- [ ] T004 [P] Create cli directory in src/cli/
- [ ] T005 [P] Create lib directory in src/lib/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Create Todo model class with ID, Title, Description, Status attributes in src/models/todo.py
- [ ] T007 [P] Implement in-memory storage using dictionary in src/models/todo.py
- [ ] T008 [P] Implement auto-incrementing ID generation in src/models/todo.py
- [ ] T009 Create TodoService class with basic CRUD operations in src/services/todo_service.py
- [ ] T010 [P] Implement validation logic for Title (required, 1-200 chars) and Description (0-1000 chars) in src/services/todo_service.py
- [ ] T011 [P] Implement error handling for invalid operations in src/services/todo_service.py
- [ ] T012 Create utility functions for input validation and formatting in src/lib/utils.py
- [ ] T013 [P] Implement CLI menu structure with main loop in src/cli/main.py
- [ ] T014 [P] Add graceful error handling to CLI interface in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todos with title and optional description

**Independent Test**: Can be fully tested by launching the application, selecting the "Add Todo" option, entering a title and description, and verifying that the new todo appears in the list of todos.

### Implementation for User Story 1

- [ ] T015 [P] [US1] Implement add_todo method in TodoService to create new todos in src/services/todo_service.py
- [ ] T016 [US1] Add input validation for new todo creation in src/services/todo_service.py
- [ ] T017 [US1] Implement CLI menu option for adding todos in src/cli/main.py
- [ ] T018 [US1] Add user prompts for title and description input in src/cli/main.py
- [ ] T019 [US1] Connect CLI add todo functionality to TodoService in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Allow users to see all their todos with their current status (complete/incomplete)

**Independent Test**: Can be fully tested by adding some todos to the system and then selecting the "View Todos" option to see the list of all todos with their status.

### Implementation for User Story 2

- [ ] T020 [P] [US2] Implement get_all_todos method in TodoService to retrieve all todos in src/services/todo_service.py
- [ ] T021 [US2] Implement CLI menu option for viewing todos in src/cli/main.py
- [ ] T022 [US2] Format and display todos with ID, Title, Description, and Status in src/cli/main.py
- [ ] T023 [US2] Handle empty todo list case with appropriate message in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Complete/Incomplete (Priority: P2)

**Goal**: Allow users to update the status of a todo to indicate whether it has been completed or not

**Independent Test**: Can be fully tested by adding a todo, viewing the todo list, selecting the "Mark Todo Complete" option, and verifying that the todo's status has changed.

### Implementation for User Story 3

- [ ] T024 [P] [US3] Implement update_todo_status method in TodoService to change completion status in src/services/todo_service.py
- [ ] T025 [US3] Add validation for todo ID existence in src/services/todo_service.py
- [ ] T026 [US3] Implement CLI menu option for marking todos complete/incomplete in src/cli/main.py
- [ ] T027 [US3] Add user prompts for selecting todo and new status in src/cli/main.py
- [ ] T028 [US3] Connect CLI mark todo functionality to TodoService in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo (Priority: P3)

**Goal**: Allow users to modify an existing todo's title or description if they need to change the details of a task

**Independent Test**: Can be fully tested by adding a todo, selecting the "Update Todo" option, choosing a todo, modifying its title or description, and verifying the changes are saved.

### Implementation for User Story 4

- [ ] T029 [P] [US4] Implement update_todo method in TodoService to modify existing todo in src/services/todo_service.py
- [ ] T030 [US4] Add validation for updating todo attributes in src/services/todo_service.py
- [ ] T031 [US4] Implement CLI menu option for updating todos in src/cli/main.py
- [ ] T032 [US4] Add user prompts for selecting todo and new values in src/cli/main.py
- [ ] T033 [US4] Connect CLI update todo functionality to TodoService in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Allow users to remove a todo from their list when it's no longer needed

**Independent Test**: Can be fully tested by adding a todo, selecting the "Delete Todo" option, choosing a todo, and verifying that it's no longer in the list.

### Implementation for User Story 5

- [ ] T034 [P] [US5] Implement delete_todo method in TodoService to remove todos by ID in src/services/todo_service.py
- [ ] T035 [US5] Add validation for confirming todo deletion in src/services/todo_service.py
- [ ] T036 [US5] Implement CLI menu option for deleting todos in src/cli/main.py
- [ ] T037 [US5] Add user prompts for selecting todo and confirmation in src/cli/main.py
- [ ] T038 [US5] Connect CLI delete todo functionality to TodoService in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T039 [P] Add comprehensive error handling throughout the application
- [ ] T040 [P] Improve user interface formatting and messaging
- [ ] T041 [P] Add input validation for all user inputs
- [ ] T042 [P] Implement graceful application exit functionality
- [ ] T043 [P] Add logging for debugging purposes
- [ ] T044 [P] Run quickstart validation to ensure all functionality works together
- [ ] T045 [P] Perform final code review and cleanup

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Implement add_todo method in TodoService to create new todos in src/services/todo_service.py"
Task: "Add user prompts for title and description input in src/cli/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

## Outcome

- ✅ Impact: Created comprehensive task list with 45 specific tasks organized by user story
- 🧪 Tests: none
- 📁 Files: 1 file created (specs/1-todo-cli-app/tasks.md)
- 🔁 Next prompts: Begin implementation with the tasks
- 🧠 Reflection: Tasks are organized by priority and user story to enable independent development

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): All tasks follow the required format with checkboxes, IDs, and file paths
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of the foundational tasks