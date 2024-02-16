"""Module for manage the window for cutting image"""
# pylint: disable=no-member

import cv2
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
            self.__image_matrix = cv2.imread(self.__image_path)
        except ImportError as e:
            show_error(e)


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
        self.__init_cutter_window()


    def __init_cutter_window(self):
        self.__show_cutter_window(self.image_matrix)
        self.__set_mouse_key_tracking()


    def __set_mouse_key_tracking(self):
        image_matrix = self.image_matrix
        project_name = self.project_name
        mouse_tracking = MouseTracking(image_matrix, project_name)
        KeyTracking(image_matrix, mouse_tracking)


    def __show_cutter_window(self, image_matrix):
        """Set and show the main window for image cutter"""

        cv2.imshow(self.__project_name, image_matrix)


    @property
    def project_name(self):
        """give the value of private intance"""

        return self.__project_name