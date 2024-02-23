import os
from .exceptions import show_error


class ComponentsProject:
    """Class that handle the components the project"""
    def __init__(self, project_main_file_path):
        self.__project_main_file_path = project_main_file_path
        self.__project_dir_parent_path = None
        self.__project_format = None
        self.__project_name = None
        self.__set_project_dir_parent_path()
        self.__set_project_format()
        self.__set_project_name()


    @property
    def project_main_file_path(self):
        """give the value of private intance"""

        return self.__project_main_file_path

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


    def update_project_main_file_path(self, new_project_main_file_path):
        """update the main faile for a change path"""

        self.__project_main_file_path = new_project_main_file_path


    def __set_project_dir_parent_path(self):
        dir_path = os.path.dirname(self.__project_main_file_path)

        if self.verify_path_exist(dir_path):
            self.__project_dir_parent_path = dir_path


    def __set_project_format(self):
        extension = os.path.splitext(self.__project_main_file_path)[1]
        self.__project_format = extension


    def __set_project_name(self):
        parent_path = self.project_dir_parent_path
        self.__project_name = os.path.basename(parent_path)



class ImageFile(ComponentsProject):
    """Representing a image file and components"""

    def __init__(self, project_main_file_path):
        super().__init__(project_main_file_path)
        self.__dir_path_save_image_cuts = None
        self.__image_file_path = self.project_main_file_path
        self.__image_file_name = None
        self.__set_image_file_name()
        self.__set__dir_path_save_image_cuts()


    @property
    def dir_path_save_image_cuts(self):
        """give the value of private intance"""

        return self.__dir_path_save_image_cuts


    @property
    def image_file_path(self):
        """give the value of private intance"""

        return self.__image_file_path


    @property
    def image_file_name(self):
        """give the value of private intance"""

        return self.__image_file_name


    def init_env_project(self):
        """init the enviorement for work a dir project"""

        try:
            new_path = self.__rename_image_file()
        except FileNotFoundError as error:
            note_user = "Can't create enviroment for project"
            show_error(error, note_user)
        else:
            self.update_project_main_file_path(new_path)
            self.__image_file_name = self.project_name
            self.__image_file_path = new_path


    def gen_path_image_cuts(self, amount_image_cuts):
        """generate the paths for save the image cuts"""

        self.__make_dir_for_save_image_cuts()
        image_cuts_paths = []
        for image_cut_number in range(1, amount_image_cuts+1):
            image_cut_name = self.__make_file_name(image_cut_number)
            image_cut_path = self.__make_file_path(image_cut_name)
            image_cuts_paths.append(image_cut_path)

        return image_cuts_paths


    def __set_image_file_name(self):
        os.path.split(self.__image_file_path)
        image_file_name = os.path.split(self.__image_file_path)[1]
        image_name = os.path.splitext(image_file_name)[0]

        if image_file_name:
            self.__image_file_name = image_name


    def __set__dir_path_save_image_cuts(self):
        name_dir = (self.project_dir_parent_path, 'image')
        self.__dir_path_save_image_cuts = os.path.join(*name_dir)


    def __make_dir_for_save_image_cuts(self):
        try:
            os.mkdir(self.__dir_path_save_image_cuts)
        except FileExistsError:
            pass


    def __make_file_name(self, cut_number):
        project_name = self.image_file_name
        project_format = self.project_format
        return f'{project_name}_{cut_number}{project_format}'


    def __make_file_path(self, file_name):
        return os.path.join(self.dir_path_save_image_cuts, file_name)


    def __create_env_file_image_path(self):
        parent_dir_path = self.project_dir_parent_path
        image_file_name = self.project_name + self.project_format

        return os.path.join(parent_dir_path, image_file_name)


    def __rename_image_file(self):
        old_path = self.image_file_path
        new_path = self.__create_env_file_image_path()
        rename_file(old_path=old_path, new_path=new_path)
        return new_path



class HtmlFile(ComponentsProject):
    """Representing a image file and components"""

    def __init__(self, project_main_file_path):
        super().__init__(project_main_file_path)
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
        html_file_path = self.__create_file_image_path()
        self.__html_file_path = html_file_path


    def __create_file_image_path(self):
        parent_dir_path = self.project_dir_parent_path
        html_file_name = self.html_file_name

        return os.path.join(parent_dir_path, html_file_name)



def rename_file(old_path, new_path):
    """Rename the files"""
    try:
        os.rename(old_path, new_path)
    except ImportError as e:
        show_error(e)
