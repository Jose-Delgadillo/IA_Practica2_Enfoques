"""
Prácticas de Inteligencia artificial
Ejemplos de Búsqueda en Grafos (general)
"""
from collections import deque

def busqueda_en_grafos(grafo, inicio, objetivo):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]

        if nodo_actual == objetivo:
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nueva_ruta = list(camino)
                    nueva_ruta.append(vecino)
                    cola.append(nueva_ruta)

    return None

# Ejemplo de grafo con ciclos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],  # B puede regresar a A (ciclo)
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'

camino = busqueda_en_grafos(grafo, inicio, objetivo)
print(f"Camino encontrado: {camino}")
