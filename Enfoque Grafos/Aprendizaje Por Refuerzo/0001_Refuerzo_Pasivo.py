"""
Prácticas de Inteligencia Artificial
Aprendizaje por Refuerzo Pasivo

El aprendizaje por refuerzo pasivo se refiere a un enfoque en el que un agente aprende a partir de recompensas obtenidas al seguir una política fija sin tomar decisiones activas. El agente evalúa los valores de los estados según las recompensas que recibe y ajusta su estimación a lo largo del tiempo.
Este código simula el proceso de aprendizaje en el que un agente sigue una política predefinida y ajusta los valores de los estados basándose en las recompensas obtenidas.
"""
import random

# Definimos los parámetros del entorno:
# Estados posibles del entorno
estados = ['S0', 'S1', 'S2', 'S3', 'S4']

# Recompensas que se reciben en cada estado
recompensas = {'S0': 0, 'S1': -1, 'S2': -2, 'S3': 1, 'S4': 5}

# La política es una función que determina a qué estado transitar dado un estado actual
# En este caso, la política está definida de forma que el agente siempre pasa al siguiente estado
politica = {
    'S0': 'S1',
    'S1': 'S2',
    'S2': 'S3',
    'S3': 'S4',
    'S4': 'S0'
}

# Parámetros del aprendizaje
gamma = 0.9  # Factor de descuento (importancia de las recompensas futuras)
epsilon = 0.1  # Tasa de exploración (probabilidad de realizar una acción aleatoria)
num_iteraciones = 100  # Número de iteraciones para el algoritmo de aprendizaje

# Inicializamos los valores de los estados
valores = {'S0': 0.0, 'S1': 0.0, 'S2': 0.0, 'S3': 0.0, 'S4': 0.0}

def aprendizaje_por_refuerzo_pasivo():
    """
    Implementación del algoritmo de aprendizaje por refuerzo pasivo donde el agente sigue
    una política fija y ajusta su estimación de los valores de los estados basándose en las recompensas.
    """
    for iteracion in range(num_iteraciones):
        # Elegimos un estado inicial aleatorio
        estado_actual = random.choice(estados)
        
        # El agente sigue la política de forma pasiva
        # La acción en la política lleva al agente al siguiente estado
        siguiente_estado = politica[estado_actual]

        # Recompensa recibida por el agente
        recompensa = recompensas[estado_actual]

        # Actualización del valor del estado con base en la recompensa obtenida
        # Usamos la fórmula de actualización de valores basada en el valor estimado del siguiente estado
        valores[estado_actual] = recompensa + gamma * valores[siguiente_estado]
        
        # Imprimir el valor de los estados para esta iteración
        print(f"Iteración {iteracion + 1}: Estado: {estado_actual}, Recompensa: {recompensa}, "
              f"Valor Estimado del Estado: {valores[estado_actual]}")

    # Después de las iteraciones, mostramos los valores finales de todos los estados
    print("\nValores finales de los estados después del aprendizaje:")
    for estado in estados:
        print(f"{estado}: {valores[estado]}")

# Llamamos a la función de aprendizaje por refuerzo pasivo
aprendizaje_por_refuerzo_pasivo()
