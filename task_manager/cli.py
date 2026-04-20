import argparse
from task_manager .service import TaskManager

manager = TaskManager()

def print_task(task):
    print(
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
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print_task(task)
    
def main():
    parser = argparse.ArgumentParser(prog = 'Task_manager')
    subparsers = parser.add_subparsers(dest = 'operation' , help = 'Enter the operation you want to perform')

    add_parser = subparsers.add_parser('add' , help = 'Enter task details you want to add')

    add_parser.add_argument('--name' ,required= True , help = 'Enter the name of the task you want to add')
    add_parser.add_argument('--priority' ,type= int ,required=True, help= 'Enter the priority that you want to assign to your task (enter number between 1 to 4)')
    add_parser.add_argument('--category' , required=True , help='Entter the category of the task')
    add_parser.add_argument('--due_date' , required=True , help= 'Enter the due date of the task')

    list_parser = subparsers.add_parser('list' , help = 'List all tasks')

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("--id", required=True , help = 'ID of task you want to delete')

    edit_parser = subparsers.add_parser("edit", help="Edit a task")
    edit_parser.add_argument("--id", required=True , help = 'Enter the id of task you want to edit ')
    edit_parser.add_argument("--name" , help = 'Enter the new name if you want to edit else skip')
    edit_parser.add_argument("--priority", type=int , help = 'Enter the priority if you want to edit else skip' )
    edit_parser.add_argument("--category" , help = 'Enter the new category if you want to edit else skip')
    edit_parser.add_argument("--due_date" , help = 'Enter the new due date if you want to edit else skip')

    search_parser = subparsers.add_parser('search' , help='Enter the keyword you want to search' )
    search_parser.add_argument('--keyword' ,required=True, help= 'Enter the keyword you want to search')

    complete_parser = subparsers.add_parser("complete", help="Mark task complete")
    complete_parser.add_argument("--id", required=True , help = 'Enter the id of the task you want to mark complete')

    filter_parser = subparsers.add_parser("filter")
    filter_parser.add_argument("--status", choices=["pending", "completed"])
    filter_parser.add_argument("--category")
    filter_parser.add_argument("--priority", type=int)

    subparsers.add_parser("today", help="Tasks due today")

    subparsers.add_parser("overdue", help="Overdue tasks")

    args = parser.parse_args()

    try:
        if args.operation == "add":
            task = manager.add_task(
                args.name,
                args.priority,
                args.category,
                args.due_date
            )
            print("Task added:")
            print_task(task)

        elif args.operation == "list":
            tasks = manager.list_tasks()
            print_task_list(tasks)

        elif args.operation == "search":
            tasks = manager.search_tasks(args.keyword)
            print_task_list(tasks)

        elif args.operation == "delete":
            task = manager.delete_task_by_id(args.id)
            print("Task deleted:")
            print_task(task)

        elif args.operation == "edit":
            task = manager.edit_task_by_id(
                args.id,
                args.name,
                args.priority,
                args.category,
                args.due_date
            )
            print("Task updated:")
            print_task(task)

        elif args.operation == "complete":
            task = manager.mark_task_complete_by_id(args.id)
            print("Task marked complete:")
            print_task(task)

        elif args.operation == "filter":
            tasks = manager.filter_tasks(
                status=args.status,
                category=args.category,
                priority=args.priority
            )
            print_task_list(tasks)

        elif args.operation == "today":
            tasks = manager.filter_task_due_today()
            print_task_list(tasks)

        elif args.operation == "overdue":
            tasks = manager.filter_overdue_tasks()
            print_task_list(tasks)

        else:
            parser.print_help()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()