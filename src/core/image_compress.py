"""The class for compress images"""
# pylint: disable=no-member

import os
import glob
from decouple import config
import tinify

class CompressImage:
    """The class for compress images"""

    def __init__(self):
        self.__api_key = config('API_KEY')
        self.__dir_name_to_compress = None


    def __make_dir_for_save_compress(self, dir_to_compress):
        try:
            dir_name = self.__dir_name_to_compress
            os.mkdir(dir_to_compress.replace(dir_name, 'compress'))
        except FileExistsError:
            pass


    def __set_dir_name_to_compress(self, dir_to_compress):
        self.__dir_name_to_compress = os.path.basename(dir_to_compress)


    def __set_api_to_tinify(self):
        tinify.key = self.__api_key


    def __make_new_path(self, image_to_compress):
        image_to_compress_items = os.path.splitext(image_to_compress)
        image_path = image_to_compress_items[0] + '_compressed'
        extension_image = image_to_compress_items[1]
        return image_path + extension_image


    def __compress_images(self, image_to_compress):
        save_compressed_image = self.__make_new_path(image_to_compress)
        image_compressed = tinify.from_file(image_to_compress)
        image_compressed.to_file(save_compressed_image)


    def __compress_images_with_dir(self, dir_to_compress):
        dir_name = self.__dir_name_to_compress

        images_to_compress = glob.glob(dir_to_compress + '\\*')
        for image in images_to_compress:
            save_compressed_image = image.replace(dir_name, 'compress')
            image_compressed = tinify.from_file(image)
            image_compressed.to_file(save_compressed_image)


    def compress_images_directory(self, dir_to_compress):
        """Compress all images from a directory"""

        self.__set_dir_name_to_compress(dir_to_compress)
        self.__make_dir_for_save_compress(dir_to_compress)
        self.__set_api_to_tinify()
        self.__compress_images_with_dir(dir_to_compress)


    def compress_image(self, image_to_compress):
        """Compress the image that user select"""

        self.__set_api_to_tinify()
        self.__compress_images(image_to_compress)
