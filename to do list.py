tasks = []
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = " CORRECT " if task[1] else " WRONG "
            print(f"{i}. {task[0]} [{status}]")
def add_task():
    task = input("Enter new task: ")
    tasks.append([task, False])
    print(" Task added.")
def mark_done():
    show_tasks()
    number = int(input("Enter task number to mark as done: "))
    if 1 <= number <= len(tasks):
        tasks[number - 1][1] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")
def delete_task():
    show_tasks()
    number = int(input("Enter task number to delete: "))
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Deleted task: {removed[0]}")
    else:
        print("Invalid task number.")
def main():
    while True:
        print("   TO-DO LIST MENU  ")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("THANK YOU!")
            break
        else:
            print("Invalid choice. Try again.")
main()
