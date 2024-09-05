import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la imagen
WIDTH, HEIGHT = 800, 800
RE_START, RE_END = -2, 1
IM_START, IM_END = -1.5, 1.5
MAX_ITER = 100

# Crear una matriz para los píxeles
mandelbrot_set = np.zeros((WIDTH, HEIGHT))

# Función que determina si un punto pertenece al conjunto de Mandelbrot
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

# Recorrer cada píxel y determinar si pertenece al conjunto
for x in range(WIDTH):
    for y in range(HEIGHT):
        re = RE_START + (x / WIDTH) * (RE_END - RE_START)  # Parte real
        im = IM_START + (y / HEIGHT) * (IM_END - IM_START)  # Parte imaginaria
        c = complex(re, im)
        color = mandelbrot(c)
        mandelbrot_set[x, y] = color

# Graficar el conjunto de Mandelbrot
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set.T, cmap='twilight', extent=[RE_START, RE_END, IM_START, IM_END])

# Añadir etiquetas a los ejes
plt.xlabel("Parte Real (Re)", fontsize=14)
plt.ylabel("Parte Imaginaria (Im)", fontsize=14)

# Añadir barra de colores y título
plt.colorbar(label='Número de Iteraciones')
plt.title("Conjunto de Mandelbrot", fontsize=16)

# Mostrar el gráfico
plt.show()
