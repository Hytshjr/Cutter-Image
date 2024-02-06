import cv2

class KeyHandler:
    def __init__(self, editor_instance):
        # Init the loop for recieve the envents
        self.editor = editor_instance
        self.tracker = self.editor.tracker
        self.img = self.editor.img
        self.bool_loop  = True
        self._init_loop()


    def _init_loop(self):
        # Set the loop
        while self.bool_loop:
            key = cv2.waitKey(12000)
            self._handle_key(key)


    def _handle_key(self, key):
        # Verify what event is
        if key == ord('l') or key == ord('L'):
            self._clean_img()

        elif key == 27:
            self._cancel_cutter()

        elif key == ord('s') or key == ord('S'):
            self._save_cuts()


    def _clean_img(self):
        # Clean the image for new cuts
        self.tracker.last_bottom = 0
        self.tracker.img_pos = 0
        self.tracker.img = self.img.copy()
        self.editor._show_image(self.img)


    def _cancel_cutter(self):
        # Cancel and close the windows for the cuts
        self._close_wnds()


    def _save_cuts(self):
        # Init the save the cuts
        self._close_wnds()
        self.editor.save_imgs = []
        self.editor.save_cuts(self.tracker.cuts)


    def _close_wnds(self):
        # Close the windows that show the image
        cv2.destroyAllWindows()
        self.bool_loop = False


