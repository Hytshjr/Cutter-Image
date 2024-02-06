from core.image_handling import Editor


class MainUtils:
    def __init__(self):
        self.editor = Editor()

    def cut_image(self):
        self.editor.cut_image()