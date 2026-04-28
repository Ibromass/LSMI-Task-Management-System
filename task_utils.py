from datetime import datetime

def get_current_datetime():
    return datetime.now()

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %I:%M %p")

def parse_datetime(d_str):
    for fmt in ("%Y-%m-%d %I:%M %p", "%Y-%m-%d %H:%M"):
        try:
            dt = datetime.strptime(d_str, fmt)
            return dt
        except ValueError:
            continue
    return None

def format_task_line(name, due, is_done):
    status = "DONE" if is_done else "PENDING"
    return f"{name}|{due}|{status}\n"

def parse_task_line(line):
    p = line.strip().split("|")
    if len(p) < 3: return None 
    return {
        "title": p[0],
        "deadline": p[1],
        "status": p[2],
    }
