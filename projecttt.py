import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")
    task = {"description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def mark_task_complete(tasks):
    task_index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def view_tasks(tasks):
    print("To-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Completed: {'Yes' if task['completed'] else 'No'}")

def delete_task(tasks):
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Manager")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_complete(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using To-Do List Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
