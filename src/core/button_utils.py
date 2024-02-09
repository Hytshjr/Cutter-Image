from core.image_handling import Editor
from interface.html_window import HtmlEntrys

class ButtonUtils:
    def __init__(self):
        self.editor = Editor()
        self.html = HtmlEntrys()


    def cut_image(self):
        # Call the func that cut the image
        self.editor.cut_image()


    def cut_img_make_html(self):
        # Cut the image and make the html
        self.editor.save_imgs = []
        self.editor.cut_image()

        if not self.editor.save_imgs:
            return

        self.html.init_windows()
        self.html.editor = self.editor
        self.html.button = self