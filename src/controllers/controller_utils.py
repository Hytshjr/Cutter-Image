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
        self.__image_file = None
        self.__cuts_writer = None
        self.__cutter_window = None


    def __load_image(self, image_user_select):
        self.__image_file = ImageFile(image_user_select)
        return self.__image_file


    def __start_cuts_image(self, image_file):
        project_name = image_file.image_file_name
        image_path_main = image_file.image_file_path
        image_name_project = (image_path_main, project_name)
        cutter_window = CutterWindowController(*image_name_project)
        cutter_window.show_cutter_window()

        return cutter_window


    def __save_cuts_image(self, cutter_window, image_file):
        image_matrix = cutter_window.image_matrix
        image_cuts = cutter_window.image_cuts_coordinates
        image_matrix_cuts = (image_matrix, image_cuts)
        cuts_writer = CutsWriter()
        cuts_writer.select_cuts_image_matrix(*image_matrix_cuts)

        cuts_amount = len(cuts_writer.image_cuts_matrix)
        path_image_cuts = image_file.gen_path_image_cuts(cuts_amount)
        cuts_writer.save_images_cuts(path_image_cuts)


    def save_key_api(self, key_api):
        """call func from core for save api key"""
        save_key_api(key_api)


    def open_windows_cutter_image(self, image_user_select):
        """set the func for cut images"""

        image_file = self.__load_image(image_user_select)
        cutter_window = self.__start_cuts_image(image_file)
        self.__save_cuts_image(cutter_window, image_file)


    @property
    def image_format(self):
        """give the value of private intance"""

        return self.__image_format


    @property
    def image_file(self):
        """give the value of private intance"""

        return self.__image_file


    @property
    def cuts_writer(self):
        """give the value of private intance"""

        return self.__cuts_writer


    @property
    def cutter_window(self):
        """give the value of private intance"""

        return self.__cutter_window