"""Write the image cuts"""
# pylint: disable=no-member

import cv2

class CutsWriter:
    """Save the images cuts of cutter window"""
    def __init__(self):
        self.__images_cuts_coordinates = None
        self.__image_cuts_matrix = []
        self.__image_cuts_paths = None
        self.__image_matrix = None


    def __set_image_matrix(self, image_matrix):
        self.__image_matrix = image_matrix


    def __set_image_cuts_coodinates(self, cuts_coordinates):
        self.__images_cuts_coordinates = cuts_coordinates


    def __add_coordinate_last_cut(self, coordinate, index):
        if index == 0:
            self.images_cuts_coordinates.append(coordinate)
        else:
            self.images_cuts_coordinates.insert(index, coordinate)


    def __process_coordinates(self, cuts_coordinates, widht_matrix):
        cuts_amount = len(cuts_coordinates)

        for index in range(cuts_amount):
            new_height_cut = cuts_coordinates[index][2]
            previous_cut = cuts_coordinates[index -1]

            if new_height_cut == 0:
                top = previous_cut[0]
                bottom = previous_cut[1]
                right = previous_cut[3]
                if right != widht_matrix:
                    coordinate = (top, bottom, right, widht_matrix)
                    self.__add_coordinate_last_cut(coordinate, index)


    def select_cuts_image_matrix(self, image_matrix, cuts_coordinates):
        """select the cuts from image matrix"""

        widht_matrix = image_matrix.shape[1]
        self.__set_image_matrix(image_matrix)
        self.__set_image_cuts_coodinates(cuts_coordinates)
        self.__process_coordinates(cuts_coordinates, widht_matrix)

        for cut_coordinate in self.images_cuts_coordinates:
            top, bottom, left, right = cut_coordinate
            matrix_cut = self.image_matrix[top:bottom,left:right]
            self.image_cuts_matrix.append(matrix_cut)


    def save_images_cuts(self, path_cuts):
        """select the cuts from image matrix"""

        cuts_matrix_paths = zip(path_cuts, self.image_cuts_matrix)
        for path_cut, cut_matrix in cuts_matrix_paths:
            cv2.imwrite(path_cut, cut_matrix)


    @property
    def images_cuts_coordinates(self):
        """give the value of private intance"""

        return self.__images_cuts_coordinates


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