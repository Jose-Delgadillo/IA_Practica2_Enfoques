"""
Prácticas de Inteligencia Artificial
Aprendizaje por Refuerzo Activo

El aprendizaje por refuerzo activo implica que un agente toma decisiones activamente sobre las acciones que debe realizar en un entorno, con el objetivo de maximizar la recompensa total que recibe. El agente explora diferentes acciones y ajusta sus decisiones basándose en las recompensas obtenidas. Este enfoque involucra la toma de decisiones para maximizar la función de valor o recompensa esperada.

En este código, el agente explora su entorno y aprende una política óptima utilizando el método de aprendizaje por refuerzo Q-learning.
"""
import random

# Definimos los estados del entorno
estados = ['S0', 'S1', 'S2', 'S3', 'S4']

# Recompensas asociadas a cada estado
recompensas = {'S0': 0, 'S1': -1, 'S2': -2, 'S3': 1, 'S4': 5}

# Las acciones disponibles en cada estado (pueden ser simplemente las transiciones a otros estados)
acciones = {'S0': ['S1'], 'S1': ['S2'], 'S2': ['S3'], 'S3': ['S4'], 'S4': ['S0']}

# Parámetros de aprendizaje
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.2  # Tasa de exploración (probabilidad de elegir una acción aleatoria)
num_iteraciones = 100  # Número de iteraciones del proceso de aprendizaje

# Inicializamos los valores Q para cada par de estado-acción
Q = {estado: {accion: 0 for accion in acciones[estado]} for estado in estados}

def seleccionar_accion(estado):
    """
    Función para seleccionar la acción que el agente debe realizar.
    Utiliza una política epsilon-greedy: con probabilidad epsilon selecciona una acción aleatoria,
    y con probabilidad 1-epsilon selecciona la acción con el mejor valor Q.
    """
    if random.uniform(0, 1) < epsilon:
        # Selección aleatoria
        return random.choice(acciones[estado])
    else:
        # Selección basada en el valor máximo de Q
        return max(acciones[estado], key=lambda x: Q[estado][x])

def aprendizaje_por_refuerzo_activo():
    """
    Implementación del aprendizaje por refuerzo activo usando el algoritmo Q-learning.
    El agente aprende una política óptima interactuando con el entorno.
    """
    for iteracion in range(num_iteraciones):
        # Elegir un estado inicial aleatorio
        estado_actual = random.choice(estados)

        # El agente selecciona una acción en función de la política epsilon-greedy
        accion = seleccionar_accion(estado_actual)

        # El agente transita al siguiente estado basado en la acción
        siguiente_estado = accion

        # Recompensa recibida por el agente al estar en el estado actual
        recompensa = recompensas[estado_actual]

        # Actualización de la función de valor Q utilizando la fórmula Q-learning
        Q[estado_actual][accion] = Q[estado_actual][accion] + alpha * (recompensa + gamma * max(Q[siguiente_estado].values()) - Q[estado_actual][accion])

        # Imprimir el valor de Q de la acción en cada iteración
        print(f"Iteración {iteracion + 1}: Estado: {estado_actual}, Acción: {accion}, "
              f"Recompensa: {recompensa}, Valor Q de la acción: {Q[estado_actual][accion]}")

    # Después de las iteraciones, mostramos los valores finales de Q para cada estado-acción
    print("\nValores finales de Q después del aprendizaje:")
    for estado in estados:
        print(f"{estado}: {Q[estado]}")
        
# Llamamos a la función de aprendizaje por refuerzo activo
aprendizaje_por_refuerzo_activo()
