from task_operations import load_tasks, save_tasks, add_task, delete_task
from task_status import mark_completed, is_overdue, check_alerts
from task_utils import parse_datetime, format_datetime, get_current_datetime

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print(f"\n---Your Task List ({len(tasks)}) ---")
    for i, t in enumerate(tasks):
        dt = parse_datetime(t["deadline"])
        if dt:
            due_str = format_datetime(dt)
        else:
           due_str = t["deadline"]

        if t["status"] == "DONE":
            icon, status_label = "✅", "DONE"
        elif is_overdue(t):
            icon, status_label = "🔴", "OVERDUE"
        else:
            icon, status_label = "⏳", "PENDING"
            
        print(f"{icon} {i+1}. [{status_label}] {t['title']} (Due: {due_str})")

def main():
    tasks = load_tasks()
    alerts = check_alerts(tasks)
    if alerts:
        print("\n--- URGENT ALERTS ---")
        for a in alerts: 
            print(a)

    while True:
        print("\nWELCOME TO SMART STUDENT TASK MANAGEMENT SYSTEM")
        print("\n1. Add a Task | 2. View Tasks | 3. Update Task Status | 4. Delete Task | 5. Exit")
        choice = input("Select: ").strip()

        if choice == "1":
            name = input("Task Title: ").strip()
            date = input("Due Date (YYYY-MM-DD HH:MM AM/PM): ").strip()

            if parse_datetime(date):
                add_task(name, date)
                tasks = load_tasks() 
                print("Task added successfully.")
            else: 
                print("Invalid date format. Use YYYY-MM-DD HH:MM")
                
        elif choice == "2":
            display_tasks(tasks)
            
        elif choice == "3":
            display_tasks(tasks)
            if not tasks: continue
            try:
                idx = int(input("Enter task number to mark as done: ")) - 1
                if mark_completed(tasks, idx): 
                    save_tasks(tasks)
                    print("Task status updated successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "4":
            display_tasks(tasks)
            if not tasks: continue
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                if delete_task(tasks, idx): 
                    tasks = load_tasks() 
                    print("Task deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "5":
            print("Exiting Student Task Manager. Goodbye!")
            break
        else:
            print("Unknown selection. Please choose 1-5.")

if __name__ == "__main__":
    main()
