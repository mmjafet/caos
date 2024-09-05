import numpy as np
import matplotlib.pyplot as plt

# Parámetros del diagrama
r_min = 2.5  # Valor mínimo del parámetro r
r_max = 4.0  # Valor máximo del parámetro r
num_r = 10000  # Número de valores de r
num_iterations = 1000  # Iteraciones totales para cada r
last_iterations = 100  # Iteraciones a graficar (últimas iteraciones)

# Crear una lista de valores de r
r_values = np.linspace(r_min, r_max, num_r)

# Valores iniciales para la población (x)
x = 1e-5 * np.ones(num_r)

# Crear una lista para almacenar los valores de r y x
r_vals = []
x_vals = []

# Iterar sobre el sistema logístico
for i in range(num_iterations):
    x = r_values * x * (1 - x)  # Ecuación logística
    
    # Guardar las últimas iteraciones para el gráfico
    if i >= (num_iterations - last_iterations):
        r_vals.append(r_values)
        x_vals.append(x)

# Convertir las listas en arrays
r_vals = np.array(r_vals)
x_vals = np.array(x_vals)

# Graficar el diagrama de bifurcación
plt.figure(figsize=(10, 7))
plt.plot(r_vals, x_vals, ',k', alpha=0.25)  # Usar puntos pequeños para el gráfico

# Configuración del gráfico
plt.title('Diagrama de Bifurcación - Ecuación Logística', fontsize=16)
plt.xlabel('Tasa de Crecimiento (r)', fontsize=14)
plt.ylabel('Población (x)', fontsize=14)
plt.xlim(r_min, r_max)
plt.show()
