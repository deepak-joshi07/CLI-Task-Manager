import uuid
from pathlib import Path
from datetime import datetime

from .storage import load_task, save_task
from .validator import (
    valid_priority,
    valid_task,
    valid_category,
    valid_due_date
)
from .models import Task


class TaskManager:
    def __init__(self):
        self.path = Path(__file__).resolve().parent.parent / "data" / "tasks.json"
        raw_tasks = load_task(self.path)
        self.tasks = {
            task_id: Task.from_dict(task_data)
            for task_id, task_data in raw_tasks.items()
        }

    def _save(self):
        data_to_save = {
            task_id: task.to_dict()
            for task_id, task in self.tasks.items()
        }
        save_task(self.path, data_to_save)

    def _get_task_by_id(self, task_id):
        if task_id not in self.tasks:
            raise ValueError("Task not found")
        return self.tasks[task_id]
    
    def list_tasks(self):
        return self.sort_task_by_priority()

    def add_task(self, task, priority, category, due_date):
        task_id = str(uuid.uuid4())

        new_task = Task(
            task_id=task_id,
            task=valid_task(task),
            priority=valid_priority(priority),
            category=valid_category(category),
            due_date=valid_due_date(due_date),
            completed=False,
            created_at=datetime.now().isoformat(timespec="seconds"),
            updated_at=None
        )

        self.tasks[task_id] = new_task
        self._save()
        return new_task

    def sort_tasks_by_priority(self):
        return sorted(self.tasks.values(), key=lambda task: task.priority)

    def sort_tasks_by_due_date(self):
        return sorted(self.tasks.values(), key=lambda task: task._due_date_obj())

    def delete_task_by_id(self, task_id):
        task = self._get_task_by_id(task_id)
        del self.tasks[task_id]
        self._save()
        return task

    def edit_task_by_id(
        self,
        task_id,
        new_task=None,
        new_priority=None,
        new_category=None,
        new_due_date=None
    ):
        task = self._get_task_by_id(task_id)

        task.update(
            task=valid_task(new_task) if new_task else None,
            priority=valid_priority(new_priority) if new_priority else None,
            category=valid_category(new_category) if new_category else None,
            due_date=valid_due_date(new_due_date) if new_due_date else None
        )

        self._save()
        return task

    def mark_task_complete_by_id(self, task_id):
        task = self._get_task_by_id(task_id)
        task.mark_complete()
        self._save()
        return task

    def filter_by_completion_status(self, status="pending"):
        if status not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")

        return [
            task
            for task in self.sort_tasks_by_priority()
            if (status == "completed" and task.completed)
            or (status == "pending" and not task.completed)
        ]

    def filter_overdue_tasks(self):
        return sorted(
            [task for task in self.tasks.values() if task.is_overdue()],
            key=lambda task: task._due_date_obj()
        )

    def filter_task_due_today(self):
        return sorted(
            [task for task in self.tasks.values() if task.is_due_today()],
            key=lambda task: task._due_date_obj()
        )

    def search_tasks(self, keyword):
        keyword = keyword.strip().lower()

        if not keyword:
            raise ValueError("Search keyword cannot be empty")

        return [
            task
            for task in self.sort_tasks_by_priority()
            if (
                keyword in task.task.lower()
                or keyword in task.category.lower()
                or keyword in task.due_date.lower()
                or keyword in str(task.priority)
                or keyword in ("completed" if task.completed else "pending")
            )
        ]