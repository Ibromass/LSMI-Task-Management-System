from task_operations import load_tasks, save_tasks, add_task, delete_task
from task_status import mark_completed, is_overdue, get_overdue_tasks, check_alerts
from task_utils import parse_datetime, format_datetime, get_current_datetime

def display_tasks(tasks):
    if not tasks:
        print("\n[!] No tasks on the list.")
        return
    
    print(f"\n--- CURRENT TASKS ({len(tasks)}) ---")
    
    for i, t in enumerate(tasks):
        dt = parse_datetime(t["deadline"])
        due_str = format_datetime(dt) if dt else t["deadline"]
        
        # Determine status and label
        if is_overdue(t):
            icon, label, info = "🔴", "OVERDUE", f"!! WAS DUE: {due_str} !!"
        elif t['status'] == "DONE":
            icon, label, info = "✅", "DONE", ""
        else:
            icon, label = "⏳", "PENDING"
            # Show "TODAY" if dates match
            today = get_current_datetime().date()
            info = f"(Today at {due_str.split()[1]})" if dt and dt.date() == today else f"(Due: {due_str})"
        
        print(f"{icon} {i + 1}. [{label}] {t['title']} {info}")

def main():
    print("--- STUDENT TASK MANAGER ---")
    
    tasks = load_tasks()
    
    # Quick alert check
    alerts = check_alerts(tasks)
    if alerts:
        print("\n⚠️  URGENT:")
        for a in alerts:
            print(f"  - {a}")
    
    while True:
        print("\n1. Add | 2. View | 3. Complete | 4. Delete | 5. Overdue | 6. Exit")
        cmd = input("Select: ").strip()

        if cmd == "1":
            name = input("Enter Task Title: ").strip()
            print("Format: YYYY-MM-DD HH:MM)")
            raw_date = input("Enter due date and time: ").strip()     
            check_dt = parse_datetime(raw_date)
            if not check_dt:
                print("Bad format. Try 2026-04-25.")
                continue
            
            add_task(name, raw_date)
            tasks = load_tasks() # Refresh list
            print("Task saved successfully.")
            
        elif cmd == "2":
            display_tasks(tasks)
            
        elif cmd == "3":
            display_tasks(tasks)
            if not tasks: continue
            try:
                idx = int(input("Enter task number to finish: ")) - 1
                if mark_completed(tasks, idx):
                    save_tasks(tasks)
                    print(f"Done! Status: {tasks[idx]['status']}")
                else:
                    print("Invalid index.")
            except (ValueError, IndexError):
                print("Enter a valid number.")
                
        elif cmd == "4":
            display_tasks(tasks)
            if not tasks: continue
            try:
                idx = int(input("Enter task number to delete: "))
                if delete_task(tasks, idx):
                    tasks = load_tasks() # Sync
                    print("Task deleted successfully.")
            except:
                print("Error deleting task.")
                
        elif cmd == "5":
            late = get_overdue_tasks(tasks)
            if late:
                print("\nLATE TASKS:")
                for l in late:
                    print(f" - {l['title']}")
            else:
                print("\nEverything is on time!")
                
        elif cmd in ("6", "exit", "quit"):
            print("See ya.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
