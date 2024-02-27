"""File for hadle the paths."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(BASE_DIR, 'resources', 'templates')
MEDIA_ROOT = os.path.join(BASE_DIR, 'src', 'interface', 'static')

print(BASE_DIR)
print(TEMPLATE_ROOT)
print(MEDIA_ROOT)