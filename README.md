# Task-Tracker
Build a CLI app to track tasks and manage your to-do list. 




## Features

Add, update, and delete tasks
Mark tasks as in-progress or done
List all tasks or filter by status



## Usage

```python task_cli.py <command> [arguments]```





## :clipboard: Examples Command

```
# Add a new task
python task_cli.py add "Buy Apple"

# Update an existing task
python task_cli.py update 1 "Buy salt and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark a task as in-progress
python task_cli.py mark-in-progress 1

# Mark a task as done
python task_cli.py mark-done 1

# List all tasks
python task_cli.py list

# List only completed tasks
python task_cli.py list done
```




## Requirements

- Python 3.9.12
- pytest (for running tests)
