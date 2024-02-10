"""File for hadle api key."""
# pylint: disable=import-error

import os
import fileinput
from config import CORE_ROOT

def save_key_api(key_api):
    """Save the api key on env file."""
    env_path = os.path.join(CORE_ROOT, '.env')
    option = 'API_KEY'

    with fileinput.FileInput(env_path, inplace=True) as file:
        for line in file:
            if  option in line:
                print(f'{option}={key_api}')
            else:
                print(line, end='')