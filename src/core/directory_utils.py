from tkinter.filedialog import askopenfilename
import os

class Diretory:
    def __init__(self):
        self.path_img = ""
        self.path_main = ""
        self.name_img = ""
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
        extension_list = ["png", "gjpg"]
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
            self.path_main = os.path.dirname(self.path_img)
        except Exception as e:
            print(f"Error renaming file: {e}")