from tkinter import messagebox as MessageBox
from core.mouse_tracker import MouseTracker
from core.directory_utils import Diretory
from core.key_handilng import KeyHandler
from tkinter import filedialog
import cv2
import os

class Editor:
    # Initialize the Editor
    def __init__(self):
        self.path = ""
        self.name = ""
        self.img = None
        self.save_cuts = []


    def cut_image(self):
        # Main editor function ask and called functions
        self._set_paths()

        if not self.path:
            return

        self._handle_errors(self._load_image)
        self._show_image_info()
        self._show_image()
        self._set_mouse_callback()
        self._handle_key()

    def _set_paths(self):
        self.dir = Diretory()
        self.path = self.dir.path_img
        self.name = self.dir.name_img


    def _load_image(self):
        # Load the images for show later
        self.img = cv2.imread(self.path)


    def _show_image_info(self):
        if self.img.shape[1] != 600:
            width = self.img.shape[1]
            height = self.img.shape[0]

            MessageBox.showwarning(
                "Tamaño",
                f"Height: {height}, Width: {width}")


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


    def _handle_errors(self, func):
        try:
            func()
        except cv2.error as e:
            self._show_error(f"cv2.error: {e}")

    def _show_error(self, message):
        MessageBox.showwarning("Error", f"Error: {message}")