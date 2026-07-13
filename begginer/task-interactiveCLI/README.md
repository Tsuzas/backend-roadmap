# Task Tracker CLI

A simple interactive command-line task manager built with Python.

This project allows you to create, edit, update, view, and delete tasks. All tasks are stored locally in a JSON file.

## Features

- Add new tasks
- View all tasks
- Edit task title and description
- Update task status
- Delete tasks
- Automatically creates the `tasks.json` file if it doesn't exist
- Saves data between program runs

## Requirements

- Python 3.10+
- InquirerPy

Install the dependency:

```bash
pip install InquirerPy
```

## Project Structure

```
task-interactiveCLI/
│
├── task-interactiveCLI.py
├── tasks.json
└── README.md
```

## Running the Project

Run the program with:

```bash
python task-interactiveCLI.py
```

or

```bash
python3 task-interactiveCLI.py
```

## Task Format

Tasks are stored as JSON objects.

Example:

```json
{
    "id": 1,
    "title": "Finish roadmap project",
    "description": "Complete Task Tracker CLI",
    "status": "todo",
    "createdAt": "2026-07-13 15:30:21",
    "updatedAt": "2026-07-13 15:30:21"
}
```

## Technologies

- Python
- JSON
- InquirerPy
- datetime
- os

## Notes

This project was made as practice while following the Backend Roadmap from roadmap.sh and focuses on learning:

- File handling
- JSON serialization
- Functions
- Match statements
- Basic CLI application design