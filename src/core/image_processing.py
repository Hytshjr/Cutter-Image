from tkinter import messagebox as MessageBox
from core.mouse_tracker import MouseTracker
from tkinter import filedialog
import cv2
import os

class Editor:
    # Initialize the Editor
    def __init__(self):
        self.path = ""
        self.name = ""
        self.path_save = ""
        self.img = None


    def cut_image(self):
        # Main editor function ask and called functions
        self.path = filedialog.askopenfilename()

        if not self.path:
            return

        self._handle_errors(self._rename_file)
        self._handle_errors(self._load_image)
        self._show_image_info()
        self._show_image()
        self._set_mouse_callback()


    def _rename_file(self):
        # Rename file for avoid issues
        new_path = self._make_new_path()
        os.rename(self.path, new_path)
        self.path = new_path


    def _make_new_path(self):
        # Make and return the new path
        directory, filename = os.path.split(self.path)
        extnsn = os.path.splitext(filename)[1]

        self.path_save = directory
        self.name = os.path.basename(self.path_save)
        return os.path.join(directory, f"{self.name}{extnsn}")


    def _load_image(self):
        # Load the images for show later
        self.img = cv2.imread(self.path)


    def _show_image_info(self):
        if self.img.shape[1] != 600:
            width = self.img.shape[1]
            height = self.img.shape[0]

            MessageBox.showwarning(
                "Tamaño",
                f"La altura es de: {height} y el ancho es de {width}")


    def _show_image(self, img=None):
        if img is None:
            cv2.imshow(self.name, self.img)
        else:
            cv2.imshow(self.name, img)


    def _set_mouse_callback(self):
        tracker = MouseTracker(self)
        cv2.setMouseCallback(self.name, tracker.main_track)


    def _handle_errors(self, func):
        try:
            func()
        except FileNotFoundError as e:
            self._show_error(f"FileNotFoundError: {e}")
        except cv2.error as e:
            self._show_error(f"cv2.error: {e}")

    def _show_error(self, message):
        MessageBox.showwarning("Error", f"Error: {message}")