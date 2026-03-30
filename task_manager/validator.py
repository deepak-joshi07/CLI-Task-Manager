import re
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
    if not cleaned_task == 0: 
        raise ValueError("Error : Content required !")
    elif not re.search(r'\w' , cleaned_task , re.UNICODE):
        raise ValueError('Task must contain atleast one letter or number')
    elif len(task) > 100:
        raise ValueError('Task cannot be greater than 100 characters')
    
    return cleaned_task


