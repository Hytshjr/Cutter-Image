from tkinter.filedialog import askopenfilename
# from tkinter import messagebox as MessageBox
import os


class HandlePaths:
    """Handle the paths of files and directories"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.dir_parent_path = str
        self.dir_cuts_path = str
        self.dir_compress_path = str
        self._set_dir_parent_path()
        self._set_dir_cuts_path()
        self._set_dir_compress_path()


    def _set_dir_parent_path(self):
        dir_parent_path = os.path.dirname(self.file_path)
        self.dir_parent_path = dir_parent_path


    def _set_dir_cuts_path(self):
        dir_cuts_path = self._create_dir_path( 'images')
        self.dir_cuts_path = dir_cuts_path


    def _set_dir_compress_path(self):
        dir_compress_path = self._create_dir_path( 'compress')
        self.dir_compress_path = dir_compress_path


    def _create_dir_path(self, directory):
        return os.path.join(self.dir_parent_path, directory)


    def get_file_path(self):
        return self.file_path


    def get_dir_parent_path(self):
        return self.dir_parent_path


    def get_dir_cuts_path(self):
        return self.dir_cuts_path


    def get_dir_compress_path(self):
        return self.dir_compress_path


    def update_file_path(self, new_path):
        self.file_path = new_path



class HandleNameFile:
    """Handle name of file"""
    def __init__(self, path_instance):
        self.path_instance = path_instance
        self.image_extension = None
        self.project_name = None
        self.image_name = None
        self.html_name = None
        self._set_image_extension()
        self._set_project_name()
        self._set_image_name()
        self._set_html_name()


    def _set_image_extension(self):
        file_path = self.path_instance.get_file_path()
        self.image_extension = os.path.splitext(file_path)[1]


    def _set_project_name(self):
        parent_path = self.path_instance.get_dir_parent_path()
        self.project_name = os.path.basename(parent_path)


    def _set_image_name(self):
        if self.project_name is None:
            self.html_name = f'Name not found{self.image_extension}'
            return

        self.image_name = self.project_name +  self.image_extension


    def _set_html_name(self):
        if self.project_name is None:
            self.html_name  = 'Name File not found.html'
            return

        self.html_name = self.project_name + '.html'


    def get_project_name(self):
        return self.project_name


    def get_image_name(self):
        return self.image_name


    def get_html_name(self):
        return self.html_name


    def get_image_extension(self):
        return  self.image_extension



def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
    except ImportError as e:
        print(e)

def run ():
    """func MAIN"""

    file_path = askopenfilename()
    hanlde_path = HandlePaths(file_path)
    handle_name = HandleNameFile(hanlde_path)
    old_path = hanlde_path.get_file_path()
    new_filename = handle_name.get_image_name()
    dir_parent_path = hanlde_path.get_dir_parent_path()
    new_path = os.path.join(dir_parent_path, new_filename)

    rename_file(old_path, new_path)

    hanlde_path.update_file_path(new_path)




if __name__ == '__main__':
    run()

    # def set_dir_img(self):
    #     """Create dir for the cuts of img"""

    #     self.dir_imgs = os.path.join(self.dir_base, 'images')
    #     self._create_dir(self.dir_imgs)


# class Diretory:
#     """Class for configure the path img and names"""

#     def __init__(self):
#         self.path_img = str
#         self.name_img = str
#         self.dir_base = str
#         self.dir_imgs = str
#          self.image_extension = str
#         self.dir_compress = str
#         self.bool_cancel = True
#          self.image_extension_list = [".png", ".jpg"]


#     def select_rename_path_main(self):
#         """Method for call all main funcs"""
#         path_img = askopenfilename()
#         self._verification(path_img)
#         if self.bool_cancel:
#             return
#         self._rename_img(path_img)


#     def _verification(self, path_img):
#          self.image_extension = path_img[-4:]
#         format_bool =  self.image_extension  in   self.image_extension_list
#         self._set_bool_cancel(format_bool, path_img)


#     def _set_bool_cancel(self, format_bool, path_img):
#         if format_bool and path_img:
#             self.bool_cancel = False
#         else:
#             self.bool_cancel = True


#     def _rename_img(self, path_img):
#         self._make_new_path(path_img)
#         self._rename_file(path_img)


#     def _make_new_path(self, path_img):
#         directory = os.path.split(path_img)[0]
#         self._make_name(directory)
#         self.path_img = os.path.join(directory, self.name_img)


#     def _make_name(self, directory):
#         new_name = os.path.basename(directory)
#         self.name_img = new_name +  self.image_extension


#     def _rename_file(self, path_img):
#         try:
#             os.rename(path_img, self.path_img)
#             self.dir_base = os.path.dirname(self.path_img)
#         except ImportError as e:
#             self._show_error(e)


#     def _show_error(self, message):
#         MessageBox.showwarning("Error", f"Error: {message}")


#     def set_dir_img(self):
#         """Create dir for the cuts of img"""

#         self.dir_imgs = os.path.join(self.dir_base, 'images')
#         self._create_dir(self.dir_imgs)


#     def _create_dir(self, dir_create):
#         if not os.path.exists(dir_create):
#             os.makedirs(dir_create)


#     def set_filesnames(self, quantity, name):
#         """Create the names for the cuts"""

#         filename, extension = os.path.splitext(name)
#         new_names = self._set_names(filename, extension, quantity)
#         paths = self._set_paths(new_names)
#         return paths


#     def _set_names(self, filename, extension, quantity):
#         name = [
#             f"{filename}_{num+1}{extension}"
#             for num in range(quantity)
#             ]
#         return name


#     def _set_paths(self, new_names):
#         paths = [
#             os.path.join(self.dir_imgs, new_name)
#             for new_name in new_names
#             ]
#         return paths


