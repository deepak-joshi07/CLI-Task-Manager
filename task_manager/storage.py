import os 
import json

def load_task(json_file_path):
    data = {}

    if os.path.exists(json_file_path) and os.path.getsize(json_file_path)>0:
        with open(json_file_path , mode ='r' , encoding='utf-8') as f:
            data = json.load(f)
    return data

def save_task(file_path , task):
        folder = os.path.dirname(file_path)
        os.makedirs(folder, exist_ok=True)
        with open(file_path , mode = 'w' , encoding= 'utf-8') as write_file: 
            json.dump(task , write_file , indent=4)