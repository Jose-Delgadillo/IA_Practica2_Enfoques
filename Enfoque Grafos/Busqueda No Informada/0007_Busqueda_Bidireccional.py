"""
Prácticas de Inteligencia artificial
Ejemplos de Búsqueda Bidireccional
"""
from collections import deque

def hacer_grafo_bidireccional(grafo):
    grafo_bidi = {}
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            grafo_bidi.setdefault(nodo, []).append(vecino)
            grafo_bidi.setdefault(vecino, []).append(nodo)
    return grafo_bidi

def busqueda_bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    grafo = hacer_grafo_bidireccional(grafo)  # Convertir el grafo a bidireccional

    # Inicializar estructuras de datos
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # Expandir desde el inicio
        camino_inicio = cola_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

        for vecino in grafo.get(nodo_inicio, []):
            if vecino not in visitados_inicio:
                nuevo_camino = camino_inicio + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                if vecino in visitados_objetivo:
                    # Se encontraron
                    return nuevo_camino + visitados_objetivo[vecino][-2::-1]

        # Expandir desde el objetivo
        camino_objetivo = cola_objetivo.popleft()
        nodo_objetivo = camino_objetivo[-1]

        for vecino in grafo.get(nodo_objetivo, []):
            if vecino not in visitados_objetivo:
                nuevo_camino = camino_objetivo + [vecino]
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)

                if vecino in visitados_inicio:
                    return visitados_inicio[vecino] + nuevo_camino[-2::-1]

    return None

# ======= Ejemplo de grafo dirigido =======

grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

inicio = 'A'
objetivo = 'F'

camino = busqueda_bidireccional(grafo, inicio, objetivo)
print(f"Camino encontrado: {camino}")
