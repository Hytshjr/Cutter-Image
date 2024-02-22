"""Write the image cuts"""
# pylint: disable=no-member

import cv2 as cv

class CutsWriter:
    """Save the images cuts of cutter window"""
    def __init__(self, image_matrix):
        self.__image_cuts_coordinates = None
        self.__image_matrix = image_matrix
        self.__image_cuts_matrix = []
        self.__image_cuts_paths = None


    def __select_cuts_image_matrix(self, cuts_coordinates):

        for cut_coordinate in cuts_coordinates:
            top, bottom, left, right = cut_coordinate
            matrix_cut = self.image_matrix[top:bottom,left:right]
            self.image_cuts_matrix.append(matrix_cut)


    def save_images_cuts(self, path_cuts, coordinate_cuts):
        """select the cuts from image matrix"""

        self.__select_cuts_image_matrix(coordinate_cuts)
        cuts_matrix_paths = zip(path_cuts, self.image_cuts_matrix)
        for path_cut, cut_matrix in cuts_matrix_paths:
            cv.imwrite(path_cut, cut_matrix)


    @property
    def image_cuts_coordinates(self):
        """give the value of private intance"""

        return self.__image_cuts_coordinates


    @property
    def image_cuts_matrix(self):
        """give the value of private intance"""

        return self.__image_cuts_matrix


    @property
    def image_cuts_paths(self):
        """give the value of private intance"""

        return self.__image_cuts_paths


    @property
    def image_matrix(self):
        """give the value of private intance"""

        return self.__image_matrix