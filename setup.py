from cx_Freeze import setup, Executable

target = Executable(
   script='main.py',
   base='Win32GUI',  # Esto es importante para no mostrar la consola
   icon='D:\\App_fazil\\images\\fazil.ico'  # Ruta al archivo .ico
)

setup(name='Fazil App',
      version='1.5',
      description='Fazil App',
      executables=[target]
)

# En terminal: python setup.py build