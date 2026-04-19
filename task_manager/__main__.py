from task_manager.service import TaskManager
from .validator import valid_options

manager = TaskManager()


def print_single_task(task, sno=None):
    prefix = f"{sno}. " if sno is not None else ""

    print(
        f"{prefix}"
        f"Task ID: {task.task_id} | "
        f"Task: {task.task} | "
        f"Priority: {task.priority} | "
        f"Category: {task.category} | "
        f"Due Date: {task.due_date} | "
        f"Completed: {task.completed} | "
        f"Created At: {task.created_at} | "
        f"Updated At: {task.updated_at}"
    )


def print_task_list(tasks):
    for sno, task in enumerate(tasks, start=1):
        print_single_task(task, sno)


def add_task():
    try:
        task = input("Enter the task you want to add: ")
        priority = int(input("Enter the priority: "))
        category = input("Enter the category: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")

        new_task = manager.add_task(task, priority, category, due_date)

        print("\nTask added successfully:")
        print_single_task(new_task)

    except ValueError as e:
        print(f"Error: {e}")


def get_all_tasks():
    return manager.list_tasks()


def get_search_tasks():
    keyword = input("Enter keyword to search: ")
    return manager.search_tasks(keyword)


def select_options():
    option = int(input(
        "Choose:\n"
        "1. Search tasks\n"
        "2. List all tasks\n"
        "Enter 1 or 2: "
    ))
    valid_options(option)
    return option


def choose_task_source():
    option = select_options()

    if option == 1:
        return get_search_tasks(), "Search Results"
    else:
        return get_all_tasks(), "All Tasks"


def show_task_list(tasks, title="Tasks"):
    if not tasks:
        print("\nNo tasks found.")
        return False

    print(f"\n{title}:\n")
    print_task_list(tasks)
    return True


def get_valid_index(tasks):
    sno = int(input("\nEnter serial number: "))

    if sno < 1 or sno > len(tasks):
        raise ValueError("Invalid serial number")

    return sno - 1


def delete_task():
    try:
        tasks, title = choose_task_source()

        if not show_task_list(tasks, title):
            return

        index = get_valid_index(tasks)
        task = tasks[index]

        deleted_task = manager.delete_task_by_id(task.task_id)

        print("\nTask deleted successfully:")
        print_single_task(deleted_task)

    except ValueError as e:
        print(f"Error: {e}")


def get_edit_input():
    new_task = input("New task (leave blank to skip): ").strip()
    new_priority = input("New priority (leave blank to skip): ").strip()
    new_category = input("New category (leave blank to skip): ").strip()
    new_due_date = input("New due date (leave blank to skip): ").strip()

    return (
        new_task or None,
        int(new_priority) if new_priority else None,
        new_category or None,
        new_due_date or None
    )


def edit_task():
    try:
        tasks, title = choose_task_source()

        if not show_task_list(tasks, title):
            return

        index = get_valid_index(tasks)
        task = tasks[index]

        updates = get_edit_input()

        if all(v is None for v in updates):
            print("\nNo changes provided.")
            return

        updated_task = manager.edit_task_by_id(
            task.task_id,
            *updates
        )

        print("\nTask updated successfully:")
        print_single_task(updated_task)

    except ValueError as e:
        print(f"Error: {e}")


def mark_task_complete():
    try:
        tasks, title = choose_task_source()

        if not show_task_list(tasks, title):
            return

        index = get_valid_index(tasks)
        task = tasks[index]

        completed_task = manager.mark_task_complete_by_id(task.task_id)

        print("\nTask marked as completed:")
        print_single_task(completed_task)

    except ValueError as e:
        print(f"Error: {e}")