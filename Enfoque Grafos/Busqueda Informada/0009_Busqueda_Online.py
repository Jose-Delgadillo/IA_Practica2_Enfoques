"""
Prácticas de Inteligencia Artificial
Búsqueda Informada: Búsqueda Online (Descubrimiento progresivo)
"""

# Grafo oculto (supongamos que el agente no lo conoce completamente)
grafo_completo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# Simula el entorno donde el agente puede consultar vecinos del nodo actual
def obtener_vecinos(nodo):
    return grafo_completo.get(nodo, [])

# Búsqueda online estilo DFS (profundidad), construyendo el grafo en tiempo real
def busqueda_online(inicio, objetivo):
    visitados = set()
    frontera = [(inicio, [inicio])]
    grafo_descubierto = {}  # Mapa que el agente construye poco a poco

    while frontera:
        nodo_actual, camino = frontera.pop()

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)
        vecinos = obtener_vecinos(nodo_actual)
        grafo_descubierto[nodo_actual] = vecinos

        if nodo_actual == objetivo:
            print("\nGrafo descubierto:")
            for nodo, conexiones in grafo_descubierto.items():
                print(f"{nodo}: {conexiones}")
            return camino

        for vecino in vecinos:
            if vecino not in visitados:
                frontera.append((vecino, camino + [vecino]))

    return None

# ============ Ejecutar búsqueda ============
inicio = 'A'
objetivo = 'F'

camino = busqueda_online(inicio, objetivo)

print("\n===== Búsqueda Online =====")
print(f"Camino encontrado: {camino}")
