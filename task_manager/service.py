import uuid
from pathlib import Path
from .storage import load_task , save_task
from .validator import valid_priority , valid_sno ,valid_task
class TaskManager:
    def __init__(self):
        self.path = Path(__file__).resolve().parent.parent /"data"/"tasks.json" # Ot wo;; later move to config
        self.tasks = load_task(self.path)
    
    def add_task(self , task , priority): 
        # genrating task id
        task_id = str(uuid.uuid4())

        # Handeling priority
        valid_priority(priority)
        # checking for valid task
        task = valid_task(task)
       # append it to the task.json

        self.tasks[task_id] = {
            'task' : task,
            'priority' : priority
        }
        save_task(self.path , self.tasks)

        return {"task_id": task_id, "task": task, "priority": priority}
    

    def sort_tasks(self): 
        sorted_tasks =  sorted(
            self.tasks.items() , 
            key = lambda task_item : task_item[1]['priority'])
        return sorted_tasks


    def list_tasks(self): 
        sorted_tasks = self.sort_tasks()
        result = []
        for sno , (task_id , detail) in enumerate(sorted_tasks , start=1):
            result.append((sno,task_id ,  detail ))
        return result

    def get_task_id_by_sno(self , sno): 
        sorted_tasks = self.sort_tasks()
        valid_sno(sorted_tasks , sno)

        for serial_no , (task_id , detail) in enumerate(sorted_tasks , start = 1):
            if serial_no == sno: 
                return task_id
            
        raise ValueError('Invalid serial number')

    def delete_task(self , sno): 
        delete_id = self.get_task_id_by_sno(sno)
        #  Delete the selected task 
        task_to_delete = self.tasks[delete_id]
        del self.tasks[delete_id]
        save_task(self.path , self.tasks)
        return task_to_delete
    
    def edit_task(self ,sno, new_task = None , new_priority = None):
        edit_task_id = self.get_task_id_by_sno(sno)

        if new_task is not None:
            new_task = valid_task(new_task)
            self.tasks[edit_task_id]['task'] = new_task
        if  new_priority is not None: 
            valid_priority(new_priority)
            self.tasks[edit_task_id]['priority'] = new_priority
        save_task(self.path , self.tasks)
        return self.tasks[edit_task_id]

