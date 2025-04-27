"""
Prácticas de Inteligencia Artificial
Ejemplos de Busqueda en Anchura
"""
from collections import deque

def bfs(grafo, inicio):
    visitados = set()              # Para registrar los nodos ya visitados
    cola = deque([inicio])          # Usamos una cola para BFS
    resultado = []                  # Para registrar el orden de visita

    while cola:
        nodo = cola.popleft()       # Sacamos el primer nodo de la cola
        if nodo not in visitados:
            visitados.add(nodo)      # Marcamos el nodo como visitado
            resultado.append(nodo)   # Guardamos el nodo visitado
            # Agregamos a la cola todos los vecinos que no hayan sido visitados
            cola.extend(vecino for vecino in grafo[nodo] if vecino not in visitados)

    return resultado

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio = 'A'
orden_visita = bfs(grafo, inicio)
print("Orden de visita:", orden_visita)

#Al final nos resulta en ['A', 'B', 'C', 'D', 'E', 'F']