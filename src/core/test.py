import os

ruta = "D:/Fazil/2024/Enero/30-01/01 FEB - 07 FEB KV TOTTUS VERANO - HS - SUPERMERCADO/ALTA MAIL TT FOOD SUPERMERCADO 1-7 FEB.png"


# Obtener el directorio que contiene el archivo

dir_fac = os.path.basename(os.path.dirname(ruta))

print(dir_fac)
