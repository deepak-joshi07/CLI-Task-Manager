from task_manager.service import TaskManager
from .validator import valid_options

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


def get_all_tasks():
    return manager.list_tasks()


def get_search_tasks():
    keyword = input("Enter the keyword that you want to search: ")
    return manager.search_tasks(keyword)


def select_options():
    option = int(input(
        "Do you want to:\n"
        "1. Search the task\n"
        "2. List all tasks\n"
        "Select either 1 or 2: "
    ))
    return option


def show_task_list(tasks, title="Tasks"):
    if not tasks:
        print("\nNo tasks found.")
        return

    print(f"\n{title}:\n")
    print_task_list(tasks)


def choose_task_source():
    option = select_options()
    valid_options(option)

    if option == 1:
        tasks = get_search_tasks()
        title = "Search Results"
    else:
        tasks = get_all_tasks()
        title = "All Tasks"

    return tasks, title


def delete_task():
    try:
        tasks, title = choose_task_source()

        if not tasks:
            print("\nNo matching tasks found.")
            return

        show_task_list(tasks, title)

        sno = int(input("\nEnter the serial number of the task to delete: "))
        deleted_task = manager.delete_task_by_list(tasks, sno)

        print("\nTask deleted successfully")
        print_single_task(deleted_task)

    except ValueError as e:
        print(f"Error: {e}")


def get_edit_input():
    new_task = input("Enter new task (leave blank to keep same): ").strip()
    new_priority = input("Enter new priority (leave blank to keep same): ").strip()
    new_category = input("Enter new category (leave blank to keep same): ").strip()
    new_due_date = input("Enter new due date (leave blank to keep same): ").strip()

    new_task = new_task if new_task else None
    new_priority = int(new_priority) if new_priority else None
    new_category = new_category if new_category else None
    new_due_date = new_due_date if new_due_date else None

    return new_task, new_priority, new_category, new_due_date


def edit_task():
    try:
        tasks, title = choose_task_source()

        if not tasks:
            print("\nNo matching tasks found.")
            return

        show_task_list(tasks, title)
        sno = int(input("\nEnter the serial number of the task to edit: "))

        new_task, new_priority, new_category, new_due_date = get_edit_input()

        if all(value is None for value in [new_task, new_priority, new_category, new_due_date]):
            print("\nNo changes provided.")
            return

        updated_task = manager.edit_task_by_list(
            tasks,
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
        tasks, title = choose_task_source()

        if not tasks:
            print("\nNo matching tasks found.")
            return

        show_task_list(tasks, title)

        sno = int(input("\nEnter the serial number of task you want to mark complete: "))
        completed_task = manager.mark_task_complete(tasks, sno)

        print("\nTask marked as completed successfully")
        print_single_task(completed_task)

    except ValueError as e:
        print(f"Error: {e}")