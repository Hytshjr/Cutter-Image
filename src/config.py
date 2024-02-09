import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'src', 'presentation', 'static')
MAIN_ROOT = os.path.join(BASE_DIR)