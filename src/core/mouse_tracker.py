"""Module for track movement and event of mouse"""
# pylint: disable=no-member
# pylint: disable=unused-argument

import cv2


class MouseTracking:
    """Class for tracking mouse events"""

    def __init__(self):
        self.__image_matrix_clean = None
        self.__rectangle_area_coordinates = {}
        self.__image_matrix_utility = None
        self.__project_name = None
        self.__image_matrix_width = None
        self.__position_window = 0
        self.__last_bottom = 0


    def __set_project_name(self, project_name):
        self.__project_name = project_name


    def __set_image_matrix_clean(self, image_matrix):
        self.__image_matrix_clean = image_matrix


    def __set_image_matrix_for_utility(self):
        self.__image_matrix_utility = self.image_matrix_clean.copy()


    def __set_image_matrix_width(self):
        self.__image_matrix_width = self.image_matrix_clean.shape[1]


    def __init_tracking(self):
        mouse_event = self.handle_mouse_event
        cv2.setMouseCallback(self.project_name, mouse_event)


    def handle_mouse_event(self, event, x, y, flags, param):
        """Select action depend on event"""

        if event == cv2.EVENT_MOUSEWHEEL:
            self.__handle_scroll_mouse(flags)
            self.__refresh_window_image()
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.__handle_left_click_event(y)
            self.__refresh_window_image()
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.__handle_right_click_event(y, x)
            self.__refresh_window_image()


    def __handle_scroll_mouse(self, flags):
        scroll_amount = 50 if flags < 0 else -50
        if self.position_window == 0 and scroll_amount == -50:
            return
        self.__update_position_window (scroll_amount)


    def __handle_right_click_event(self, click_y, click_x):
        self.__set_rectangle_area(click_y, click_x)
        self.__draw_reactangle_in_window()


    def __handle_left_click_event(self, click_y):
        self.__set_rectangle_area(click_y, self.image_matrix_width)
        self.__draw_reactangle_in_window()


    def __update_position_window(self, updated_position):
        self.__position_window += updated_position


    def __set_rectangle_area(self, click_y, click_x):
        if self.__click_to_select_new_cut_area(click_y):
            self.__set_rectangle_area_height(click_y)

        self.__set_rectangle_area_widht(click_y, click_x)
        self.__save_rectangle_history_area_coordinates()


    def __set_rectangle_area_height(self, click_y):
        self.rectangle_area_coordinates.update({
                    'top': self.last_bottom,
                    'bottom': click_y + self.position_window
                })
        self.__last_bottom = self.__get_side_of_rectangle('bottom')


    def __set_rectangle_area_widht(self, click_y, click_x):
        if self.__click_to_select_new_cut_area(click_y):
            self.__rectangle_area_coordinates['left'] = 0
        else:
            last_right_click = self.__get_side_of_rectangle('right')
            self.__rectangle_area_coordinates.update({
                'left' : last_right_click
                })
        self.__rectangle_area_coordinates['right'] = click_x


    def __set_rectangle_area_to_draw(self):
        top, bottom, left, right = self.__get_side_of_rectangle()

        right_bot = (right, bottom)
        left_top = (left, top)

        return right_bot, left_top


    def __draw_reactangle_in_window(self):
        right_bot, left_top = self.__set_rectangle_area_to_draw()
        color = (251, 0, 255)

        cv2.rectangle(
            self.image_matrix_utility, right_bot,
            left_top, color)


    def __click_to_select_new_cut_area(self, click_y):
        rectangle_bottom = self.last_bottom
        position_click = click_y + self.position_window
        if position_click >= rectangle_bottom:
            return True

        return False


    def __refresh_window_image(self):
        scrolled_image = self.__scroll_image()
        cv2.imshow(self.project_name, scrolled_image)


    def __scroll_image(self):
        size_window = 1080
        top_image = self.position_window
        bottom_image = self.position_window + size_window

        return self.image_matrix_utility[top_image:bottom_image]


    def __get_side_of_rectangle(self, side='all'):
        if side == 'all':
            top = self.rectangle_area_coordinates['top']
            bottom = self.rectangle_area_coordinates['bottom']
            left = self.rectangle_area_coordinates['left']
            right = self.rectangle_area_coordinates['right']

            return top, bottom, left, right

        try:
            return self.rectangle_area_coordinates[side]
        except KeyError:
            return None


    def __save_rectangle_history_area_coordinates(self):
        name_of_history = 'history_area_coordinates'
        if name_of_history not in self.rectangle_area_coordinates:
            self.__rectangle_area_coordinates[name_of_history] = []

        self.rectangle_area_coordinates[name_of_history].append(
            self.__get_side_of_rectangle()
            )


    def init_tracking(self, image_matrix, project_name):
        """init the tracking of event and movement of mouse"""

        self.__set_project_name(project_name)
        self.__set_image_matrix_clean(image_matrix)
        self.__set_image_matrix_for_utility()
        self.__set_image_matrix_width()
        self.__init_tracking()


    def reset_image_crop(self):
        """Reset the cut and clean image for window"""

        self.__last_bottom = 0
        self.__position_window = 0
        self.__rectangle_area_coordinates.clear()
        self.__set_image_matrix_for_utility()
        self.__refresh_window_image()


    @property
    def rectangle_history_area_coordinates(self):
        """give the history of cuts coordinates"""

        return self.__get_side_of_rectangle('history_area_coordinates')


    @property
    def image_matrix_clean(self):
        """give the value of private intance"""

        return self.__image_matrix_clean


    @property
    def rectangle_area_coordinates(self):
        """give the value of private intance"""

        return self.__rectangle_area_coordinates


    @property
    def image_matrix_utility(self):
        """give the value of private intance"""

        return self.__image_matrix_utility


    @property
    def project_name(self):
        """give the value of private intance"""

        return self.__project_name


    @property
    def image_matrix_width(self):
        """give the value of private intance"""

        return self.__image_matrix_width


    @property
    def position_window(self):
        """give the value of private intance"""

        return self.__position_window


    @property
    def last_bottom(self):
        """give the value of private intance"""

        return self.__last_bottom