"""Controler events of buttons"""
# pylint: disable=import-error

from core.components_files import ImageFile, rename_file
from core.image_handling import CutterWindowController
from core.api_utils import save_key_api

class Controller:
    """Class for copycharmntroller events of buttons"""
    def __init__(self):
        pass


    def save_key_api(self, key_api):
        """call func from core for save api key"""
        save_key_api(key_api)


    def open_windows_cutter_image(self, image_user_select):
        """set the func for cut images"""

        image_file = ImageFile(image_user_select)
        project_name = image_file.project_name
        old_path = image_file.project_main_file
        new_path = image_file.image_file_path
        rename_file(old_path=old_path, new_path=new_path)
        image_file.update_project_main_file(new_path)

        CutterWindowController(new_path, project_name)
