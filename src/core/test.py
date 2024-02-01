import numpy as np

matrix = np.array([
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9), (7, 8, 9), (7, 8, 9)],
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9), (7, 8, 9), (7, 8, 9)],
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9), (7, 8, 9), (7, 8, 9)],
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9), (7, 8, 9), (7, 8, 9)],
    [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9), (7, 8, 9), (7, 8, 9)]
])

# Divide la matriz en dos segmentos específicos
first_segment = matrix[:, :3]  # Primeras tres columnas
second_segment = matrix[:, 3:]  # Resto de las columnas

# Convierte las matrices de nuevo a listas de Python si es necesario
first_segment = first_segment.tolist()
second_segment = second_segment.tolist()

print(first_segment)
print(second_segment)


# img = self.img[self.coords['rtngl_top']:self.coords['rtngl_bottom'],self.coords['rtngl_mid']:]

# cv2.imshow('test', img)