"""
Prácticas de Inteligencia Artificial
Q-Learning

El algoritmo Q-Learning es un método de aprendizaje por refuerzo en el que un agente aprende una política óptima de decisiones, sin necesidad de un modelo del entorno. El agente aprende a partir de recompensas obtenidas por las acciones que toma en su entorno, y utiliza estos datos para actualizar una tabla de valores de acción (Q-values).

Este código implementa el algoritmo de Q-Learning en un entorno sencillo de estados y acciones, en el que el agente aprende a través de interacciones y actualizaciones de Q-values.
"""
import random

# Definir los estados del entorno
estados = ['S0', 'S1', 'S2', 'S3', 'S4']

# Definir las recompensas para cada estado
recompensas = {'S0': 0, 'S1': -1, 'S2': -2, 'S3': 1, 'S4': 5}

# Definir las acciones disponibles para cada estado
acciones = {'S0': ['S1'], 'S1': ['S2'], 'S2': ['S3'], 'S3': ['S4'], 'S4': ['S0']}

# Parámetros de Q-Learning
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.2  # Tasa de exploración (probabilidad de elegir una acción aleatoria)
num_iteraciones = 100  # Número de iteraciones del proceso de aprendizaje

# Inicializar la tabla Q para cada estado-acción
Q = {estado: {accion: 0 for accion in acciones[estado]} for estado in estados}

def seleccionar_accion(estado):
    """
    Función para seleccionar la acción a realizar por el agente.
    Utiliza una política epsilon-greedy: con probabilidad epsilon elige una acción aleatoria,
    y con probabilidad 1-epsilon selecciona la acción con el mayor valor Q.
    """
    if random.uniform(0, 1) < epsilon:
        # Selección aleatoria
        return random.choice(acciones[estado])
    else:
        # Selección basada en el valor máximo de Q
        return max(acciones[estado], key=lambda x: Q[estado][x])

def q_learning():
    """
    Implementación del algoritmo Q-Learning, donde el agente aprende a través de iteraciones.
    El agente explora el entorno y actualiza su política de acción basada en las recompensas obtenidas.
    """
    for iteracion in range(num_iteraciones):
        # Seleccionar un estado inicial aleatorio
        estado_actual = random.choice(estados)

        # El agente selecciona una acción en función de la política epsilon-greedy
        accion = seleccionar_accion(estado_actual)

        # El agente transita al siguiente estado basado en la acción
        siguiente_estado = accion

        # El agente recibe la recompensa asociada al estado actual
        recompensa = recompensas[estado_actual]

        # Actualización de la función de valor Q usando la fórmula de Q-learning
        Q[estado_actual][accion] = Q[estado_actual][accion] + alpha * (recompensa + gamma * max(Q[siguiente_estado].values()) - Q[estado_actual][accion])

        # Imprimir el valor de Q de la acción en cada iteración
        print(f"Iteración {iteracion + 1}: Estado: {estado_actual}, Acción: {accion}, "
              f"Recompensa: {recompensa}, Valor Q de la acción: {Q[estado_actual][accion]}")

    # Mostrar los valores finales de Q después de completar el proceso de aprendizaje
    print("\nValores finales de Q después del aprendizaje:")
    for estado in estados:
        print(f"{estado}: {Q[estado]}")
        
# Ejecutar el algoritmo de Q-Learning
q_learning()
