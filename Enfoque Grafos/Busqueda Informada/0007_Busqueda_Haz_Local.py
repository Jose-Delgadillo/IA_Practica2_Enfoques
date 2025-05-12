"""
Prácticas de Inteligencia Artificial
Búsqueda Informada: Búsqueda de Haz Local (Local Beam Search)
"""

def busqueda_haz_local(grafo, heuristicas, inicio, objetivo, k=2, max_iteraciones=10):
    """
    Algoritmo de Búsqueda de Haz Local.
    - grafo: estructura de conexiones del grafo.
    - heuristicas: estimación de costo a objetivo para cada nodo.
    - inicio: nodo inicial.
    - objetivo: nodo destino.
    - k: número de trayectorias que se mantienen en cada iteración (tamaño del haz).
    - max_iteraciones: número máximo de ciclos.
    """
    # Inicializar el haz con k copias del nodo inicial
    haz = [[inicio] for _ in range(k)]

    for iteracion in range(max_iteraciones):
        # Generar todos los vecinos posibles a partir del haz actual
        candidatos = []

        for camino in haz:
            nodo_actual = camino[-1]
            vecinos = grafo.get(nodo_actual, [])
            for vecino in vecinos:
                if vecino not in camino:  # evitar ciclos
                    nuevo_camino = camino + [vecino]
                    candidatos.append(nuevo_camino)

        if not candidatos:
            break  # No hay más vecinos, termina la búsqueda

        # Ordenar candidatos por heurística del último nodo
        candidatos.sort(key=lambda c: heuristicas[c[-1]])

        # Verificar si el mejor candidato llega al objetivo
        if candidatos[0][-1] == objetivo:
            return candidatos[0], True

        # Mantener los k mejores caminos
        haz = candidatos[:k]

    return haz[0], haz[0][-1] == objetivo  # devolver el mejor intento


# ============ Definir grafo y heurísticas ============
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

# ============ Ejecutar búsqueda ============
camino, exito = busqueda_haz_local(grafo, heuristicas, inicio, objetivo, k=2)

# ============ Mostrar resultado ============
print("\n===== Búsqueda de Haz Local =====")
print(f"Camino seguido: {camino}")
print(f"¿Se llegó al objetivo?: {'Sí' if exito else 'No'}")
