"""
Prácticas de Inteligencia Artificial
Búsquedas Informadas: A* y AO*
"""

import heapq  # Módulo para manejar colas de prioridad (usado en A*)

# =================== Búsqueda A* ===================
def busqueda_a_estrella(grafo, heuristicas, inicio, objetivo):
    """
    Algoritmo de búsqueda A*
    Usa una cola de prioridad para expandir los nodos con menor costo + heurística
    """

    # Cola de prioridad: cada elemento es una tupla (f, g, nodo_actual, camino)
    # f = g + h, g = costo acumulado real, h = heurística estimada
    cola = [(heuristicas[inicio], 0, inicio, [inicio])]
    visitados = set()

    while cola:
        # Sacamos el nodo con menor f (prioridad)
        prioridad, costo_actual, nodo_actual, camino = heapq.heappop(cola)

        # Si llegamos al objetivo, devolvemos el camino y costo total
        if nodo_actual == objetivo:
            return camino, costo_actual
        
        # Si aún no fue visitado, lo procesamos
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Expandimos los vecinos
            for vecino, costo in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nuevo_costo = costo_actual + costo
                    prioridad = nuevo_costo + heuristicas[vecino]  # f(n) = g(n) + h(n)
                    heapq.heappush(cola, (prioridad, nuevo_costo, vecino, camino + [vecino]))
    
    # Si no hay camino posible
    return None, float('inf')

# =================== Búsqueda AO* ===================
def ao_star(grafo, heuristicas, nodo_actual, solucion, visitados):
    """
    Algoritmo AO* (AND-OR): Encuentra la estrategia óptima para resolver el problema
    """

    # Si ya lo resolvimos antes, regresamos el resultado
    if nodo_actual in visitados:
        return solucion.get(nodo_actual, None)

    visitados.add(nodo_actual)

    # Si no tiene hijos, es nodo terminal: su costo es solo su heurística
    if not grafo.get(nodo_actual):
        solucion[nodo_actual] = ([], heuristicas[nodo_actual])
        return solucion[nodo_actual]
    
    mejor_costo = float('inf')   # Inicializamos con costo infinito
    mejor_camino = []            # Para guardar mejor grupo de hijos

    # Evaluamos cada conjunto de hijos (pueden ser múltiples en AO*)
    for opciones in grafo[nodo_actual]:
        costo_total = 0
        camino_actual = []

        for hijo in opciones:
            subcamino, subcosto = ao_star(grafo, heuristicas, hijo, solucion, visitados)
            camino_actual.append(hijo)
            costo_total += subcosto  # Sumamos el costo de todos los hijos requeridos

        # Si encontramos una mejor opción, la actualizamos
        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_camino = camino_actual

    # Guardamos la mejor decisión para este nodo
    solucion[nodo_actual] = (mejor_camino, heuristicas[nodo_actual] + mejor_costo)
    return solucion[nodo_actual]

def encontrar_solucion_ao_star(grafo, heuristicas, inicio):
    """
    Controlador para iniciar la búsqueda AO*
    """
    solucion = {}      # Diccionario donde guardamos la mejor solución de cada nodo
    visitados = set()  # Para evitar ciclos o repetir nodos
    ao_star(grafo, heuristicas, inicio, solucion, visitados)
    return solucion

# =================== Definición del Grafo ===================
# Grafo con costos para A*
grafo_con_costos = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Grafo tipo AND-OR para AO*
# Aquí cada valor es una lista de posibles grupos de hijos
# Cada grupo representa una opción a tomar (puede ser un solo nodo o varios)
grafo_ao = {
    'A': [['B', 'C']],   # Para resolver A, debo resolver B y C juntos
    'B': [['D']],        # Para resolver B, debo resolver D
    'C': [['E', 'F']],   # Para resolver C, debo resolver E y F juntos
    'D': [],             # D, E, F son terminales
    'E': [],
    'F': []
}

# Heurísticas para cada nodo
# Indican una estimación del costo desde ese nodo al objetivo
heuristicas = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# =================== Ejecutar Búsquedas ===================
inicio = 'A'
objetivo = 'F'

# ----- Ejecutamos búsqueda A* -----
camino_aestrella, costo_total = busqueda_a_estrella(grafo_con_costos, heuristicas, inicio, objetivo)
print("\n===== Búsqueda A* =====")
print(f"Camino encontrado A*: {camino_aestrella}")
print(f"Costo total A*: {costo_total}")

# ----- Ejecutamos búsqueda AO* -----
solucion_ao = encontrar_solucion_ao_star(grafo_ao, heuristicas, inicio)
print("\n===== Búsqueda AO* =====")
for nodo, (hijos, costo) in solucion_ao.items():
    print(f"Nodo {nodo}: sigue a {hijos} con costo total {costo}")
