# todo-cli-app Reading Notes

## What this project does

This project is a command-line todo list app. It lets users add, list, delete, complete, search, and clear tasks.

## Project structure

- `todo.py`: all program logic
- `tasks.json`: stores task data
- `README.md`: explains the project

## Important ideas

### JSON storage

The project uses `load_tasks()` to read tasks from `tasks.json` and `save_tasks()` to write tasks back to the file.

### Command-based interface

The program reads user input, splits it into words, and uses the first word as the command.

### Task representation

Each task is stored as a dictionary with description, done status, and priority.

## What I can learn from it

- How to use JSON for persistent storage
- How to design a simple CLI command system
- How to split program features into functions
- How to handle invalid user input

## What I might apply to Music Queue

- Save songs to a JSON file
- Load the queue when the program starts
- Add command-style interaction as an alternative to menu numbers