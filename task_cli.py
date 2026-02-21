import os
import sys
import json
from datetime import datetime

tasks = "tasks.json"

# -----------------------------------------
# UTILITY FUNCTIONS
# -----------------------------------------

def load_tasks():
    if not os.path.exists(tasks):
        with open(tasks, 'w') as f:
            json.dump([], f)
            print(f"The file {tasks} has been created")
        return []

    try:
        with open(tasks, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print('Error: tasks.json is corrupted.')
        sys.exit(1)


def save_task(task):
    with open(tasks, 'w') as f:
        json.dump(task, f, indent=4)


def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def current_timestamp():
    return datetime.now().isoformat()


# -----------------------------------------
# CORE FUNCTIONS
# -----------------------------------------

def list_tasks(filter_status=None):
    tasks = load_tasks()

    if filter_status:
        if filter_status not in ["todo", "in-progress", "done"]:
            print("Invalid status filter.")
            return
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(
            f"[{task['id']}] {task['description']}"
            f" (Status: {task['status']})"
            f" Created: {task['createdAt']}"
            f" Updated: {task['updatedAt']}"
        )


def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)

    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": current_timestamp(),
        "updatedAt": current_timestamp()
    }

    tasks.append(task)
    save_task(tasks)
    print(f"Task added successfully (ID: {task["id"]})")

def update_task(task_id, new_description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = current_timestamp()
            save_task(tasks)
            print("Task updated successfully.")
            return

    print("Error: Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_task = [task for task in tasks if task['id'] != int(task_id)]

    if len(updated_task) < len(tasks):
        save_task(updated_task)
        print(f"(ID: {task_id}) was deleted successfully")
    else:
        print("Task not found")


def change_status(task_id, status):
    if status not in ["todo", "in-progress", "done"]:
        print("Invalid status.")
        return
    
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = current_timestamp()
            save_task(tasks)

    print(f"Task ID: {task_id} status was changed to {status}")



# -----------------------------------------
# Command line arguments
# -----------------------------------------
def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(" Add: add 'description'")
        print(" Update: update <task id> 'changed description'")
        print(" Delete: delete <task id>")
        print(" Change status: mark-in-progress / mark-done <task id>")
        print(" List: list / list todo / list in-progress / list done")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            description = sys.argv[2]
            add_task(description)

        elif command == "update":
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)

        elif command == "delete":
            task_id = int(sys.argv[2])
            delete_task(task_id)

        elif command == "list":
            if len(sys.argv) == 3:
                filter_status = sys.argv[2]
                list_tasks(filter_status)
            else:
                list_tasks()

        elif command == "mark-in-progress":
            task_id = int(sys.argv[2])
            change_status(task_id, "in-progress")

        elif command == "mark-done":
            task_id = int(sys.argv[2])
            change_status(task_id, "done")

        else:
            print("Unknown Command.")

    except IndexError:
        print("Error: Missing arguments")
    except ValueError:
        print("Error: Task ID must be an integer")

if __name__ == "__main__":
    main()
