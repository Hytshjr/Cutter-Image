"""Controler events of buttons"""
# pylint: disable=import-error

from core.components_files import ImageFile
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
        image_path_main = image_file.image_file_path
        image_name_project = (image_path_main, project_name)
        image_file.prepare_for_a_file_format(image_path_main)

        cutter_windows = CutterWindowController(*image_name_project)
        images_cuts = cutter_windows.image_cuts
        cuts_amount = len(images_cuts)

        path_image_cuts = image_file.gen_path_image_cuts(cuts_amount)

