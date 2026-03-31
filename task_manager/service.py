import uuid
from pathlib import Path
from .storage import load_task, save_task
from .validator import valid_priority, valid_sno, valid_task , valid_category
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.path = Path(__file__).resolve().parent.parent / "data" / "tasks.json"
        self.tasks = load_task(self.path)

    def add_task(self, task, priority , category):
        task_id = str(uuid.uuid4())

        valid_priority(priority)
        task = valid_task(task)
        category = valid_category(category)

        completed = False
        created_at = datetime.now().isoformat(timespec="seconds")
        updated_at = None

        self.tasks[task_id] = {
            'task': task,
            'priority': priority,
            'category' : category,
            'completed': completed,
            'created_at' : created_at,
            'updated_at' : updated_at
        }

        save_task(self.path, self.tasks)

        return {
            "task_id": task_id,
            "task": task,
            "priority": priority,
            "completed": completed,
            "created_at": created_at,
            "updated_at": updated_at,
            "category": category
        }

    def mark_task_complete(self, sno):
        required_id = self.get_task_id_by_sno(sno)
        completed_task = self.tasks[required_id]

        if completed_task.get('completed', False):
            raise ValueError("Task is already completed.")

        completed_task['completed'] = True
        completed_task['updated_at'] = datetime.now().isoformat(timespec="seconds")
        save_task(self.path, self.tasks)

        return completed_task

    def sort_tasks(self):
        sorted_tasks = sorted(
            self.tasks.items(),
            key=lambda task_item: task_item[1]['priority']
        )
        return sorted_tasks

    def list_tasks(self):
        sorted_tasks = self.sort_tasks()
        result = []

        for sno, (task_id, detail) in enumerate(sorted_tasks, start=1):
            if 'completed' not in detail:
                detail['completed'] = False
            result.append((sno, task_id, detail))

        return result

    def get_task_id_by_sno(self, sno):
        sorted_tasks = self.sort_tasks()
        valid_sno(sorted_tasks, sno)

        for serial_no, (task_id, detail) in enumerate(sorted_tasks, start=1):
            if serial_no == sno:
                return task_id

        raise ValueError("Invalid serial number")

    def delete_task(self, sno):
        delete_id = self.get_task_id_by_sno(sno)
        task_to_delete = self.tasks[delete_id]

        if 'completed' not in task_to_delete:
            task_to_delete['completed'] = False

        del self.tasks[delete_id]
        save_task(self.path, self.tasks)

        return task_to_delete

    def edit_task(self, sno, new_task=None, new_priority=None , new_category = None):
        edit_task_id = self.get_task_id_by_sno(sno)

        if new_task is not None:
            new_task = valid_task(new_task)
            self.tasks[edit_task_id]['task'] = new_task

        if new_priority is not None:
            valid_priority(new_priority)
            self.tasks[edit_task_id]['priority'] = new_priority

        if new_category is not None: 
            new_category = valid_category(new_category)
            self.tasks[edit_task_id]['category'] = new_category

        if 'completed' not in self.tasks[edit_task_id]:
            self.tasks[edit_task_id]['completed'] = False
        
        self.tasks[edit_task_id]['updated_at'] = datetime.now().isoformat(timespec= "seconds")

        save_task(self.path, self.tasks)
        return self.tasks[edit_task_id]