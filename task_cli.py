import sys
import json
import os
from datetime import datetime

#Define Helper Functions
def load_tasks():
    if not os.path.exists('tasks.json'):
        return []
    with open('tasks.json', 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def get_next_task_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

#Implement Task Management Functions
def add_task(description):
    tasks = load_tasks()
    task_id = get_next_task_id(tasks)
    now = datetime.now().isoformat()
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task {task_id} not found.")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    if tasks:
        for task in tasks:
            created_at = task.get('createdAt', 'N/A')
            updated_at = task.get('updatedAt', 'N/A')
            print(f"""
Task ID: {task['id']}
Description: {task['description']}
Status: {task['status']}
Created At: {created_at}
Updated At: {updated_at}
            """)
    else:
        print("No tasks found.")

#Handle Command-Line Arguments
def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("Please provide a valid command.")
        return

    command = args[0]
    
    if command == 'add' and len(args) == 2:
        add_task(args[1])
    elif command == 'update' and len(args) == 3:
        update_task(int(args[1]), args[2])
    elif command == 'delete' and len(args) == 2:
        delete_task(int(args[1]))
    elif command == 'mark-in-progress' and len(args) == 2:
        mark_task(int(args[1]), 'in-progress')
    elif command == 'mark-done' and len(args) == 2:
        mark_task(int(args[1]), 'done')
    elif command == 'list' and len(args) == 1:
        list_tasks()
    elif command == 'list' and len(args) == 2:
        list_tasks(args[1])
    else:
        print("Invalid command or arguments.")

if __name__ == '__main__':
    main()


