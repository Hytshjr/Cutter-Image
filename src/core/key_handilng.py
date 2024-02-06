import cv2

class KeyHandler:
    def __init__(self, editor_instance):
        self.editor = editor_instance
        self.tracker = self.editor.tracker
        self.img = self.editor.img
        self.bool_loop  = True
        self._init_loop()


    def _init_loop(self):
        while self.bool_loop:
            key = cv2.waitKey(12000)
            self._handle_key(key)


    def _handle_key(self, key):
        if key == ord('l') or key == ord('L'):
            self._clean_img()

        elif key == 27:
            self._cancel_cutter()

        elif key == ord('s') or key == ord('S'):
            self._save_cuts()


    def _clean_img(self):
        self.tracker.save_cuts = []
        self.tracker.last_buttom = 0
        self.tracker.img = self.img.copy()
        self.editor._show_image(self.img)


    def _cancel_cutter(self):
        self._close_wnds()


    def _save_cuts(self):
        self.editor.save_cuts = self.tracker.cuts
        self._close_wnds()


    def _close_wnds(self):
        cv2.destroyAllWindows()
        self.bool_loop = False


