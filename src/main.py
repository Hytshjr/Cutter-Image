from config import MEDIA_ROOT
from gui.main_window import Frame
import tkinter as tk
import os

def run():
    # Create window
    window = tk.Tk()
    window.title("Fazil")
    window.config(bg='#fff')

    # Construye la ruta completa al archivo de imagen
    image_path = os.path.join(MEDIA_ROOT, 'images', 'fazil.png')

    # Charge the img from disk
    icono = tk.PhotoImage(file=image_path)

    # Set the icon
    window.iconphoto(True, icono)

    Frame(root = window)

    # Initi app while
    window.mainloop()


if __name__ == "__main__":
    run()