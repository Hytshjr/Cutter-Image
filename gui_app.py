import tkinter as tk
from modules.image_cut import buscador, Editor

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root)

        self.root = root
        self.pack()
        self.config(width= 480, height= 320, bg='#23606E')
        self.campos_rellenar()


    def campos_rellenar(self):
        editor = Editor(root=self.root)

        # Seccion de Api
        self.label_nombre = tk.Label(self, text = 'Introduce la Api: ')
        self.label_nombre.config(font = ('Helvetica',10,'bold'),fg='#fff', bg='#23606E')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=15)


        # Informacion de Api
        self.compres_api = tk.StringVar() #Guarda lo que ingresa en el primer campo
        self.compres_api.set(buscador('html\\info.txt', 'key'))
        self.entry_api = tk.Entry(self, textvariable = self.compres_api)
        self.entry_api.config(width=20, bg='#23606E', state='disable')
        self.entry_api.grid(row=0, column=1)

        # Botones
        #Este primer boton guarda el api
        self.boton_save = tk.Button(self, text='Guardar Api')#command=self.guardar_api)
        self.boton_save.config(font = ('Helvetica',10,'bold'), width=20, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_save.grid(row=1, column=0,  pady=3)

        #Este segundo boton remplaza el api
        self.boton_replpace = tk.Button(self, text='Reemplazar Api', )#command=self.replace_api)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=20, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=1, column=1, pady=3)

        #Este boton recorte la imagen
        self.boton_replpace = tk.Button(self, text='Recortar imagen', command=editor.cut_image)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=2, column=0, pady=3, columnspan=2)

        #Este boton comprime las imagenes
        self.boton_replpace = tk.Button(self, text='Comprimir imagenes', command=editor.compress )
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=3, column=0, pady=3, columnspan=2)

        #Este boton crea el nuevo frame para hacer el html
        self.boton_replpace = tk.Button(self, text='Hacer el html', )#command=self.create_html)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=4, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y compresion de imagen', command=self.just_cut)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=5, column=0, pady=3, columnspan=2)

        #Este boton hace el proceso de corte y compresion
        self.boton_replpace = tk.Button(self, text='Corte y hacer HTML', command=self.cut_compress)
        self.boton_replpace.config(font = ('Helvetica',10,'bold'), width=40, border=0, fg='#23606E', bg='#FACFCE')
        self.boton_replpace.grid(row=6, column=0, pady=3, columnspan=2)

        # Crear el checkbox y asociarlo a la variable
        checkbox_var_color = tk.BooleanVar()
        # Lee el archivo para setear el CAMBIO DE COLOR en True o False 
        color = buscador('html\\info.txt', 'color')
        if color == 'False':
            checkbox_var_color.set(False)
        elif color == 'True':
            checkbox_var_color.set(True)       
        checkbox_color = tk.Checkbutton(self, text="Cambiar color", variable=checkbox_var_color, command=lambda: self.las_cut('color', checkbox_var_color))
        checkbox_color.grid(row=7, column=1)

        # Crear el checkbox y asociarlo a la variable
        checkbox_var = tk.BooleanVar()
        # Lee el archivo para setear el LICOR en True o False
        last = color = buscador('html\\info.txt', 'last')            
        if last == 'False':
            checkbox_var.set(False)
        elif last == 'True':
            checkbox_var.set(True)       
        checkbox = tk.Checkbutton(self, text="Licor en exceso", variable=checkbox_var, command=lambda: self.las_cut('last', checkbox_var))
        checkbox.grid(row=7, column=0)



    def crear_entrys(self,count, position, ventana, link = True):

        link_png = []
        link_app = []

        # En una iteracion crea los entrys que le pida, le paso la columna como atributo
        def crear_inputs(count, position, columna = 0):
            # count: La cantidad de entrys debe de haber
            # position: a partir de que empieza a crear los entrys

            list_entry = []

            for box_content in range(count):

                count_varia = tk.StringVar() #Guarda lo que ingresa en el campo
                position_row = position+(box_content+1)

                count_get = tk.Entry(ventana, textvariable = count_varia)
                count_get.config(width=20, bg='#DCDCDC', border=0)
                count_get.grid(row=position_row, column=columna, padx=5, pady=5)

                list_entry.append(count_get)

            return list_entry
            


    def new_windows(self, name = 'Nueva ventana'):
            window = tk.Toplevel(self)
            window.title(name)
            window.config(bg='#808080')

            return window
    

    def just_cut(self):
        editor = Editor(root=self.root)

        editor.cut_image()
        editor.compress(continuar = False)   


    def cut_compress(self):
        editor = Editor(root=self.root)

        try:
            editor.cut_image()
            # editor.compress(continuar = False)   

            ventana = self.new_windows(editor.name)
            ventana.config(width=200)

            #Este primer espacio para poner la cantidad de legales
            count_legal = tk.StringVar() #Guarda lo que ingresa en el campo
            count_legal.set('')

            entry_legal = tk.Entry(ventana, textvariable = count_legal)
            entry_legal.config(width=20, bg='#DCDCDC', border=0)
            entry_legal.grid(row=0, column=0, padx=10, pady=10)

            # Boton para obtener las cantidades   
            boton_save = tk.Button(ventana, text='Cantidad de Legales', command=lambda: editor.obtener_contenido(count_legal, ventana))#, command=obtener_contenido)
            boton_save.config(width=20, border=0, fg='black', bg='#DCDCDC')
            boton_save.grid(row=0, column=1,columnspan=2)

        except NameError as e:
            print(e)
        

    def las_cut(self, cambio, check_box):
        
        import fileinput

        bool = check_box.get()

        with fileinput.FileInput('html\info.txt', inplace=True) as file:
                # Recorrer cada línea del archivo de entrada
                for line in file:   
                              
                    # Buscar la etiqueta <!--/Legal/-->
                    if cambio in line:
                      print(f'''{cambio} = {bool},''')
                    
                    else:
                      print(line,end='')  
