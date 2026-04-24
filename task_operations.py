from task_utils import format_task_line, parse_task_line

DB_FILE = "task.txt"

def load_tasks():
    tasks = []
    try:
        with open(DB_FILE, "r") as f:
            for i, line in enumerate(f):
                if line.strip():
                    t = parse_task_line(line)
                    t["id"] = i + 1 # Assigns ID for display logic
                    tasks.append(t)
    except FileNotFoundError:
        return []
    return tasks

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        for t in tasks:
            f.write(format_task_line(t["title"], t["deadline"], t["status"] == "DONE"))

def add_task(title, deadline):
    with open(DB_FILE, "a") as f:
        f.write(format_task_line(title, deadline, False))

def delete_task(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)
        return True
    return False
