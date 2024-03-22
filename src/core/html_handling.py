# pylint: disable=import-error

import os
from jinja2 import Environment, FileSystemLoader
from config import TEMPLATE_ROOT


class HtmlMaker:
    """Class for make the html file with link images and legals"""

    def __init__(self, dir_parent_path, project_name):
        self.__dir_parent_path = dir_parent_path
        self.__project_name = project_name
        self.__templates_path = None
        self.__html_template = None
        self.__map_items = None
        self.__html_items = {}
        self.__set_path_template()


    def __set_html_file_path(self):
        html_file_name = self.__project_name + '.html'
        return os.path.join(self.__dir_parent_path, html_file_name)


    def __set_path_template(self):
        self.__templates_path = TEMPLATE_ROOT


    def __mapping_items(self, items_img, items_web):
        if self.__map_items is None:
            return (items_img, items_web)

        mapped_items = []
        index = 0
        for amount in self.__map_items:
            try:
                if amount == 1:
                    mapped_items.append((items_img[index], items_web[index]))
                else:
                    mapped_items.append((items_img[index:index + amount], items_web[index:index + amount]))
                index += amount
            except IndexError:
                if items_img[index:]==[]:
                    break
                mapped_items.append((items_img[index:], items_web[index:]))
        return mapped_items


    def __process_items_for_html_file(self, data):

        items_1, items_2, items_3 = data
        url_mappings = self.__mapping_items(items_1, items_2)

        context = {
            'url_img_web':url_mappings,
            'legals':items_3,
            'title':self.__project_name,
        }
        self.__html_items = context


    def __set_config_jinja(self):
        template = 'add_elements.html'
        file_system = FileSystemLoader(self.__templates_path)
        jinja_environment = Environment(loader=file_system)
        jinja_environment.globals.update(zip=zip)

        self.__html_template = jinja_environment.get_template(template)


    def __render_html_with_items(self):
        rendered_html = self.__html_template.render(self.__html_items)
        return rendered_html


    def __save_html_file(self):
        rendered_html = self.__render_html_with_items()
        html_file_path = self.__set_html_file_path()
        output_file = open(html_file_path, 'w', encoding='UTF8')
        output_file.write(rendered_html)
        output_file.close()


    def make_html_file(self, data):
        """Make the html file for the images"""

        self.__process_items_for_html_file(data)
        self.__set_config_jinja()
        self.__render_html_with_items()
        self.__save_html_file()


    def map_items_html(self, map_items):
        """Recive a map for the items on html file"""

        self.__map_items = map_items