"""Module for manage the key event of the keyboard"""
# pylint: disable=no-member

import cv2

class KeyTracking:
    """Handle the events of keyboard"""

    def __init__(self, mouse_tracking):
        self.__mouse_tracking = mouse_tracking
        self.__if_loop_continues  = True
        self._init_loop()


    def _init_loop(self):
        while self.if_loop_continues:
            key = cv2.waitKey(12000)
            self.__handle_key(key)


    def __handle_key(self, key):
        if key == ord('l') or key == ord('L'):
            self.__clean_image()

        elif key == 27:
            self.__cancel_clipping()

        elif key == ord('s') or key == ord('S'):
            self.__save_image_clippings()


    def __clean_image(self):
        self.mouse_tracking.reset_image_crop()



    def __cancel_clipping(self):
        self.__close_window()


    def __save_image_clippings(self):
        self.__close_window()


    def __close_window(self):
        cv2.destroyAllWindows()
        self.__if_loop_continues = False


    @property
    def mouse_tracking(self):
        """give the value of private intance"""

        return self.__mouse_tracking


    @property
    def if_loop_continues(self):
        """give the value of private intance"""

        return self.__if_loop_continues
