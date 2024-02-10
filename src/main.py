"""Module that init all app."""

import os
import tkinter as tk
from config import MEDIA_ROOT
from interface.views.main_window import Frame

class App:
    """Class calling to main window"""

    def __init__(self, main_window):
        self.root = main_window
        self._set_title_app()
        self._set_icon_app()
        self._add_elements()


    def _set_title_app(self):
        self.root.title("Image Cutter")


    def _set_icon_app(self):
        image_path = os.path.join(MEDIA_ROOT, 'images', 'fazil.png')
        icon = tk.PhotoImage(file=image_path)
        self.root.iconphoto(True, icon)


    def _add_elements(self):
        Frame(self.root)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()