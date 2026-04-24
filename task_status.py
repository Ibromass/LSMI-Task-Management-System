from datetime import timedelta
from task_utils import parse_datetime, get_current_datetime, format_datetime
import winsound

def play_alert():
    # Windows notification beep
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    print("🔔 ALERT: Task deadline reached!")

def mark_completed(tasks, idx):
    if 0 <= idx < len(tasks):
        curr = tasks[idx]["status"]
        # Toggle status
        tasks[idx]["status"] = "DONE" if curr == "PENDING" else "PENDING"
        return True
    return False

def is_overdue(t):
    if t["status"] == "DONE": return False
    
    dl = parse_datetime(t["deadline"])
    if not dl: return False
    
    return dl < get_current_datetime()

def is_due_soon(t, mins=30):
    if t["status"] == "DONE": return False
    
    dl = parse_datetime(t["deadline"])
    if not dl: return False
    
    diff = dl - get_current_datetime()
    # Check if it's within the window or already late
    return timedelta(0) < diff <= timedelta(minutes=mins) or dl < get_current_datetime()

def get_overdue_tasks(tasks):
    return [t for t in tasks if is_overdue(t)]

def check_alerts(tasks):
    alerts = []
    now = get_current_datetime()
    
    for t in tasks:
        if t["status"] == "DONE": continue
            
        dl = parse_datetime(t["deadline"])
        if not dl: continue
            
        if dl < now:
            play_alert()
            alerts.append(f"⚠️  OVERDUE: {t['title']} ({format_datetime(dl)})")
        elif (dl - now).total_seconds() <= 1800: # 30 mins
            play_alert()
            alerts.append(f"⏰ DUE SOON: {t['title']} ({format_datetime(dl)})")
    
    return alerts
