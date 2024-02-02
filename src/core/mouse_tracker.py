import cv2

class MouseTracker:
    def __init__(self, editor_instance):
        # Initialize the MouseTracker with an Editor instance
        self.editor = editor_instance
        self.img = self.editor.img.copy()
        self.width = self.img.shape[1]
        self.img_pos = 0
        self.last_buttom = 0
        self.coords = {}
        self.save_pxl = []
        self.coords_lelt = []


    def main_track(self, event, eje_x, eje_y, flags, param):
        # Main tracking function called on mouse events
        if event == cv2.EVENT_MOUSEWHEEL:
            self._handle_scroll_event(flags)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self._handle_left_click_event(eje_y)
        elif event == cv2.EVENT_RBUTTONDOWN:
            self._handle_right_click_event(eje_y, eje_x)


    def _handle_scroll_event(self, flags):
        # Handle mouse wheel scrolling event
        scroll_amount = 50 if flags < 0 else -50
        self.img_pos += scroll_amount
        self._show_image(self.img_pos, self.img)


    def _handle_left_click_event(self, click_y):
        # Handle left mouse button click event
        self._set_rctngl_size(click_y, self.width)
        self._create_rectangle()


    def _handle_right_click_event(self, click_y, click_x):
        # Handle right mouse button click event
        self._set_rctngl_size(click_y, click_x)
        self._create_rectangle()


    def _set_rctngl_size(self, click_y, click_x):
        # Set rectangle size based on mouse position
        self._set_widht_rctngl(click_x)
        self._set_hight_rctngl(click_y)
        self._set_size_rctngl()


    def _set_widht_rctngl(self, click_x):
        # Set rectangle widht based on mouse position
        self.line_left = 0
        self.line_right = click_x


    def _set_hight_rctngl(self, click_y):
        # Set hight widht based on mouse position
        rctngl_buttom = self.last_buttom
        click_position = click_y + self.img_pos

        if click_position > rctngl_buttom:
            self.line_top = self.last_buttom
            self.line_bottom = click_y + self.img_pos
            self.last_buttom = self.line_bottom


    def _set_size_rctngl(self):
        # Set rectangle size on a dict
        right_bot = (self.line_right, self.line_bottom)
        left_top = (self.line_left, self.line_top)

        self.coords['line_bot_left'] = right_bot
        self.coords['line_top_rght'] = left_top
        self._save_pxl()


    def _create_rectangle(self):
        # Create a green rectangle on the image
        color = (0, 255, 0)
        cv2.rectangle(
            self.img, self.coords['line_bot_left'],
            self.coords['line_top_rght'], color)

        self._show_image(self.img_pos, self.img)


    def _show_image(self, position, img):
        # Show a portion of the image based on the current position
        pos_top = position
        pos_bottom = position + 1080
        self.editor._show_image(img[pos_top:pos_bottom:])


    def _save_pxl(self):
        # Save the coordinates of the rectangle for save images
        self.save_pxl.append((self.line_top,
                            self.line_bottom, self.line_right))