import os
from .exceptions import show_error


class ComponentsProject:
    """Class that handle the components the project"""
    def __init__(self, project_main_file):
        self.__project_main_file = project_main_file
        self.__project_dir_parent_path = None
        self.__project_format = None
        self.__project_name = None
        self.__set_project_dir_parent_path()
        self.__set_project_format()
        self.__set_project_name()


    @property
    def project_main_file(self):
        """give the value of private intance"""

        return self.__project_main_file

    @property
    def project_format(self):
        """give the value of private intance"""

        return self.__project_format


    @property
    def project_name(self):
        """give the value of private intance"""

        return self.__project_name


    @property
    def project_dir_parent_path(self):
        """give the value of private intance"""

        return self.__project_dir_parent_path


    def verify_path_exist(self, path):
        """Verify if the path exist"""

        if os.path.exists(path):
            return True

        return False


    def prepare_for_a_file_format(self, path_new_format_file):
        """prepare the class for some formatfile"""

        old_path = self.project_main_file
        new_path = path_new_format_file
        rename_file(old_path=old_path, new_path=new_path)

        self.update_project_main_file(path_new_format_file)


    def update_project_main_file(self, new_project_main_file):
        """update the main faile for a change path"""

        self.__project_main_file = new_project_main_file


    def __set_project_dir_parent_path(self):
        dir_path = os.path.dirname(self.__project_main_file)

        if self.verify_path_exist(dir_path):
            self.__project_dir_parent_path = dir_path


    def __set_project_format(self):
        extension = os.path.splitext(self.__project_main_file)[1]
        self.__project_format = extension


    def __set_project_name(self):
        parent_path = self.__project_dir_parent_path
        self.__project_name = os.path.basename(parent_path)



class ImageFile(ComponentsProject):
    """Representing a image file and components"""

    def __init__(self, project_main_file):
        super().__init__(project_main_file)
        self.__image_file_name = None
        self.__image_file_path = None
        self.__set_image_file_name()
        self.__set_image_file_path()


    @property
    def image_file_path(self):
        """give the value of private intance"""

        return self.__image_file_path


    @property
    def image_file_name(self):
        """give the value of private intance"""

        return self.__image_file_name


    def __set_image_file_name(self):
        image_name = self.project_name + self.project_format
        if image_name:
            self.__image_file_name = image_name


    def __set_image_file_path(self):
        image_file_path = self.__create_image_path()
        self.__image_file_path = image_file_path


    def __create_image_path(self):
        parent_dir_path = self.project_dir_parent_path
        image_file_name = self.image_file_name

        return os.path.join(parent_dir_path, image_file_name)



class HtmlFile(ComponentsProject):
    """Representing a image file and components"""

    def __init__(self, project_main_file):
        super().__init__(project_main_file)
        self.__html_file_name = None
        self.__html_file_path = None
        self.__set_html_file_name()
        self.__set_html_file_path()


    @property
    def html_file_path(self):
        """give the value of private intance"""

        return self.__html_file_path


    @property
    def html_file_name(self):
        """give the value of private intance"""

        return self.__html_file_name


    def __set_html_file_name(self):
        html_name = self.project_name + '.html'
        self.__html_file_name = html_name


    def __set_html_file_path(self):
        html_file_path = self.__create_image_path()
        self.__html_file_path = html_file_path


    def __create_image_path(self):
        parent_dir_path = self.project_dir_parent_path
        html_file_name = self.html_file_name

        return os.path.join(parent_dir_path, html_file_name)



def rename_file(old_path, new_path):
    """Rename the files"""
    try:
        os.rename(old_path, new_path)
    except ImportError as e:
        show_error(e)
