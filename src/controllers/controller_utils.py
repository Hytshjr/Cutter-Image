"""Controler events of buttons"""
# pylint: disable=import-error

from core.cuts_writer import CutsWriter
from core.components_files import ImageFile
from core.image_handling import CutterWindowController
from core.api_utils import save_key_api


class Controller:
    """Class for copycharmntroller events of buttons"""
    def __init__(self):
        self.__img_format = ['.jpg', '.png']


    def save_key_api(self, key_api):
        """call func from core for save api key"""
        save_key_api(key_api)


    def open_windows_cutter_image(self, image_user_select):
        """set the func for cut images"""

        image_file = ImageFile(image_user_select)
        if image_file.project_format not in self.__img_format:
            return

        project_name = image_file.project_name
        image_path_main = image_file.image_file_path
        image_file.prepare_for_a_file_format(image_path_main)

        image_name_project = (image_path_main, project_name)
        cutter_windows = CutterWindowController(*image_name_project)
        cutter_windows.show_cutter_window()
        image_cuts_coordinates = cutter_windows.image_cuts_coordinates
        if image_cuts_coordinates is None:
            return

        cut_writer = CutsWriter()
        image_matrix = cutter_windows.image_matrix
        image_matrix_cuts = image_matrix, image_cuts_coordinates
        cut_writer.select_cuts_image_matrix(*image_matrix_cuts)

        cuts_amount = len(cut_writer.image_cuts_matrix)
        path_image_cuts = image_file.gen_path_image_cuts(cuts_amount)
        cut_writer.save_images_cuts(path_image_cuts)

