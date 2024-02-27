"""File for hadle api key."""
# pylint: disable=import-error

import os
import fileinput
from config import BASE_DIR

def save_key_api(key_api):
    """Save the api key on env file."""
    env_path = os.path.join(BASE_DIR, '.env')
    option = 'API_KEY'

    with fileinput.FileInput(env_path, inplace=True) as file:
        for line in file:
            if  option in line:
                print(f'{option}={key_api}')
            else:
                print(line, end='')