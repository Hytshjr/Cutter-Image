image_cuts = [(0, 309, 0, 600), (309, 472, 0, 600), (472, 598, 0, 600), (598, 738, 0, 600), (738, 781, 0, 261), (738, 781, 261, 409), (738, 781, 409, 546), (781, 853, 0, 600), (853, 894, 0, 600)]

grupo_dict = {}

# Iterar sobre las tuplas y construir el diccionario
for image_cut in image_cuts:
    KEY = image_cut[0]  # La clave es una tupla con los dos primeros elementos
    if KEY not in grupo_dict:
        grupo_dict[KEY] = []
        grupo_dict[KEY].append(image_cut[0])
        grupo_dict[KEY].append(image_cut[1])
        grupo_dict[KEY].append(image_cut[2])
        grupo_dict[KEY].append(image_cut[3])
    else:
        grupo_dict[KEY].append(image_cut[3])

print(grupo_dict)
