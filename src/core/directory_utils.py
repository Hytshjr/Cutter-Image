import os
from .exceptions import show_error


class HandlePaths:
    """Handle the paths of files and directories"""

    def __init__(self):
        self.images_files_paths_for_cuts = []
        self.dir_compress_path = None
        self.dir_parent_path = None
        self.image_file_path = None
        self.dir_cuts_path = None


    def _set_image_file_path(self, file_path):
        self.image_file_path = file_path


    def _set_dir_parent_path(self):
        dir_parent_path = os.path.dirname(self.image_file_path)
        self.dir_parent_path = dir_parent_path


    def _set_dir_cuts_path(self):
        dir_cuts_path = self._create_dir_path('images')
        self.dir_cuts_path = dir_cuts_path


    def _set_dir_compress_path(self):
        dir_compress_path = self._create_dir_path('compress')
        self.dir_compress_path = dir_compress_path


    def _create_dir_path(self, directory):
        return os.path.join(self.dir_parent_path, directory)


    def process_img_path(self, file_path):
        """Call method for process the path and utils"""

        self._set_image_file_path(file_path)
        self._set_dir_parent_path()
        self._set_dir_cuts_path()
        self._set_dir_compress_path()


    def get_file_path(self):
        return self.image_file_path


    def get_dir_parent_path(self):
        return self.dir_parent_path


    def get_dir_cuts_path(self):
        return self.dir_cuts_path


    def get_dir_compress_path(self):
        return self.dir_compress_path


    def update_image_file_path(self, new_image_path):
        self.image_file_path = new_image_path


    def get_images_files_paths_for_cuts(self, files_names):
        """Create the paths for the cuts of img"""

        self.images_files_paths_for_cuts = [
            os.path.join(self.dir_cuts_path, file_name)
            for file_name in files_names
            ]

        return self.images_files_paths_for_cuts



class HandleNameFile:
    """Handle name of file"""
    def __init__(self, path_instance):
        self.path_instance = path_instance
        self.image_extension = None
        self.names_for_cuts = None
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


    def get_names_for_cuts(self, cuts_quantity):
        """Return the names for cuts of img"""

        return self._create_names_for_cuts(cuts_quantity)


    def _create_names_for_cuts(self, cuts_quantity):
        img_name = self.project_name
        img_extension = self.image_extension
        names_files_img_cut = []

        for cut_number in range(cuts_quantity):
            cut_number_file = cut_number + 1
            name_img_cut = f"{img_name}_{cut_number_file}"
            name_file_img_cut = name_img_cut + img_extension
            names_files_img_cut.append(name_file_img_cut)

        return names_files_img_cut



def rename_file(old_path, new_path):
    """Rename the files"""
    try:
        os.rename(old_path, new_path)
    except ImportError as e:
        show_error(e)