from datetime import timedelta
from task_utils import parse_datetime, get_current_datetime, format_datetime
import winsound

def play_alert():
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

def mark_completed(tasks, idx):
    if 0 <= idx < len(tasks):
        curr = tasks[idx]["status"]
        tasks[idx]["status"] = "DONE" if curr == "PENDING" else "PENDING"
        return True
    return False

def is_overdue(t):
    if t["status"] == "DONE": return False
    dl = parse_datetime(t["deadline"])
    return dl < get_current_datetime() if dl else False

def check_alerts(tasks):
    alerts = []
    now = get_current_datetime()
    for t in tasks:
        if t["status"] == "DONE": continue
        dl = parse_datetime(t["deadline"])
        if not dl: continue
        
        diff = (dl - now).total_seconds()
        if diff < 0:
            play_alert()
            alerts.append(f"⚠️ OVERDUE: {t['title']}")
        elif diff <= 1800:
            play_alert()
            alerts.append(f"⏰ DUE SOON: {t['title']}")
    return alerts
