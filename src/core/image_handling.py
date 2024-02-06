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

        import os

        list_cuts = list(cuts.values())
        self.dir_imgs = self.dir.dir_imgs

        filename, extension = os.path.splitext(self.name)


        top = []
        bottom = []
        verticals = []
        count = 0

        for cut in list_cuts:
            top.append(cut[0][0])
            bottom.append(cut[0][1])
            verticals.append(cut[1:])

        for index, vertical in enumerate(verticals):

            if vertical[0] == 600:
                count += 1
                new_name = f"{filename}_{count}{extension}"
                name = os.path.join(self.dir_imgs, new_name)
                image_cutter = self.img[top[index]:bottom[index], 0:vertical[0]]
                cv2.imwrite(name, image_cutter)
                print(name)

            else:
                left = 0
                vertical.append(600)

                for right in vertical:
                    count += 1
                    new_name = f"{filename}_{count}{extension}"
                    name = os.path.join(self.dir_imgs, new_name)
                    image_cutter = self.img[top[index]:bottom[index], left:right]
                    cv2.imwrite(name, image_cutter)
                    left = right
                    print(name)




    def _handle_errors(self, func):
        try:
            func()
        except cv2.error as e:
            self._show_error(f"cv2.error: {e}")


    def _show_error(self, message):
        MessageBox.showwarning("Error", f"Error: {message}")