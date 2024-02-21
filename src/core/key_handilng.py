"""Module for manage the key event of the keyboard"""
# pylint: disable=no-member

import cv2

class KeyTracking:
    """Handle the events of keyboard"""

    def __init__(self, cutter_window):
        self.__cutter_window = cutter_window
        self.__if_loop_continues  = True
        self._init_loop()


    def _init_loop(self):
        while self.if_loop_continues:
            key = cv2.waitKey(12000)
            self.__handle_key(key)


    def __handle_key(self, key):
        if key == ord('l') or key == ord('L'):
            self.__clean_cutter_window()

        elif key == 27:
            self.__cancel_clipping()

        elif key == ord('s') or key == ord('S'):
            self.__save_image_clippings()


    def __clean_cutter_window(self):
        self.cutter_window.clean_cutter_window()


    def __cancel_clipping(self):
        self.__close_window()


    def __save_image_clippings(self):
        self.cutter_window.save_image_clippings()
        if self.cutter_window.image_cuts_coordinates is None:
            return

        self.__close_window()


    def __close_window(self):
        cv2.destroyAllWindows()
        self.__if_loop_continues = False


    @property
    def cutter_window(self):
        """give the value of private intance"""

        return self.__cutter_window


    @property
    def if_loop_continues(self):
        """give the value of private intance"""

        return self.__if_loop_continues
