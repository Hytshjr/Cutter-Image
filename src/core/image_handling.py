"""Module for manage the window for cutting image"""
# pylint: disable=no-member

import cv2 as cv
from .exceptions import show_error
from .mouse_tracker import MouseTracking
from .key_handilng import KeyTracking



class Image:
    """Representing the info of image"""

    def __init__(self, image_file_path):
        self.__image_path = image_file_path
        self.__image_color_format = None
        self.__image_matrix = None
        self.__image_height = None
        self.__image_width = None
        self.__load_image_matrix()
        self.__set_image_dimension()


    def __load_image_matrix(self):
        try:
            path_to_find = cv.samples.findFile(self.__image_path)
            self.__image_matrix = cv.imread(path_to_find)
        except cv.error:
            show_error("Can't find the img file")


    def __set_image_dimension(self):
        height, widht, color_format = self.__image_matrix.shape
        self.__image_height = height
        self.__image_width = widht
        self.__image_color_format = color_format


    @property
    def image_path(self):
        """give the value of private intance"""

        return self.__image_path


    @property
    def image_color_format(self):
        """give the value of private intance"""

        return self.__image_color_format


    @property
    def image_matrix(self):
        """give the value of private intance"""

        return self.__image_matrix


    @property
    def image_height(self):
        """give the value of private intance"""

        return self.__image_height


    @property
    def image_width(self):
        """give the value of private intance"""

        return self.__image_width



class CutterWindowController(Image):
    """Class that manage info of windows project and controllers"""

    def __init__(self, image_file_path, project_name):
        super().__init__(image_file_path)
        self.__project_name = project_name
        self.__mouse_tracking = None
        self.__image_cuts_coordinates = None


    def show_cutter_window(self):
        """show windows for cut image"""

        if self.image_matrix is None:
            return
        self.__show_cutter_window()
        self.__set_mouse_tracking()
        self.__set_key_tracking()


    def __show_cutter_window(self):
        """Set and show the main window for image cutter"""

        cv.imshow(self.__project_name, self.image_matrix)


    def __set_mouse_tracking(self):
        project_name = self.project_name
        image_matrix = self.image_matrix

        self.__mouse_tracking = MouseTracking()
        self.mouse_tracking.init_tracking(image_matrix, project_name)


    def __set_key_tracking(self):
        KeyTracking(self)


    def __get_cuts_coordinates(self):
        return self.mouse_tracking.rectangle_history_area_coordinates


    def clean_cutter_window(self):
        """Clean the windows for cut image"""

        self.mouse_tracking.reset_image_crop()


    def save_image_clippings(self):
        """Save the cuts of image coordinates"""

        self.__image_cuts_coordinates = self.__get_cuts_coordinates()


    @property
    def project_name(self):
        """give the value of private intance"""

        return self.__project_name


    @property
    def mouse_tracking(self):
        """give the value of private intance"""

        return self.__mouse_tracking


    @property
    def image_cuts_coordinates(self):
        """give the value of private intance"""

        return self.__image_cuts_coordinates