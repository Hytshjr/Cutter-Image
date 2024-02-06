from tkinter import messagebox as MessageBox
from core.mouse_tracker import MouseTracker
from core.directory_utils import Diretory
from core.key_handilng import KeyHandler
import cv2

class Editor:
    # Initialize the Editor
    def __init__(self):
        self.dir_imgs = ""
        self.path = ""
        self.name = ""
        self.img = ""
        self.save_cuts = []
        self.save_imgs = []



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
        self._process_coords(self.tracker.cuts)
        self._cut_image_coords(self.top, self.bot, self.right)
        self._write_cuts()


    def _process_coords(self, coords):
        coords = list(coords.values())
        unpacked_coords = [
            (coord[0][0], coord[0][1], coord[1:])
            for coord in coords
            ]
        self.top, self.bot, self.right = zip(*unpacked_coords)


    def _cut_image_coords(self, tops, bots, rights):
        for top, bot, right in zip(tops, bots, rights):
            self._image_cutting(top, bot, right)


    def _image_cutting(self, top, bot, right):
        left = 0
        if right[0] != 600:
            right.append(600)

        for right in right:
            image_cutter = self.img[top:bot, left:right]
            self.save_imgs.append(image_cutter)
            left = right


    def _write_cuts(self):
        self.dir.set_dir_img()
        import os
        self.dir_imgs = self.dir.dir_imgs
        filename, extension = os.path.splitext(self.name)
        for i ,cut in enumerate(self.save_imgs):
            new_name = f"{filename}_{i}{extension}"
            name = os.path.join(self.dir_imgs, new_name)
            cv2.imwrite(name, cut)


    def _handle_errors(self, func):
        try:
            func()
        except cv2.error as e:
            self._show_error(f"cv2.error: {e}")


    def _show_error(self, message):
        MessageBox.showwarning("Error", f"Error: {message}")