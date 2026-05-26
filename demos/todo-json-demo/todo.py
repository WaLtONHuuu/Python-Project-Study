import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, description, priority="Medium"):
    tasks.append({
        "description": description,
        "done": False,
        "priority": priority
    })
    save_tasks(tasks)
    print(f"Added: {description} (Priority: {priority})")

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            priority = task.get("priority", "Medium")
            print(f"{i}. [{status}] ({priority}) {task['description']}")

def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['description']}")
    except IndexError:
        print("Invalid task number.")

def mark_done(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")

def search_tasks(tasks, keyword):
    results = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if not results:
        print("No matching tasks found.")
    else:
        print("\nSearch Results:")
        for i, task in enumerate(results):
            status = "✓" if task["done"] else "✗"
            priority = task.get("priority", "Medium")
            print(f"[{status}] ({priority}) {task['description']}")

def clear_completed(tasks):
    tasks[:] = [task for task in tasks if not task["done"]]
    save_tasks(tasks)
    print("Cleared all completed tasks.")

def main():
    tasks = load_tasks()
    print("Welcome to CLI Todo App\nCommands:\n add <task> [priority]\n list\n delete <index>\n done <index>"
          "\n search <keyword>\n clear\n exit")
    print("\n Format:\n command--todo task--priority")

    while True:
        command = [part.strip() for part in input("\n> ").strip().split("--") if part.strip()]
        if not command:
            continue

        if command[0].lower() == "add" and len(command) > 1:
            desc = command[1]
            if len(command) > 2:
                priority = command[2].capitalize()
            else:
                priority = "Medium"
            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"
            add_task(tasks, desc, priority)

        elif command[0].lower() == "list":
            list_tasks(tasks)

        elif command[0].lower() == "delete" and len(command) > 1:
            try:
                delete_task(tasks, int(command[1]))
            except ValueError:
                print("Please enter a valid number.")

        elif command[0].lower() == "done" and len(command) > 1:
            try:
                mark_done(tasks, int(command[1]))
            except ValueError:
                print("Please enter a valid number.")

        elif command[0].lower() == "search" and len(command) > 1:
            keyword = command[1]
            search_tasks(tasks, keyword)

        elif command[0].lower() == "clear":
            clear_completed(tasks)

        elif command[0].lower() == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
