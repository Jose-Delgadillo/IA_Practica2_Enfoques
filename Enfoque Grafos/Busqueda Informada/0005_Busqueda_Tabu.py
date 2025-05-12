"""
Prácticas de Inteligencia Artificial
Búsqueda Informada: Búsqueda Tabú (Tabu Search)
"""

import random

def busqueda_tabu(grafo, heuristicas, inicio, objetivo, tamano_tabu=3, max_iteraciones=20):
    """
    Realiza una búsqueda tabú para encontrar el camino hacia el objetivo.
    - grafo: diccionario con nodos y sus vecinos
    - heuristicas: valores heurísticos de cada nodo
    - inicio: nodo inicial
    - objetivo: nodo a alcanzar
    - tamano_tabu: número de pasos que un nodo permanece en la lista tabú
    - max_iteraciones: número máximo de iteraciones a realizar
    """

    actual = inicio
    mejor = actual
    mejor_heuristica = heuristicas[actual]
    camino = [actual]
    lista_tabu = []

    for _ in range(max_iteraciones):
        vecinos = grafo.get(actual, [])
        if not vecinos:
            break  # No hay más vecinos que explorar

        # Filtrar vecinos que no están en la lista tabú
        candidatos = [n for n in vecinos if n not in lista_tabu]

        if not candidatos:
            break  # Todos los vecinos están en la lista tabú

        # Elegir el mejor vecino disponible (menor heurística)
        siguiente = min(candidatos, key=lambda n: heuristicas[n])
        camino.append(siguiente)

        # Actualizar la mejor solución si encontramos una mejor
        if heuristicas[siguiente] < mejor_heuristica:
            mejor = siguiente
            mejor_heuristica = heuristicas[siguiente]

        # Añadir el nodo actual a la lista tabú
        lista_tabu.append(actual)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)  # Eliminar el nodo más antiguo

        actual = siguiente

        # Si llegamos al objetivo, terminamos
        if actual == objetivo:
            break

    exito = actual == objetivo
    return camino, exito, mejor


# ============ Definir el grafo y heurísticas ============
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

# ============ Ejecutar búsqueda tabú ============
camino, exito, mejor_encontrado = busqueda_tabu(grafo, heuristicas, inicio, objetivo)

# ============ Mostrar resultados ============
print("\n===== Búsqueda Tabú =====")
print(f"Camino seguido: {camino}")
print(f"¿Se llegó al objetivo?: {'Sí' if exito else 'No'}")
print(f"Mejor nodo encontrado: {mejor_encontrado} (h={heuristicas[mejor_encontrado]})")
