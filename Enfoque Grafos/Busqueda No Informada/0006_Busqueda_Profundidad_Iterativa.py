"""
Prácticas de Inteligencia Artificial
Ejemplos de Búsqueda en Profundidad Iterativa
"""
def busqueda_profundidad_limitada(grafo, nodo_actual, objetivo, limite):
    if nodo_actual == objetivo:
        return [nodo_actual]
    if limite == 0:
        return None

    for vecino in grafo.get(nodo_actual, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite - 1)
        if resultado:
            return [nodo_actual] + resultado

    return None

def busqueda_profundidad_iterativa(grafo, inicio, objetivo):
    profundidad = 0
    while True:
        resultado = busqueda_profundidad_limitada(grafo, inicio, objetivo, profundidad)
        if resultado:
            return resultado
        profundidad += 1

# Ejemplo de grafo:
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

camino = busqueda_profundidad_iterativa(grafo, inicio, objetivo)
print(f"Camino encontrado: {camino}")

#Camino encontrado: ['A', 'C', 'F']