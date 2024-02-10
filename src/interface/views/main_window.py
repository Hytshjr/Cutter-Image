"""Module that create the main window."""

import tkinter as tk
from decouple import config

# Acces to environment variable from .env
API_KEY = config('API_KEY')

class Frame(tk.Frame):
    """Class add elements to main window"""

    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root
        self.key_api = None
        self.entry_api = None
        self.button_config = None
        self.controller = controller
        self._set_style_frame()
        self._add_elements_frame()
        self._show_frame()


    def _set_style_frame(self):
        self.config(bg='#23666E')


    def _add_elements_frame(self):
        self._create_api_section()
        self._add_func_buttons()


    def _create_api_section(self):
        self._add_text_api()
        self._add_entry_api()
        self._set_style_buttons()
        self._add_buttons_api()


    def _add_text_api(self):
        # Section text Api
        text_api = tk.Label(self, text = 'Introduce la Api: ')
        text_api.config(font = ('Helvetica',10,'bold'), fg='#fff', bg='#23666E')
        text_api.grid(row=0, column=0, padx=10, pady=15)


    def _add_entry_api(self):
        # Content key Api
        self.key_api = tk.StringVar()
        self.key_api.set(API_KEY)
        self._set_entry_api_on_frame()


    def _set_entry_api_on_frame(self):
        # Draw entry on Frame
        self.entry_api = tk.Entry(self, textvariable=self.key_api)
        self.entry_api.config(width=20, bg='#23606E', state='disable')
        self.entry_api.grid(row=0, column=1)


    def _add_buttons_api(self):
        #Este primer button guarda el api
        button_save = tk.Button(self, text='Guardar Api', **self.button_config, command=self.save_api)
        button_save.config(width=19)
        button_save.grid(row=1, column=0,  pady=3)

        #Este segundo button remplaza el api
        button_replpace = tk.Button(self, text='Reemplazar Api', **self.button_config, command=self.update_api)
        button_replpace.config(width=19)
        button_replpace.grid(row=1, column=1, pady=3)


    def _add_func_buttons(self):
        # Este botón recorta la imagen
        button_cut = tk.Button(self, text='Recortar imagen', **self.button_config)
        button_cut.grid(row=2, column=0, pady=3, columnspan=2)

        # Este botón comprime las imágenes
        button_compress = tk.Button(self, text='Comprimir imágenes', **self.button_config)
        button_compress.grid(row=3, column=0, pady=3, columnspan=2)

        # Este botón crea el nuevo frame para hacer el HTML
        button_html = tk.Button(self, text='Hacer el HTML', **self.button_config)
        button_html.grid(row=4, column=0, pady=3, columnspan=2)

        # Este botón hace el proceso de corte y compresión
        button_cut_compress = tk.Button(self, text='Corte y compresión de imagen', **self.button_config)
        button_cut_compress.grid(row=5, column=0, pady=3, columnspan=2)

        # Este botón hace el proceso de corte y compresión y crea el HTML
        button_cut_html = tk.Button(self, text='Corte y hacer HTML', **self.button_config)
        button_cut_html.grid(row=6, column=0, pady=3, columnspan=2)


    def _set_style_buttons(self):
        # Configuration common for buttons
        self.button_config = {
            'font': ('Helvetica', 10, 'bold'),
            'width': 40,
            'border': 0,
            'fg': '#23606E',
            'bg': '#FACFCE'
        }


    def _show_frame(self):
        self.pack()


    def save_api(self):
        """Save the api key on env file"""
        key_api = self.key_api.get()
        self.controller.save_key_api(key_api)
        self.entry_api.config(state='disable')


    def update_api(self):
        """Set the entry on normal for update the api"""
        self.entry_api.config(state='normal')