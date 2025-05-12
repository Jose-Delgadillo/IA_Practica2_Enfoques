"""
Prácticas de Inteligencia Artificial
Búsqueda Informada: Ascensión de Colinas (Hill Climbing)
"""

def ascension_colinas(grafo, heuristicas, inicio, objetivo):
    """
    Algoritmo de Ascensión de Colinas (Hill Climbing).
    En cada paso se elige el vecino con la heurística más baja (más prometedor),
    sin considerar el costo total del camino.
    """
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = grafo.get(actual, [])
        if not vecinos:
            # No hay vecinos para explorar: punto muerto
            break

        # Elegimos el vecino con la mejor heurística (menor)
        mejor_vecino = min(vecinos, key=lambda nodo: heuristicas.get(nodo, float('inf')))
        
        # Si el vecino es mejor que el actual, avanzamos
        if heuristicas[mejor_vecino] < heuristicas[actual]:
            actual = mejor_vecino
            camino.append(actual)
        else:
            # No hay mejora: llegamos a un máximo local
            break

    # Retornamos el camino seguido y si se llegó o no al objetivo
    exito = actual == objetivo
    return camino, exito


# =============== Definición del grafo y heurísticas ===============
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heurísticas: valores más bajos indican estar más cerca del objetivo
heuristicas = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1  # Objetivo
}

# =================== Ejecutar la búsqueda ===================
inicio = 'A'
objetivo = 'F'

camino, exito = ascension_colinas(grafo, heuristicas, inicio, objetivo)

# =================== Mostrar resultados ===================
print("\n===== Búsqueda Ascensión de Colinas =====")
print(f"Camino seguido: {camino}")
print(f"¿Se llegó al objetivo?: {'Sí' if exito else 'No (máximo local)'}")

#Siempre elige al vecino más prometedor (el de menor heurística).
#No retrocede ni evalúa alternativas si elige mal.
#Puede quedar atrapado en un máximo local, si ningún vecino mejora la situación actual.