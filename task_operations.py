from task_utils import format_task_line, parse_task_line

DB_FILE = "task.txt"

def load_tasks():
    tasks = []
    try:
        with open(DB_FILE, "r") as f:
            for line in f:
                if line.strip():
                    tasks.append(parse_task_line(line))
    except FileNotFoundError:
        return [] # Just return empty if file isn't there
    return tasks

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        for t in tasks:
            # Pass title, deadline, and a simple boolean for status
            f.write(format_task_line(t["title"], t["deadline"], t["status"] == "DONE"))

def add_task(title, deadline):
    # Appending is faster than rewriting the whole file
    with open(DB_FILE, "a") as f:
        f.write(format_task_line(title, deadline, False))

def delete_task(tasks, idx):
    if idx < 0 or idx >= len(tasks):
        return False
    
    tasks.pop(idx)
    save_tasks(tasks)
    return True
