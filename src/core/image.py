from tkinter import messagebox as MessageBox
from core.mouse import MouseTracker
from tkinter import filedialog
import cv2
import os

class Editor:
    def __init__(self):
        self.path = ""
        self.name = ""
        self.img = None
        self.img_siz = (0, 0)
        self.pxl_save = []
        self.count = 0


    def cut_image(self):
        self.path = filedialog.askopenfilename()

        if not self.path:
            return

        self._select_name()
        self._handle_errors(self._rename_file)
        self._handle_errors(self._load_image)
        self._rename_file()
        self._load_image()
        self._show_image_info()
        self._show_image()
        self._set_mouse_callback()


    def _select_name(self):
        self.name = os.path.basename(os.path.dirname(self.path))


    def _rename_file(self):
        directory, filename = os.path.split(self.path)
        extension = os.path.splitext(filename)[1]
        new_path = os.path.join(directory, f"{self.name}{extension}")
        os.rename(self.path, new_path)
        self.path = new_path

    def _load_image(self):
        self.img = cv2.imread(self.path)
        self.img_siz = self.img.shape


    def _show_image_info(self):
        if self.img_siz[1] != 600:
            MessageBox.showwarning(
                "Tamaño",
                f"La altura es de: {self.img_siz[0]} y el ancho es de {self.img_siz[1]}"
            )


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