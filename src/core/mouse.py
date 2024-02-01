import cv2

class MouseTracker:
    def __init__(self, editor_instance):
        # Initialize the MouseTracker with an Editor instance
        self.editor = editor_instance
        self.img = self.editor.img
        self.width = self.img.shape[1]
        self.height = self.img.shape[0]
        self.img_pos = 0
        self.last_height = 0
        self.coords = {}
        self.save_pxl = []


    def main_track(self, event, eje_x, eje_y, flags, param):
        # Main tracking function called on mouse events
        if event == cv2.EVENT_MOUSEWHEEL:
            self._handle_scroll_event(flags)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self._handle_click_event(eje_y)


    def _handle_scroll_event(self, flags):
        # Handle mouse wheel scrolling event
        scroll_amount = 50 if flags < 0 else -50
        self.img_pos += scroll_amount
        self._show_image(self.img_pos, self.img)


    def _handle_click_event(self, eje_y):
        # Handle left mouse button click event
        self._rect_pts(eje_y)
        self._set_coords(eje_y)
        self._create_rectangle()
        self._show_image(self.img_pos, self.img)
        self._save_pxl()
        self._last_height()


    def _rect_pts(self, eje_y):
        # Set rectangle points based on mouse position
        if self.img_pos == 0:
            self.coords['height'] = (0,eje_y)
        else:
            self.coords['height'] = (0,eje_y+self.img_pos)


    def _set_coords(self, eje_y):
        # Set coordinates for the rectangle and save for later use
        self.coords['witdh'] = (self.width,self.last_height)
        self.coords['top_rtngl'] = self.last_height
        self.coords['bottom_rtngl'] = eje_y+self.img_pos


    def _create_rectangle(self):
        # Create a green rectangle on the image
        color = (0, 255, 0)
        cv2.rectangle(
            self.img, self.coords['height'],
            self.coords['witdh'], color)


    def _show_image(self, position, img):
        # Show a portion of the image based on the current position
        pos_top = position
        pos_bottom = position + 1080
        self.editor._show_image(img[pos_top:pos_bottom:])


    def _save_pxl(self):
        # Save the coordinates of the rectangle for save images
        self.save_pxl.append(
            (self.coords['top_rtngl'],
            self.coords['bottom_rtngl']))


    def _last_height(self):
        # Save the last height for future reference
        self.last_height = self.coords['height'][1]





