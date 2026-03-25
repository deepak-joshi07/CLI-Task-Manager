def valid_priority(priority):
    if not isinstance(priority , int):
        raise ValueError('Expected an integer value')
    if priority < 1 or priority>4:
        raise ValueError('Value outside the range')
    
def valid_sno(task , sno):
    valid = len(task)

    if not isinstance(sno , int):
        raise ValueError('Expected a integer value')
    if 1> sno or sno  >valid: 
        raise ValueError('Value out side the range')

    
