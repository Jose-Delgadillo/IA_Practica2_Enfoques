"""
Prácticas de Inteligencia Artificial
Búsqueda Informada: Temple Simulado (Simulated Annealing)
"""

import math
import random

def temple_simulado(grafo, heuristicas, inicio, objetivo, temperatura_inicial=100, enfriamiento=0.95, iteraciones_por_temp=10):
    """
    Algoritmo de Temple Simulado.
    - Elige vecinos aleatorios.
    - Acepta soluciones peores con cierta probabilidad basada en la temperatura.
    """

    actual = inicio
    mejor = actual
    camino = [actual]
    temperatura = temperatura_inicial

    while temperatura > 0.1:
        for _ in range(iteraciones_por_temp):
            vecinos = grafo.get(actual, [])
            if not vecinos:
                break  # No hay vecinos

            vecino = random.choice(vecinos)  # Elige un vecino aleatorio

            # Evaluar diferencia de heurística
            delta = heuristicas[vecino] - heuristicas[actual]

            if delta < 0:
                # El vecino es mejor (menor heurística)
                actual = vecino
                camino.append(actual)
                if heuristicas[actual] < heuristicas[mejor]:
                    mejor = actual
            else:
                # El vecino es peor: aceptarlo con una probabilidad
                prob = math.exp(-delta / temperatura)
                if random.random() < prob:
                    actual = vecino
                    camino.append(actual)

            if actual == objetivo:
                return camino, True

        temperatura *= enfriamiento  # Enfriar el sistema

    return camino, actual == objetivo


# ============ Definición del grafo y heurísticas ============
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristicas = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1  # Objetivo
}

inicio = 'A'
objetivo = 'F'

# ============ Ejecutar el algoritmo ============
camino, exito = temple_simulado(grafo, heuristicas, inicio, objetivo)

# ============ Mostrar resultados ============
print("\n===== Búsqueda: Temple Simulado =====")
print(f"Camino seguido: {camino}")
print(f"¿Se llegó al objetivo?: {'Sí' if exito else 'No'}")
