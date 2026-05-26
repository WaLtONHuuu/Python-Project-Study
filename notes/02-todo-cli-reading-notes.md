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

## Possible Improvement

One possible improvement I noticed is the command input format.

In the original project, the program uses spaces to separate the command, task description, and priority. This can make multi-word task descriptions harder to parse.

For example:

```text
add buy milk
```

In this input, the program may treat the last word, `milk`, as the priority instead of part of the task description.

This could become confusing because the program has to guess whether the last word is part of the task or a priority value.

In my own demo, I tried using `--` as a separator:

```text
add--buy milk--high
```

This makes each part of the command clearer:

```text
command: add
task description: buy milk
priority: high
```

This format is not necessarily the only solution, but it helped me understand how command parsing can be improved.

Another possible format could be:

```text
add "buy milk" --priority high
```

This would be closer to how many real command-line tools handle multi-word input.

From this improvement idea, I learned that user input design is an important part of CLI programs. Even if the program logic works, unclear input format can make the program harder to use.