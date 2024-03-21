from cx_Freeze import setup, Executable

target = Executable(
   script='main.py',
   base='Win32GUI',  # Esto es importante para no mostrar la consola
   icon='D://Tottus_App//src//interface//static//images//fazil.png')

setup(name='Fazil App',
      version='1.5',
      description='Image Cutter',
      executables=[target]
)

# En terminal: python setup.py build