from task_manager.service import TaskManager
manager = TaskManager()


def add_task():
    try:
        task = input('Enter the task you want to add: ')
        priority = int(input('Enter the priority you want to assign: '))
        category = input("Enter the category of the current task: ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        task_added = manager.add_task(task, priority , category , due_date)

        print(
            f"\nTask added successfully\n"
            f"Task ID: {task_added['task_id']}\n"
            f"Task: {task_added['task']}\n"
            f"Priority: {task_added['priority']}\n"
            f"Category: {task_added['category']}\n"
            f"Due Date: {task_added['due_date']}\n"
            f"Completed: {task_added['completed']}\n"
            f"Created_at: {task_added['created_at']}\n"
            f"Updated_at: {task_added['updated_at']}\n"
        )
    except ValueError as e:
        print(f"Error: {e}")


def list_tasks():
    tasks = manager.list_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nListing all tasks:\n")

    for sno, task_id, details in tasks:
        print(
            f"{sno}. "
            f"Task ID: {task_id} | "
            f"Task: {details['task']} | "
            f"Priority: {details['priority']} | "
            f"Category: {details['category']} |"
            f"Due Date: {details['due_date']} |"
            f"Completed: {details['completed']} |"
            f"Created_at: {details['created_at']} |"
            f"Updated_at: {details['updated_at']}"
        )


def delete_task():
    try:
        list_tasks()
        sno = int(input('\nEnter the serial number of the task to delete: '))
        deleted_task = manager.delete_task(sno)

        print("\nTask deleted successfully")
        print(f"Task: {deleted_task['task']}")
        print(f"Priority: {deleted_task['priority']}")
        print(f"Category: {deleted_task['category']}")
        print(f"Due Date: {deleted_task['due_date']}")
        print(f"Completed: {deleted_task['completed']}")
        print(f"Created_at: {deleted_task['created_at']}")
        print(f"Updated_at: {deleted_task['updated_at']}")

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

        updated_task = manager.edit_task(sno, new_task, new_priority , new_category  ,new_due_date)

        print("\nTask updated successfully")
        print(f"Task: {updated_task['task']}")
        print(f"Priority: {updated_task['priority']}")
        print(f"Category: {updated_task['category']}")
        print(f"Due Date: {updated_task['due_date']}")
        print(f"Completed: {updated_task['completed']}")
        print(f"Created_at: {updated_task['created_at']}")
        print(f"Updated_at: {updated_task['updated_at']}")

    except ValueError as e:
        print(f"Error: {e}")


def mark_task_complete():
    try:
        list_tasks()
        sno = int(input("\nEnter the serial number of task you want to mark complete: "))

        completed_task = manager.mark_task_complete(sno)

        print("\nTask marked as completed successfully")
        print(f"Task: {completed_task['task']}")
        print(f"Priority: {completed_task['priority']}")
        print(f"Category: {completed_task['category']}")
        print(f"Due Date: {completed_task['due_date']}")
        print(f"Completed: {completed_task['completed']}")
        print(f"Created_at: {completed_task['created_at']}")
        print(f"Updated_at: {completed_task['updated_at']}")

    except ValueError as e:
        print(f"Error: {e}")

def filter_task_by_completion():
    status = input("Enter either 'completed' or 'pending': ").strip().lower()

    try:
        filtered_task = manager.filter_by_completion_status(status)
        if not filtered_task:
            print(f"\nNo {status} tasks found.")
            return

        for sno ,task_id , details in filtered_task:
            print(
            f"{sno}. "
            f"Task ID: {task_id} | "
            f"Task: {details['task']} | "
            f"Priority: {details['priority']} | "
            f"Category: {details['category']} |"
            f"Due Date: {details['due_date']} |"
            f"Completed: {details['completed']} |"
            f"Created_at: {details['created_at']} |"
            f"Updated_at: {details['updated_at']}"
        )
    except ValueError as e:
        print(f"Error : {e}")


