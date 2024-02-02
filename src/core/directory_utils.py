from tkinter.filedialog import askopenfilename
from tkinter import messagebox as MessageBox
import os

class Diretory:
    def __init__(self):
        self.path_img = ""
        self.name_img = ""
        self.dir_base = ""
        self.dir_imgs = ""
        self.dir_compress = ""
        self.bool_cancel = True
        self._select_and_rename()


    def _select_and_rename(self):
        path_img = askopenfilename()
        self._verification(path_img)
        if self.bool_cancel :
            return

        self._make_new_path(path_img)
        self._rename_file(path_img)


    def _verification(self, path_img):
        extension = path_img[-3:]
        extension_list = ["png", "jpg"]
        format_bool = extension in extension_list

        if format_bool and path_img:
            self.extension = extension
            self.bool_cancel = False


    def _make_new_path(self, path_img):
            directory, filename = os.path.split(path_img)
            self._make_name(directory, filename)
            self.path_img = os.path.join(directory, self.name_img)


    def _make_name(self, directory, filename):
            extension = os.path.splitext(filename)[1]
            new_name = os.path.basename(directory)
            self.name_img = new_name + extension


    def _rename_file(self, path_img):
        try:
            os.rename(path_img, self.path_img)
            self.dir_base = os.path.dirname(self.path_img)
        except Exception as e:
            self._show_error(e)


    def _show_error(self, message):
        MessageBox.showwarning("Error", f"Error: {message}")


    def set_dir_img(self):
        self.dir_imgs = os.path.join(self.dir_base, 'images')
        self._create_dir(self.dir_imgs)



    def _create_dir(self, dir_create):
        if not os.path.exists(dir_create):
            os.makedirs(dir_create)