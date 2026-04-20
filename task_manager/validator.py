import re
from datetime import datetime, date


def valid_priority(priority):
    if not isinstance(priority, int):
        raise ValueError("Priority must be an integer")

    if priority < 1 or priority > 4:
        raise ValueError("Priority must be between 1 and 4")

    return priority


def valid_task(task):
    if not isinstance(task, str):
        raise ValueError("Task must be a string")

    cleaned_task = task.strip()

    if not cleaned_task:
        raise ValueError("Task cannot be empty")

    if not re.search(r"\w", cleaned_task, re.UNICODE):
        raise ValueError("Task must contain at least one letter or number")

    if len(cleaned_task) > 100:
        raise ValueError("Task cannot be greater than 100 characters")

    return cleaned_task


def valid_category(category):
    if not isinstance(category, str):
        raise ValueError("Category must be a string")

    cleaned_category = category.strip()

    if not cleaned_category:
        raise ValueError("Category cannot be empty")

    if not re.search(r"\w", cleaned_category, re.UNICODE):
        raise ValueError("Category must contain at least one letter or number")

    if len(cleaned_category) > 15:
        raise ValueError("Category cannot be greater than 15 characters")

    return cleaned_category


def valid_due_date(due_date, format_string="%Y-%m-%d"):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string")

    due_date = due_date.strip()

    if not due_date:
        raise ValueError("Due date cannot be empty")

    try:
        parsed_date = datetime.strptime(due_date, format_string).date()
        if parsed_date < date.today():
            raise ValueError("Due date cannot be in the past")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")


    return due_date


def valid_options(option):
    if not isinstance(option, int):
        raise ValueError("Option must be an integer")

    if option < 1 or option > 2:
        raise ValueError("Option must be either 1 or 2")

    return option

