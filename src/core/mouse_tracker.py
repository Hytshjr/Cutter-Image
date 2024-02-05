import cv2

class MouseTracker:
    def __init__(self, editor_instance):
        # Initialize the MouseTracker with an Editor instance
        self.editor = editor_instance
        self.img = self.editor.img.copy()
        self.width = self.img.shape[1]
        self.img_pos = 0
        self.last_bottom = 0
        self.save_cuts = []
        self.cuts = {}


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
        self._set_coords_area(click_y, self.width)


    def _handle_right_click_event(self, click_y, click_x):
        # Handle right mouse button click event
        self._set_coords_area(click_y, click_x)


    def _set_coords_area(self, click_y, click_x):
        # Set rectangle size based on mouse position
        if self._is_click_out_area(click_y):
            self._set_hight_area(click_y)
        self._set_widht_area(click_x)
        self._set_size_rctngl()


    def _set_hight_area(self, click_y):
        # Set variables if the click is outside of rectangle
        self.line_top = self.last_bottom
        self.line_bottom = click_y + self.img_pos
        self.last_bottom = self.line_bottom
        self._set_new_cut_area()


    def _set_widht_area(self, click_x):
        # Set rectangle widht based on mouse position
        self.line_left = 0
        self.line_right = click_x
        self.cuts[self.line_top].append(click_x)


    def _is_click_out_area(self, click_y):
        rctngl_bottom = self.last_bottom
        click_position = click_y + self.img_pos

        if click_position > rctngl_bottom:
            return True


    def _set_new_cut_area(self):
        if self.line_top  not in self.cuts:
            self.cuts[self.line_top] = []

        height_cut = (self.line_top, self.line_bottom)
        self.cuts[self.line_top].append(height_cut)


    def _set_size_rctngl(self):
        # Set rectangle size on a dict
        right_bot = (self.line_right, self.line_bottom)
        left_top = (self.line_left, self.line_top)
        coords = {}

        coords['line_right_bot'] = right_bot
        coords['line_left_top'] = left_top
        self._create_rectangle(coords)


    def _create_rectangle(self, coords):
        # Create a green rectangle on the image
        color = (251, 0, 255)
        cv2.rectangle(
            self.img, coords['line_right_bot'],
            coords['line_left_top'], color)

        self._show_image(self.img_pos, self.img)


    def _show_image(self, position, img):
        # Show a portion of the image based on the current position
        pos_top = position
        pos_bottom = position + 1080
        self.editor._show_image(img[pos_top:pos_bottom:])