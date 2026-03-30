from task_manager.service import TaskManager

manager = TaskManager()
def add_task():
    try:
        task = input('Enter the task you want to add : ')
        priority = int(input('Enter the priority that you want to add : '))
        task_added = manager.add_task(task , priority)

        print( 
        f"Task added successfully\n"
        f"Task ID: {task_added['task_id']}\n"
        f"Task: {task_added['task']}\n"
        f"Priority: {task_added['priority']}")
    except ValueError as e: 
        print(f"Error : {e}")


def list_tasks():
    tasks = manager.list_task()

    if not tasks: 
        print("\nNo tasks available.")
        return 
    
    print("\nListing all the added task : ")

    for sno ,task_id ,  details in tasks:
        print(f"{sno}. Task_id : {details['task_id']} , Task : {details['task']} , Priority : {details['priority']}")

def delete_task():
    try:
        list_tasks()
        sno = int(input('\nEnter the serial number of the number of the task to delete: '))
        delete_task = manager.delete_task(sno)
        print(f'\nSucessfully deleted the task with id ')
        print(f"Task : {delete_task['task']}")
        print(f"Priority : {delete_task['priority']}")

    except ValueError as e : 
        print(f'Error: {e}')


def edit_task():
    try: 
        list_tasks() 
        sno = int(input("\nEnter the serial number of the task to edit: "))

        new_task = input("Enter new task (leave blank to keep same): ").strip()
        new_priority = input("Enter new priority (leave blank to keep same): ").strip()

        new_task = new_task if new_task else None
        new_priority = int(new_priority) if new_priority else None

        update_task = manager.edit_task(sno , new_task , new_priority)

        print("\nTask updated successfully")
        print(f"Task :{update_task['task']}")
        print(f"Priority :{update_task['priority']}")
    except ValueError as e: 
        print(f"Error {e}")


