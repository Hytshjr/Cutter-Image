"""En terminal: python setup.py build"""

from cx_Freeze import setup, Executable

target = Executable(
   script='main.py',
   base='Win32GUI',  # Esto es importante para no mostrar la consola
   icon='icon.ico',
   )

setup(name='Cut App',
      version='1.5.1',
      description='Image Cutter',
      executables=[target]
)
