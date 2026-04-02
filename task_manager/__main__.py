from task_manager.service import TaskManager

manager = TaskManager()


def print_single_task(details, task_id=None, sno=None):
    prefix = f"{sno}. " if sno is not None else ""
    task_id_text = f"Task ID: {task_id} | " if task_id is not None else ""

    print(
        f"{prefix}"
        f"{task_id_text}"
        f"Task: {details['task']} | "
        f"Priority: {details['priority']} | "
        f"Category: {details['category']} | "
        f"Due Date: {details['due_date']} | "
        f"Completed: {details['completed']} | "
        f"Created_at: {details['created_at']} | "
        f"Updated_at: {details['updated_at']}"
    )


def print_task_list(tasks):
    for sno, task_id, details in tasks:
        print_single_task(details, task_id, sno)


def add_task():
    try:
        task = input("Enter the task you want to add: ")
        priority = int(input("Enter the priority you want to assign: "))
        category = input("Enter the category of the current task: ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")

        task_added = manager.add_task(task, priority, category, due_date)

        print("\nTask added successfully")
        print_single_task(task_added, task_added["task_id"])

    except ValueError as e:
        print(f"Error: {e}")


def list_tasks():
    tasks = manager.list_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nListing all tasks:\n")
    print_task_list(tasks)


def delete_task():
    try:
        list_tasks()
        sno = int(input("\nEnter the serial number of the task to delete: "))
        deleted_task = manager.delete_task(sno)

        print("\nTask deleted successfully")
        print_single_task(deleted_task)

    except ValueError as e:
        print(f"Error: {e}")


def edit_task():
    try:
        list_tasks()
        sno = int(input("\nEnter the serial number of the task to edit: "))

        new_task = input("Enter new task (leave blank to keep same): ").strip()
        new_priority = input("Enter new priority (leave blank to keep same): ").strip()
        new_category = input("Enter new category (leave blank to keep same): ").strip()
        new_due_date = input("Enter new due date (leave blank to keep same): ").strip()

        new_task = new_task if new_task else None
        new_priority = int(new_priority) if new_priority else None
        new_category = new_category if new_category else None
        new_due_date = new_due_date if new_due_date else None

        updated_task = manager.edit_task(
            sno,
            new_task,
            new_priority,
            new_category,
            new_due_date
        )

        print("\nTask updated successfully")
        print_single_task(updated_task)

    except ValueError as e:
        print(f"Error: {e}")


def mark_task_complete():
    try:
        list_tasks()
        sno = int(input("\nEnter the serial number of task you want to mark complete: "))
        completed_task = manager.mark_task_complete(sno)

        print("\nTask marked as completed successfully")
        print_single_task(completed_task)

    except ValueError as e:
        print(f"Error: {e}")


def filter_task_by_completion():
    status = input("Enter either 'completed' or 'pending': ").strip().lower()

    try:
        filtered_task = manager.filter_by_completion_status(status)

        if not filtered_task:
            print(f"\nNo {status} tasks found.")
            return

        print(f"\n{status.capitalize()} tasks:\n")
        print_task_list(filtered_task)

    except ValueError as e:
        print(f"Error: {e}")


def sort_tasks_by_due_date():
    tasks = manager.sort_tasks_by_due_date()

    if not tasks:
        print("\nNo task available")
        return

    print("\nTasks sorted by due date:\n")
    print_task_list(tasks)


def filter_overdue_tasks():
    tasks = manager.filter_overdue_tasks()

    if not tasks:
        print("\nNo overdue tasks available")
        return

    print("\nOverdue tasks:\n")
    print_task_list(tasks)


def filter_task_due_today():
    tasks = manager.filter_task_due_today()

    if not tasks:
        print("\nNo tasks due today")
        return

    print("\nTasks due today:\n")
    print_task_list(tasks)


def search_task():
    try:
        keyword = input("Enter the keyword that you want to search: ")
        tasks = manager.search_tasks(keyword)
        if not tasks:
            print("\nNo matching tasks found")
            return 
        print(f"\nSearch result for '{keyword}':\n")
        print_task_list(tasks)
    except ValueError as e:
        print(f"Error: {e}")