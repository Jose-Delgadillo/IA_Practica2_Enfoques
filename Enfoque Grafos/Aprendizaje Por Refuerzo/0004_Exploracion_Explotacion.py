"""
Prácticas de Inteligencia Artificial
Exploración vs. Explotación: Política Epsilon-Greedy

En este programa se ilustra el concepto de exploración frente a explotación dentro del contexto de un agente de aprendizaje por refuerzo. 
El agente tiene que balancear entre:

1. **Exploración**: Elegir una acción aleatoria en el entorno para aprender más sobre él.
2. **Explotación**: Elegir la acción que maximiza el valor esperado de la recompensa según lo aprendido hasta el momento.

La política epsilon-greedy es una de las formas de manejar este dilema. Esta política dice que con una probabilidad **epsilon** (ε), el agente va a explorar (elegir una acción aleatoria), y con una probabilidad **(1 - epsilon)**, el agente va a explotar (elegir la acción con el mayor valor de Q).

En este programa, un agente entrenado en un entorno simple actualizará su función de valor Q utilizando esta política. 

El agente aprende a través de iteraciones y optimiza sus decisiones basadas en las recompensas obtenidas por cada acción tomada en cada estado.

"""

import random

# Función para seleccionar la acción según la política epsilon-greedy
def seleccionar_accion(estado, Q, epsilon, acciones):
    """
    Selecciona la acción de acuerdo con la política epsilon-greedy.
    
    Con probabilidad epsilon, el agente explora eligiendo una acción aleatoria.
    Con probabilidad (1 - epsilon), el agente explota eligiendo la acción con el mayor valor Q.
    
    :param estado: Estado actual del agente
    :param Q: Diccionario que contiene las funciones Q para cada acción en cada estado
    :param epsilon: Proporción de exploración (0 <= epsilon <= 1)
    :param acciones: Lista de acciones posibles en cada estado
    :return: Acción seleccionada
    """
    if random.uniform(0, 1) < epsilon:
        # Exploración: elige una acción aleatoria
        return random.choice(acciones[estado])
    else:
        # Explotación: elige la acción con el valor Q máximo
        return max(acciones[estado], key=lambda x: Q[estado][x])

# Función para actualizar la función Q basándose en la recompensa obtenida
def actualizar_Q(Q, estado, accion, recompensa, siguiente_estado, alpha, gamma, acciones):
    """
    Actualiza el valor de la función Q para el par estado-acción usando la fórmula de Q-learning.
    
    :param Q: Diccionario de valores Q
    :param estado: Estado actual
    :param accion: Acción tomada en el estado actual
    :param recompensa: Recompensa obtenida después de tomar la acción
    :param siguiente_estado: El siguiente estado después de tomar la acción
    :param alpha: Tasa de aprendizaje
    :param gamma: Factor de descuento
    :param acciones: Lista de acciones posibles
    """
    # Obtener el valor máximo de Q para el siguiente estado (explotación)
    max_Q_siguiente_estado = max([Q[siguiente_estado][a] for a in acciones[siguiente_estado]])
    
    # Fórmula de actualización Q-learning
    Q[estado][accion] = Q[estado][accion] + alpha * (recompensa + gamma * max_Q_siguiente_estado - Q[estado][accion])

# Definir el entorno y el agente
def entorno():
    """
    Simula un entorno sencillo con 3 estados y 2 acciones posibles por estado.
    
    :return: Diccionario de estados y sus acciones posibles con recompensas asociadas.
    """
    # Definimos 3 estados (S0, S1, S2)
    # Cada estado tiene 2 acciones: 'A' y 'B'
    acciones = {
        'S0': ['A', 'B'],
        'S1': ['A', 'B'],
        'S2': ['A', 'B']
    }
    
    # Definimos las recompensas para cada acción en cada estado
    recompensas = {
        ('S0', 'A'): 1,
        ('S0', 'B'): 0,
        ('S1', 'A'): 0,
        ('S1', 'B'): 2,
        ('S2', 'A'): 3,
        ('S2', 'B'): 1
    }
    
    # Definimos las transiciones de estado
    transiciones = {
        'S0': {'A': 'S1', 'B': 'S2'},
        'S1': {'A': 'S2', 'B': 'S0'},
        'S2': {'A': 'S0', 'B': 'S1'}
    }
    
    return acciones, recompensas, transiciones

def entrenamiento(epsilon, alpha, gamma, iteraciones):
    """
    Entrenamiento del agente usando la política epsilon-greedy y Q-learning.
    
    :param epsilon: Proporción de exploración
    :param alpha: Tasa de aprendizaje
    :param gamma: Factor de descuento
    :param iteraciones: Número de iteraciones de entrenamiento
    """
    # Inicializar el diccionario Q con valores arbitrarios
    acciones, recompensas, transiciones = entorno()
    
    # Diccionario Q para almacenar los valores Q de cada acción en cada estado
    Q = {estado: {accion: 0 for accion in acciones[estado]} for estado in acciones}
    
    # Entrenamiento
    for i in range(iteraciones):
        # Selección de un estado aleatorio para comenzar el episodio
        estado_actual = random.choice(list(acciones.keys()))
        
        # Ejecutar una serie de acciones en este episodio
        for _ in range(10):  # Limitar a 10 pasos por episodio
            accion = seleccionar_accion(estado_actual, Q, epsilon, acciones)
            siguiente_estado = transiciones[estado_actual][accion]
            recompensa = recompensas[(estado_actual, accion)]
            
            # Actualizar la función Q
            actualizar_Q(Q, estado_actual, accion, recompensa, siguiente_estado, alpha, gamma, acciones)
            
            # Moverse al siguiente estado
            estado_actual = siguiente_estado
    
    # Devolver los valores Q aprendidos
    return Q

# Configuración de parámetros
epsilon = 0.1  # 10% de exploración
alpha = 0.5    # Tasa de aprendizaje
gamma = 0.9    # Factor de descuento
iteraciones = 1000  # Número de episodios de entrenamiento

# Entrenamiento del agente
Q_aprendido = entrenamiento(epsilon, alpha, gamma, iteraciones)

# Imprimir los resultados del entrenamiento
print("Valores Q aprendidos:")
for estado in Q_aprendido:
    print(f"Estado {estado}: {Q_aprendido[estado]}")
