import json
import os

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add task
def add_task(tasks):
    title = input("Enter task title: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['title']} [{status}]")


# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"🗑 Task '{removed['title']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


# Mark task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()