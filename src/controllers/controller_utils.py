"""Controler events of buttons"""
# pylint: disable=import-error

from core.cuts_writer import CutsWriter
from core.components_files import ImageFile
from core.image_handling import CutterWindowController
from core.api_utils import save_key_api


class Controller:
    """Class for copycharmntroller events of buttons"""
    def __init__(self):
        self.__image_format = ['.jpg', '.png']


    def __load_image(self, image_user_select, activate_env=False):
        image_file = ImageFile(image_user_select)
        if activate_env:
            image_file.init_env_project()
        return image_file


    def __start_cuts_image(self, image_file):

        project_name = image_file.image_file_name
        image_path_main = image_file.image_file_path

        cutter_window = CutterWindowController(project_name)
        cutter_window.show_cutter_window(image_path_main)
        return cutter_window


    def __save_cuts_image(self, cutter_window, image_file):
        if cutter_window.image_cuts_coordinates is None:
            return
        image_matrix = cutter_window.image_matrix
        cuts_coordinates = cutter_window.image_cuts_coordinates
        cuts_amount = cutter_window.image_cuts_amount
        cuts_paths = image_file.gen_path_image_cuts(cuts_amount)

        cuts_writer = CutsWriter(image_matrix)
        cuts_writer.save_images_cuts(cuts_paths, cuts_coordinates)


    def save_key_api(self, key_api):
        """call func from core for save api key"""

        save_key_api(key_api)


    def open_windows_cutter_image(self, image_user_select):
        """set the func for cut images"""

        image_file = self.__load_image(image_user_select, True)
        if image_file.project_format not in self.image_format:
            return
        cutter_window = self.__start_cuts_image(image_file)
        self.__save_cuts_image(cutter_window, image_file)


    @property
    def image_format(self):
        """give the value of private intance"""

        return self.__image_format