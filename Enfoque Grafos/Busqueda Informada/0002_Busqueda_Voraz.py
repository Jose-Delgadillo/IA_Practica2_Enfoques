"""
Prácticas de Inteligencia Artificial
Búsqueda Voraz (Primero el Mejor)
"""

import heapq

def busqueda_voraz(grafo, heuristicas, inicio, objetivo):
    # Cola de prioridad (heurística primero)
    cola = [(heuristicas[inicio], inicio, [inicio])]
    visitados = set()

    while cola:
        heur_actual, nodo_actual, camino = heapq.heappop(cola)

        if nodo_actual == objetivo:
            return camino
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    heapq.heappush(cola, (heuristicas[vecino], vecino, camino + [vecino]))
    
    return None

# Definimos el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos las heurísticas
heuristicas = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Parámetros de búsqueda
inicio = 'A'
objetivo = 'F'

camino = busqueda_voraz(grafo, heuristicas, inicio, objetivo)
print(f"Camino encontrado (Voraz): {camino}")

#Camino encontrado (Voraz): ['A', 'B', 'E', 'F']