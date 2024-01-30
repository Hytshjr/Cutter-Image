from gui_app import Frame
import tkinter as tk


def run():
    # Crear la ventana
    window = tk.Tk()
    window.title("Fazil")
    window.config(bg='#fff')

    # Cargar el archivo de imagen desde el disco.
    icono = tk.PhotoImage(file='images\\fazil.png')

    # Establecerlo como ícono de la ventana.
    window.iconphoto(True, icono)

    # edit = Editor(root = window) 
    Frame(root = window)#, clase = edit)

    # Iniciar el bucle de la aplicación
    window.mainloop()

if __name__ == "__main__":
    run()