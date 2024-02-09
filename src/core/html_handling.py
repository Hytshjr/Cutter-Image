# from config import MEDIA_ROOT
from jinja2 import Environment, FileSystemLoader


class HtmlMaker:
    def __init__(self):
        self.path_template = ""
        self.name_file = ""
        self.path_file = ""
        self.data = {}


    def html_maker(self):
        self._set_env_jinja()
        self._set_template()
        self._render_template()
        self._write_html()


    def _set_env_jinja(self):
        file_system = FileSystemLoader(self.path_template)
        template_env = Environment(loader=file_system)
        self.template_env = template_env


    def _set_template(self):
        template = 'add_img.html'
        self.template = self.template_env.get_template(template)


    def _render_template(self):
        self.output = self.template.render(self.data)


    def _write_html(self):
        with open(self.path_file, 'w') as archivo_salida:
            archivo_salida.write(self.output)


def run():
    # Create window
    html = HtmlMaker()
    html.path_template = 'D://Tottus_App//resources//html'
    html.name_file = "test_html.html"
    html.path_file = 'D://Tottus_App//resources//html//test_html.html'
    html.data['list_png'] = [1,2,[3,4],5,[6,7,8],9]
    html.html_maker()

if __name__ == "__main__":
    run()