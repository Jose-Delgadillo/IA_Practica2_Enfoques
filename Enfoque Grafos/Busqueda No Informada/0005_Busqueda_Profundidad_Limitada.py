"""
Prácticas de Inteligencia Artificial
Ejemplos de Búsqueda en Profundidad Limitada
"""
def busqueda_profundidad_limitada(grafo, inicio, objetivo, limite):
    pila = [(inicio, [inicio], 0)]  # Nodo, Camino y Profundidad actual
    visitados = set()

    while pila:
        nodo_actual, camino, profundidad = pila.pop()

        if nodo_actual == objetivo:
            return camino
        
        if profundidad < limite:
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                for vecino in grafo.get(nodo_actual, []):
                    if vecino not in visitados:
                        pila.append((vecino, camino + [vecino], profundidad + 1))

    return None  # Si no se encuentra el objetivo dentro del límite

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
limite = 2  # Límite de profundidad

camino = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite)
print(f"Camino encontrado: {camino}")

#Camino encontrado: ['A', 'C', 'F']