import cv2

class MouseTracker:
    def __init__(self, editor_instance):
        # Initialize the MouseTracker with an Editor instance
        self.editor = editor_instance
        self.img = self.editor.img
        self.width = self.img.shape[1]
        self.img_pos = 0
        self.last_top = 0
        self.last_left = 0
        self.coords = {}
        self.save_pxl = []


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


    def _handle_left_click_event(self, eje_y):
        # Handle left mouse button click event
        self._set_rctngl_size(eje_y, self.width, 0)
        self._create_rectangle()
        self._set_coords(eje_y, self.width)
        self._save_pxl()


    def _handle_right_click_event(self, eje_y, eje_x):
        # Handle right mouse button click event
        self._set_rctngl_size(eje_y, eje_x, self.last_left)
        self._create_rectangle()
        self._set_coords(eje_y, eje_x)
        self._save_pxl()


    def _set_rctngl_size(self, crd_bot, crd_right, crd_left):
        # Set rectangle size based on mouse position
        self._set_widht_rctngl(crd_right, crd_left)
        self._set_hight_rctngl(crd_bot)
        self._set_size_rctngl()


    def _set_widht_rctngl(self, crd_right, crd_left):
        self.line_ritght = crd_right
        self.line_left = crd_left

        self.last_left = self.line_ritght



    def _set_hight_rctngl(self, crd_bot):
        self.line_top = self.last_top
        self.line_bottom = crd_bot+self.img_pos

        if self.line_bottom < self.line_top:
            self.line_bottom = self.last_top
            self.line_top =  self.last_bot

        self.last_top = self.line_bottom
        self.last_bot = self.line_top


    def _set_size_rctngl(self):
        left_bot = (self.line_left, self.line_bottom)
        right_top = (self.line_ritght, self.line_top)

        self.coords['line_bot_left'] = left_bot
        self.coords['line_top_rght'] = right_top


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


    def _set_coords(self, eje_y, width):
        # Sets the coordinates for the pixel to be saved.
        self.coords['save_top'] = self.last_top
        self.coords['save_bottom'] = eje_y+self.img_pos
        self.coords['save_mid'] = width


    def _save_pxl(self):
        # Save the coordinates of the rectangle for save images
        self.save_pxl.append(
            (self.coords['save_top'],
            self.coords['save_bottom'],
            self.coords['save_mid']))






