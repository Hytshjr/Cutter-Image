"""Module for manage the window for cutting image"""
# pylint: disable=no-member
# pylint: disable=catching-non-exception

import cv2 as cv
from .exceptions import show_error
from .key_handilng import KeyTracking
from .mouse_tracker import MouseTracking


class CutterWindowController:
    """Class that manage info of windows project and controllers"""

    def __init__(self, project_name):
        self.__image_cuts_coordinates = None
        self.__project_name = project_name
        self.__mouse_tracking = None
        self.__image_matrix = None


    def __load_image_matrix(self, image_path_main):
        try:
            path_to_find = cv.samples.findFile(image_path_main)
            self.__image_matrix = cv.imread(path_to_find)
        except cv.error:
            error = "Can't find the image file"
            show_error(error, image_path_main)


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


    def __complete_selected_cuts(self, cuts_coordinates):
        widht_matrix = self.image_matrix.shape[1]
        cuts_coordinates = cuts_coordinates.copy()
        self.__process_coordinates(cuts_coordinates, widht_matrix)


    def __process_coordinates(self, cuts_coordinates, widht_matrix):
        cuts_amount_added = 0

        for index in range(self.image_cuts_amount):
            new_height_cut = cuts_coordinates[index][2]
            previous_cut = cuts_coordinates[index - 1]

            if new_height_cut == 0:
                top = previous_cut[0]
                bottom = previous_cut[1]
                right = previous_cut[3]
                if right != widht_matrix:
                    index += cuts_amount_added
                    coordinate = (top, bottom, right, widht_matrix)
                    self.__add_coordinate_last_cut(coordinate, index)
                    cuts_amount_added += 1


    def __add_coordinate_last_cut(self, coordinate, index):
        if index == 0:
            self.image_cuts_coordinates.append(coordinate)
        else:
            self.image_cuts_coordinates.insert(index, coordinate)


    def show_cutter_window(self, image_path_main):
        """show windows for cut image"""

        self.__load_image_matrix(image_path_main)
        if self.image_matrix is None:
            return
        self.__show_cutter_window()
        self.__set_mouse_tracking()
        self.__set_key_tracking()


    def clean_cutter_window(self):
        """Clean the windows for cut image for key 'L' """

        self.mouse_tracking.reset_image_crop()


    def save_image_clippings(self):
        """Save the cuts of image coordinates for key 'S' """

        self.__image_cuts_coordinates = self.__get_cuts_coordinates()
        self.__complete_selected_cuts(self.image_cuts_coordinates)


    @property
    def image_cuts_amount(self):
        """give the amount of cuts on image"""

        return len(self.__image_cuts_coordinates)


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


    @property
    def image_matrix(self):
        """give the value of private intance"""

        return self.__image_matrix