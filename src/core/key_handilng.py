import cv2

class KeyHandler:
    def __init__(self, editor_instance):
        self.editor = editor_instance
        self.bool_loop  = True
        self._init_loop()


    def _init_loop(self):
        while self.bool_loop:
            key = cv2.waitKey(12000)
            self._handle_key(key)


    def _handle_key(self, key):
        if key == ord('l'):
            self._clean_canva()

        elif key == 27:
            self._cancel_cutter()

        elif key == ord('s'):
            self._save_cuts()


    def _clean_canva(self):
        print('Presionaste la tecla "l"')


    def _cancel_cutter(self):
        print('Presionaste la tecla Esc (27)')
        self._break_loop()


    def _save_cuts(self):
        print('Presionaste la tecla "s"')
        self._break_loop()


    def _break_loop(self):
        self.bool_loop = False


