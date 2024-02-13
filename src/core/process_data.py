import os
from .directory_utils import rename_file


def process_img_path_name(handle_paths, handle_name):
    """set the name file, path file and name project"""

    handle_paths.process_img_path()
    handle_name.process_img_name()
    change_new_and_old_paths(handle_paths, handle_name)


def change_new_and_old_paths(handle_paths, handle_name):
    """change the img name for the project name"""

    patern_path = handle_paths.get_dir_parent_path()
    new_namefile = handle_name.set_new_name_for_rename_img()

    new_path = os.path.join(patern_path, new_namefile)
    old_path = handle_paths.get_image_file_path()

    rename_file(old_path=old_path, new_path=new_path)
    handle_paths.update_image_file_path(new_path)
