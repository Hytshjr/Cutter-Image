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
        # Set paths or dirs importans
        self.dir = Diretory()
        self.path = self.dir.path_img
        self.name = self.dir.name_img


    def _load_image(self):
        # Load the images for show later
        try:
            self.img = cv2.imread(self.path)
            self.width = self.img.shape[1]
            self.height = self.img.shape[0]
        except Exception as e:
            self._show_error(f"cv2.error: {e}")


    def _show_image_info(self):
        # Show if the image is out the size allowed
        if self.img.shape[1] != 600:
            message = f"Height: {self.height}, Width: {self.width}"
            self._show_error(message)


    def _show_image(self, img=None):
        # Show the image for user
        if img is None:
            cv2.imshow(self.name, self.img)
        else:
            cv2.imshow(self.name, img)


    def _set_mouse_callback(self):
        # Call tack mouse for cut the image
        self.tracker = MouseTracker(self)
        cv2.setMouseCallback(self.name, self.tracker.main_track)


    def _handle_key(self):
        # Call keyboard event for save or cancel the cuts
        KeyHandler(self)


    def _save_cuts(self):
        # Init the process for saves the cuts
        self._process_coords(self.tracker.cuts)
        self._cut_image_coords(self.top, self.bot, self.right)
        self.dir.set_dir_img()
        self._write_cuts()


    def _process_coords(self, coords):
        # Process and order the coords for the cuts
        coords = list(coords.values())
        unpacked_coords = [
            (coord[0][0], coord[0][1], coord[1:])
            for coord in coords
            ]
        self.top, self.bot, self.right = zip(*unpacked_coords)


    def _cut_image_coords(self, tops, bots, rights):
        # Set the variables with the coords for cut the image
        for top, bot, right in zip(tops, bots, rights):
            left = 0
            self._image_cutting(top, bot, left,right)


    def _image_cutting(self, top, bot, left,right):
        # Cut the image and save the matriz in a list
        if right[0] != self.width:
            right.append(self.width)

        for right in right:
            image_cutter = self.img[top:bot, left:right]
            self.save_imgs.append(image_cutter)
            left = right


    def _write_cuts(self):
        # Save the cuts like imgfiles
        num_cuts = len(self.save_imgs)
        paths = self.dir.set_filesnames(num_cuts, self.name)

        for path, cut in zip(paths, self.save_imgs):
            cv2.imwrite(path, cut)


    def _handle_errors(self, func):
        # Handle the error of functions
        try:
            func()
        except cv2.error as e:
            self._show_error(f"cv2.error: {e}")


    def _show_error(self, message):
        # Show the error of functions
        MessageBox.showwarning("Error", f"Error: {message}")