import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de la ecuación logística
r = 4  # Tasa de crecimiento (puedes cambiarlo para ver diferentes comportamientos)
x0 = 0.1  # Población inicial
n_generations = 300  # Número de generaciones

# Función para modelar el crecimiento poblacional con la ecuación logística
def logistic_growth(r, x, generations):
    population = [x]  # Lista que almacena la población en cada generación
    for _ in range(generations):
        x = r * x * (1 - x)  # Ecuación logística
        population.append(x)
    return population

# Datos iniciales
population_data = logistic_growth(r, x0, n_generations)

# Configuración del gráfico
fig, ax = plt.subplots()
ax.set_xlim(0, n_generations)
ax.set_ylim(0, 1)
line, = ax.plot([], [], lw=2, color='b')

# Etiquetas
ax.set_title('Evolución de la Población de Conejos')
ax.set_xlabel('Generación')
ax.set_ylabel('Población (x)')

# Función de inicialización
def init():
    line.set_data([], [])
    return line,

# Función de actualización de la animación
def update(frame):
    x = np.linspace(0, frame, frame)
    y = population_data[:frame]
    line.set_data(x, y)
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(1, n_generations), init_func=init, blit=True, interval=50)

plt.show()
