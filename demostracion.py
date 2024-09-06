import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir parámetros de la imagen (Conjunto de Mandelbrot)
WIDTH, HEIGHT = 500, 500
RE_START, RE_END = -2, 1
IM_START, IM_END = -1.5, 1.5
MAX_ITER = 100

# Crear una matriz para los píxeles del conjunto de Mandelbrot
mandelbrot_set = np.zeros((WIDTH, HEIGHT))

# Función que determina si un punto pertenece al conjunto de Mandelbrot
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

# Llenar la matriz del conjunto de Mandelbrot
for x in range(WIDTH):
    for y in range(HEIGHT):
        re = RE_START + (x / WIDTH) * (RE_END - RE_START)
        im = IM_START + (y / HEIGHT) * (IM_END - IM_START)
        c = complex(re, im)
        mandelbrot_set[x, y] = mandelbrot(c)

# Generar el diagrama de bifurcación en la dirección z
r_min, r_max = 2.5, 4.0
num_r = WIDTH
num_iterations = 1000
last_iterations = 100

# Crear una lista de valores de r
r_values = np.linspace(r_min, r_max, num_r)
x = 1e-5 * np.ones(num_r)

# Almacenar valores en z para cada bifurcación
z_vals = np.zeros((WIDTH, HEIGHT))

# Iterar sobre el sistema logístico
for i in range(num_iterations):
    x = r_values * x * (1 - x)
    if i >= (num_iterations - last_iterations):
        z_vals[:, i % HEIGHT] = x

# Crear malla para las coordenadas x, y, z
X = np.linspace(RE_START, RE_END, WIDTH)
Y = np.linspace(IM_START, IM_END, HEIGHT)
X, Y = np.meshgrid(X, Y)
Z = mandelbrot_set.T / MAX_ITER  # Normalizar el conjunto de Mandelbrot
Z_bif = z_vals.T  # Z_bifurcación corresponde al comportamiento caótico

# Crear la figura 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie del conjunto de Mandelbrot
ax.plot_surface(X, Y, Z, cmap='twilight', edgecolor='none', alpha=0.6)

# Graficar el diagrama de bifurcación en 3D
ax.plot_surface(X, Y, Z_bif, cmap='inferno', edgecolor='none', alpha=0.4)

# Configuración de etiquetas
ax.set_xlabel('Parte Real (Re)', fontsize=12)
ax.set_ylabel('Parte Imaginaria (Im)', fontsize=12)
ax.set_zlabel('Iteraciones / Bifurcaciones', fontsize=12)
ax.set_title('Conjunto de Mandelbrot y Diagrama de Bifurcación en 3D', fontsize=14)

plt.show()
