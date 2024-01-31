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
        new_path = os.path.join(directory, self.name + extension)


        try:
            os.rename(self.path, new_path)
            self.path = new_path
        except Exception as e:
            MessageBox.showwarning(
                "Error",
                f"Error al renombrar el archivo: {e}")


    def _load_image(self):
        try:
            self.img = cv2.imread(self.path)
            self.img_siz = self.img.shape
        except Exception as e:
            MessageBox.showwarning(
                "Error",
                f"Error loading image: {e}")


    def _show_image_info(self):
        if self.img_siz[1] != 600:
            MessageBox.showwarning(
                "Tamaño",
                f"La altura es de: {self.img_siz[0]} y el ancho es de {self.img_siz[1]}"
            )


    def _show_image(self):
        cv2.imshow(self.name, self.img)


    def _set_mouse_callback(self):
        tracker = MouseTracker(self.img, self.name)
        cv2.setMouseCallback(self.name, tracker.main_track)
