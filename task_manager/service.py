import uuid
from pathlib import Path
from .storage import load_task , save_task
from .validator import valid_priority , valid_sno
class TaskManager:
    def __init__(self , file_path = 'data//tasks.json' ):
        self.path = Path(__file__).resolve().parent.parent /"data"/"task.json"
        self.task = load_task(self.path)
    
    def add_task(self , task , priority): 
        # genrating task id
        task_id = str(uuid.uuid4())

        # Handeling priority
        valid_priority(priority)
       # append it to the task.json

        self.task[task_id] = {
            'task' : task,
            'priority' : priority
        }
        save_task(self.path , self.task)

        return {"task_id": task_id, "task": task, "priority": priority}
    

    def sort_task(self): 
        sorted_data = dict(sorted(self.task.items() , key = lambda x : x[1]['priority']))
        return sorted_data


    def list_task(self): 
        sorted_task = self.sort_task()
        result = []
        for i , (task_id , detail) in enumerate(sorted_task.items()):
            result.append([i+1, detail ])
        return result



    def delete_task(self , sno): 
        # call list_task function -> which store task in sorte order with numbering as uuid can give any id 
        sorted_task = self.sort_task()
        valid_sno(sorted_task , sno)
        task_to_delete = None
        delete_id = None
        # Ask the user to select one serial number
        for i , (task_id , detail) in enumerate(sorted_task.items()): 
            if i+1 == sno : 
                delete_id = task_id
                break

        if delete_id is None: 
            raise ValueError('Invalid serial number')

        #  Delete the selected task 
        task_to_delete = self.task[delete_id]
        del self.task[delete_id]
        save_task(self.path , self.task)
        return task_to_delete
    
    def edit_task(self ,sno, new_task = None , new_priority = None):
        sorted_task = self.sort_task()
        valid_sno(sorted_task , sno)
        edit_id = None

        # find the task to edit
        for i , (task_id , detail) in enumerate(sorted_task.items()): 
            if i+1 == sno : 
                edit_id = task_id
                break
        if new_task is not None:
            self.task[edit_id]['task'] = new_task
        if  new_priority is not None: 
            valid_priority(new_priority)
            self.task[edit_id]['priority'] = new_priority
        save_task(self.path , self.task)
        return self.task[edit_id]

