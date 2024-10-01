import pytest

import json
import os
from task_cli import add_task, load_tasks, delete_task, mark_task, update_task


'''
    Ensure the reset_tasks function is executed before each test run to clear the tasks.json file,
    maintaining a clean testing environmen
'''
@pytest.fixture(autouse=True)
def reset_tasks():
  
    if os.path.exists('tasks.json'):
        os.remove('tasks.json')


def test_add_task():
    add_task("Test task")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]['description'] == "Test task"

def test_update_task():
    add_task("Task to be updated")
    tasks = load_tasks()
    task_id = tasks[0]['id']
    update_task(task_id, "Updated task")
    updated_tasks = load_tasks()
    assert updated_tasks[0]['description'] == "Updated task"

def test_delete_task():
    add_task("Task to be deleted")
    tasks = load_tasks()
    task_id = tasks[0]['id']
    delete_task(task_id)
    assert len(load_tasks()) == 0

def test_mark_task():
    add_task("Task to be marked")
    tasks = load_tasks()
    task_id = tasks[0]['id']
    mark_task(task_id, 'done')
    assert load_tasks()[0]['status'] == 'done'
