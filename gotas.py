import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
n_drops = 10
drop_speed = 0.02  # Velocidad de caída

# Crear un array para las posiciones iniciales de las gotas (fuera de la pantalla)
drop_positions = np.random.rand(n_drops) * 2 - 1  # Posiciones horizontales
drop_heights = np.random.rand(n_drops) * -1  # Alturas iniciales (fuera del cuadro)

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Crear los círculos que representarán las gotas
drops, = ax.plot([], [], 'o', color='blue', markersize=8)

# Función de inicialización
def init():
    drops.set_data([], [])
    return drops,

# Función de actualización de la animación
def update(frame):
    global drop_heights

    # Actualizar las alturas de las gotas
    drop_heights += drop_speed  # Las gotas caen hacia abajo
    
    # Reposicionar las gotas que caen fuera de la pantalla (reseteo)
    drop_heights[drop_heights > 1] = np.random.rand() * -1
    
    # Actualizar los datos de las gotas
    drops.set_data(drop_positions, drop_heights)
    return drops,

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True, interval=50)

plt.show()
