import os
import json

PRIORITIES = ("low", "medium", "high")

def print_tasks(tasks, filter_priority=None):
    print("\nTasks:")
    found = False
    for idx, task in enumerate(tasks, start=1):  # 1-based indices for display
        if filter_priority and task["priority"] != filter_priority:
            continue
        status = "Done" if task["done"] else "Not done"
        print(f"[{idx}] {task['title']} (Priority: {task['priority']}) - {status}")
        found = True
    if not found:
        print("No tasks to show.")
    print()

def get_priority():
    while True:
        priority = input(f"Enter priority ({'/'.join(PRIORITIES)}): ").strip().lower()
        if priority in PRIORITIES:
            return priority
        print(f"Invalid priority. Please enter one of: {', '.join(PRIORITIES)}.")

def get_index(tasks, prompt):
    while True:
        try:
            shown = int(input(prompt))
            idx = shown - 1   # convert 1-based input to 0-based index
            if 0 <= idx < len(tasks):
                return idx
            print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def main():
    tasks = load_tasks()

    while True:
        print("Menu:")
        print("[1] Add task")
        print("[2] List tasks")
        print("[3] Toggle task done/not done")
        print("[4] Delete task")
        print("[5] Filter by priority")
        print("[0] Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            if not title:
                print("Title cannot be empty.\n")
                continue
            priority = get_priority()
            tasks.append({"title": title, "priority": priority, "done": False})
            print("Task added.\n")

        elif choice == "2":
            print_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("No tasks to update.\n")
                continue
            print_tasks(tasks)
            idx = get_index(tasks, "Enter task number to toggle: ")
            tasks[idx]["done"] = not tasks[idx]["done"]
            print(f"Task updated: {tasks[idx]['title']} is now {'done' if tasks[idx]['done'] else 'not done'}.\n")

        elif choice == "4":
            if not tasks:
                print("No tasks to delete.\n")
                continue
            print_tasks(tasks)
            idx = get_index(tasks, "Enter task number to delete: ")
            deleted = tasks.pop(idx)
            print(f"Task deleted: {deleted['title']}\n")

        elif choice == "5":
            priority = get_priority()
            print_tasks(tasks, filter_priority=priority)

        elif choice == "0":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
# ToDoListv2/todolist v2.py
# This is a simple To-Do List application that allows users to manage tasks with priorities.    