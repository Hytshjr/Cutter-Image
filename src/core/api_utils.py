from config import MAIN_ROOT
import fileinput
import os

def replace_api(entry_api):
    entry_api.config(state='normal')

def save_api(entry_api):
    env_path = os.path.join(MAIN_ROOT, '.env')
    option = 'API_KEY'
    
    entry_api.config(state='disable')

    with fileinput.FileInput(env_path, inplace=True) as file:
        for line in file:   
            if  option in line:
                  print(f'{option}={entry_api.get()}')
            else:
                  print(line, end='')
