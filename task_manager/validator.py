import re
from datetime import datetime , date
def valid_priority(priority):

    if not isinstance(priority , int):
        raise ValueError('Expected an integer value')
    
    if priority < 1 or priority>4:
        raise ValueError('Value outside the range')
    
def valid_sno(tasks , sno):
    valid = len(tasks)

    if not isinstance(sno , int):
        raise ValueError('Expected a integer value')
    
    if 1> sno or sno  >valid: 
        raise ValueError('Value out side the range')

    
def valid_task(task): 
    if not isinstance(task , str):
        raise ValueError('Task must be a string')
    
    cleaned_task = task.strip()

    if cleaned_task == "": 
        raise ValueError("Error : Content required !")
    elif not re.search(r'\w' , cleaned_task , re.UNICODE):
        raise ValueError('Task must contain atleast one letter or number')
    elif len(cleaned_task) > 100:
        raise ValueError('Task cannot be greater than 100 characters')
    
    return cleaned_task


def valid_category(category):
    if not isinstance(category, str):
        raise ValueError("Category must be a string")

    cleaned_category = category.strip()

    if cleaned_category == "":
        raise ValueError("Category cannot be empty!")

    if not re.search(r"\w", cleaned_category, re.UNICODE):
        raise ValueError("Category must contain at least one letter or number")

    if len(cleaned_category) > 15:
        raise ValueError("Category cannot be greater than 15 characters")

    return cleaned_category


def valid_due_date(due_date, format_string="%Y-%m-%d"):
    if not isinstance(due_date, str):
        raise ValueError("Expected a string value")

    due_date = due_date.strip()

    if due_date == "":
        raise ValueError("Due date cannot be empty")

    try:
        parsed_date = datetime.strptime(due_date, format_string).date()
    except ValueError:
        raise ValueError("Invalid format. Use YYYY-MM-DD")

    if parsed_date < date.today():
        raise ValueError("Due date cannot be in the past")

    return due_date
    
