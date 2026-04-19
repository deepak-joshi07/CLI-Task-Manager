from dataclasses import dataclass, asdict
from datetime import datetime, date

@dataclass
class Task:
    task_id:str
    task: str
    priority: int
    category: str
    due_date: str
    completed: bool
    created_at: str
    updated_at: str | None = None

    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    
    def mark_complete(self):
        if self.completed:
            raise ValueError("Task already completed")
        self.completed = True
        self.updated_at = datetime.now().isoformat(timespec="seconds")

    def update(
        self,
        task=None,
        priority=None,
        category=None,
        due_date=None
    ):
        if task is not None:
            self.task = task

        if priority is not None:
            self.priority = priority

        if category is not None:
            self.category = category

        if due_date is not None:
            self.due_date = due_date

        self.updated_at = datetime.now().isoformat(timespec="seconds")

    def is_overdue(self):
        return (
            not self.completed and
            self._due_date_obj() < date.today()
        )

    def is_due_today(self):
        return (
            not self.completed and
            self._due_date_obj() == date.today()
        )

    def _due_date_obj(self):
        return datetime.strptime(self.due_date, "%Y-%m-%d").date()


    