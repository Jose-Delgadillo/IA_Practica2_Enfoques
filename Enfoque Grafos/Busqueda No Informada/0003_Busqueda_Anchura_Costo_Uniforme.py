"""
Prácticas de Inteligencia Artificial
Ejemplos de Búsqueda en Anchura de Costo Uniforme
"""
import heapq

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    # La cola de prioridad almacena tuplas de (costo acumulado, nodo actual, camino recorrido)
    cola = [(0, inicio, [inicio])]
    visitados = set()

    while cola:
        costo_actual, nodo_actual, camino = heapq.heappop(cola)

        if nodo_actual == objetivo:
            return camino, costo_actual
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, costo in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    heapq.heappush(cola, (costo_actual + costo, vecino, camino + [vecino]))
    
    return None, float('inf') #Si no se encuentra camino

# Ejemplo de grafo con costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

inicio = 'A'
objetivo = 'F'

camino, costo_total = busqueda_costo_uniforme(grafo, inicio, objetivo)
print(f"Camino encontrado: {camino}")
print(f"Costo total: {costo_total}")

#Camino encontrado: ['A', 'C', 'F'] Costo total: 5