from datetime import datetime

def get_current_datetime():
    return datetime.now()

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M")

def parse_datetime(d_str):
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(d_str, fmt)
            if fmt == "%Y-%m-%d":
                dt = dt.replace(hour=23, minute=59)
            return dt
        except ValueError:
            continue
    return None

def format_task_line(name, due, is_done):
    status = "DONE" if is_done else "PENDING"
    return f"{name}|{due}|{status}\n"

def parse_task_line(line):
    p = line.strip().split("|")
    return {
        "title": p[0],
        "deadline": p[1],
        "status": p[2]
    }
