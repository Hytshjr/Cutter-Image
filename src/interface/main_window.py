from core.api_utils import replace_api, save_api
from core.image_handling import Editor
from core.button_utils import ButtonUtils
from decouple import config
import tkinter as tk



# Acces to environment variable from .env
API_KEY = config('API_KEY')
img_user = Editor()
button_utls = ButtonUtils()


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.config(width=480, height=320, bg='#23606E')
        self.campos_rellenar()


    def campos_rellenar(self):
        self.create_api_section()
        self.create_buttons()


    def create_api_section(self):
        # Section text Api
        self.label_nombre = tk.Label(self, text = 'Introduce la Api: ')
        self.label_nombre.config(font = ('Helvetica',10,'bold'),fg='#fff', bg='#23606E')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=15)

        # Content of Api
        self.compres_api = tk.StringVar() #Guarda lo que ingresa en el primer campo
        self.compres_api.set(API_KEY)
        self.entry_api = tk.Entry(self, textvariable = self.compres_api)
        self.entry_api.config(width=20, bg='#23606E', state='disable')
        self.entry_api.grid(row=0, column=1)


    def create_buttons(self):
        #Este primer boton guarda el api
        self.boton_save = tk.Button(self, text='Guardar Api', command=lambda: save_api(self.entry_api))
        self.boton_save.config(font = ('Helvetica',10,'bold'), width=20, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_save.grid(row=1, column=0,  pady=3)

        #Este segundo boton remplaza el api
        self.boton_replpace = tk.Button(self, text='Reemplazar Api', command=lambda: replace_api(self.entry_api))
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=20, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=1, column=1, pady=3)

        #Este boton recorte la imagen
        self.boton_replpace = tk.Button(self, text='Recortar imagen', command=button_utls.cut_image)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=2, column=0, pady=3, columnspan=2)

        #Este boton comprime las imagenes
        self.boton_replpace = tk.Button(self, text='Comprimir imagenes' )
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=3, column=0, pady=3, columnspan=2)

        #Este boton crea el nuevo frame para hacer el html
        self.boton_replpace = tk.Button(self, text='Hacer el html', )#command=self.create_html)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=4, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y compresion de imagen')
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=5, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y hacer HTML', command=button_utls.cut_img_make_html)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=6, column=0, pady=3, columnspan=2)