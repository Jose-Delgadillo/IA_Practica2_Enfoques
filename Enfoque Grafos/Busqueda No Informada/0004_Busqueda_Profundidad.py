def busqueda_en_profundidad(grafo, inicio, objetivo):
    # Usamos una pila (LIFO) para mantener los nodos pendientes
    pila = [(inicio, [inicio])]  # Cada tupla contiene el nodo actual y el camino
    visitados = set()

    while pila:
        nodo_actual, camino = pila.pop()

        # Si encontramos el objetivo, devolvemos el camino
        if nodo_actual == objetivo:
            return camino
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))

    return None  # Si no se encuentra el objetivo

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
objetivo = 'F'

camino = busqueda_en_profundidad(grafo, inicio, objetivo)
print(f"Camino encontrado: {camino}")

#Camino encontrado: ['A', 'C', 'F']