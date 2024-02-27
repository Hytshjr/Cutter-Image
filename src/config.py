"""File for hadle the paths."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'src', 'interface', 'static')
CORE_ROOT = os.path.join(BASE_DIR, 'src')
TEMPLATE_ROOT = os.path.join(BASE_DIR, 'resources', 'templates')