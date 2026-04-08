import uuid
from pathlib import Path
from datetime import datetime

from .storage import load_task, save_task
from .validator import (
    valid_priority,
    valid_task,
    valid_category,
    valid_due_date,
    valid_list_sno
)


class TaskManager:
    def __init__(self):
        self.path = Path(__file__).resolve().parent.parent / "data" / "tasks.json"
        self.tasks = load_task(self.path)

    def add_task(self, task, priority, category, due_date):
        task_id = str(uuid.uuid4())

        valid_priority(priority)
        task = valid_task(task)
        category = valid_category(category)
        due_date = valid_due_date(due_date)

        completed = False
        created_at = datetime.now().isoformat(timespec="seconds")
        updated_at = None

        self.tasks[task_id] = {
            'task': task,
            'priority': priority,
            'category': category,
            'due_date': due_date,
            'completed': completed,
            'created_at': created_at,
            'updated_at': updated_at
        }

        save_task(self.path, self.tasks)

        return {
            "task_id": task_id,
            "task": task,
            "priority": priority,
            "category": category,
            "due_date": due_date,
            "completed": completed,
            "created_at": created_at,
            "updated_at": updated_at
        }

    def sort_tasks(self):
        return sorted(
            self.tasks.items(),
            key=lambda task_item: task_item[1]['priority']
        )

    def list_tasks(self):
        sorted_tasks = self.sort_tasks()
        result = []

        for sno, (task_id, detail) in enumerate(sorted_tasks, start=1):
            result.append((sno, task_id, detail))

        return result

    def get_task_list_id_by_sno(self, task_list, sno):
        valid_list_sno(task_list, sno)

        for serial_number, task_id, _ in task_list:
            if serial_number == sno:
                return task_id

        raise ValueError("Invalid serial number")

    def delete_task_by_id(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found")

        task_to_delete = self.tasks[task_id]
        del self.tasks[task_id]
        save_task(self.path, self.tasks)

        return task_to_delete

    def delete_task_by_list(self, task_list, sno):
        task_id = self.get_task_list_id_by_sno(task_list, sno)
        return self.delete_task_by_id(task_id)

    def edit_task_by_id(self, task_id, new_task=None, new_priority=None, new_category=None, new_due_date=None):
        if task_id not in self.tasks:
            raise ValueError("Task not found")

        if new_task is not None:
            self.tasks[task_id]['task'] = valid_task(new_task)

        if new_priority is not None:
            valid_priority(new_priority)
            self.tasks[task_id]['priority'] = new_priority

        if new_category is not None:
            self.tasks[task_id]['category'] = valid_category(new_category)

        if new_due_date is not None:
            self.tasks[task_id]['due_date'] = valid_due_date(new_due_date)

        self.tasks[task_id]['updated_at'] = datetime.now().isoformat(timespec="seconds")

        save_task(self.path, self.tasks)
        return self.tasks[task_id]

    def edit_task_by_list(self, task_list, sno, new_task=None, new_priority=None, new_category=None, new_due_date=None):
        task_id = self.get_task_list_id_by_sno(task_list, sno)
        return self.edit_task_by_id(task_id, new_task, new_priority, new_category, new_due_date)

    def mark_task_complete_by_id(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found")

        completed_task = self.tasks[task_id]

        if completed_task['completed']:
            raise ValueError("Task is already completed.")

        completed_task['completed'] = True
        completed_task['updated_at'] = datetime.now().isoformat(timespec="seconds")
        save_task(self.path, self.tasks)

        return completed_task

    def mark_task_complete(self, task_list, sno):
        task_id = self.get_task_list_id_by_sno(task_list, sno)
        return self.mark_task_complete_by_id(task_id)