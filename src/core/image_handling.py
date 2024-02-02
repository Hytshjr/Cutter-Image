from tkinter import messagebox as MessageBox
from core.mouse_tracker import MouseTracker
from core.directory_utils import Diretory
from core.key_handilng import KeyHandler
import cv2

class Editor:
    # Initialize the Editor
    def __init__(self):
        self.path = ""
        self.name = ""
        self.img = ""
        self.save_cuts = []


    def cut_image(self):
        # Main editor function ask and called functions
        self._set_paths()
        if not self.path:
            return
        self._load_image()
        self._show_image_info()
        self._show_image()
        self._set_mouse_callback()
        self._handle_key()
        self._save_cuts()


    def _set_paths(self):
        self.dir = Diretory()
        self.path = self.dir.path_img
        self.name = self.dir.name_img


    def _load_image(self):
        # Load the images for show later
        try:
            self.img = cv2.imread(self.path)
        except Exception as e:
            self._show_error(f"cv2.error: {e}")


    def _show_image_info(self):
        if self.img.shape[1] != 600:
            width = self.img.shape[1]
            height = self.img.shape[0]
            message = f"Height: {height}, Width: {width}"
            self._show_error(message)


    def _show_image(self, img=None):
        if img is None:
            cv2.imshow(self.name, self.img)
        else:
            cv2.imshow(self.name, img)


    def _set_mouse_callback(self):
        self.tracker = MouseTracker(self)
        cv2.setMouseCallback(self.name, self.tracker.main_track)


    def _handle_key(self):
        KeyHandler(self)

    def _save_cuts(self):
        self.dir.set_dir_img()
        self._process_cuts(self.save_cuts)


    def _process_cuts(self, cuts):
        list_test = []
        for i in range(len(cuts)):
            if i < len(cuts)-1:
                if cuts[i][2] == 600:
                    list_test = []
                else:
                    if cuts[i][0]==cuts[i+1][0]:
                        list_test.append(cuts[i][2])
                        list_test.append(cuts[i+1][2])

                        print(cuts[i], cuts[i+1])


        print('last:',list_test)


    def _handle_errors(self, func):
        try:
            func()
        except cv2.error as e:
            self._show_error(f"cv2.error: {e}")

    def _show_error(self, message):
        MessageBox.showwarning("Error", f"Error: {message}")