"""
Prácticas de Inteligencia Artificial
Ejemplo de Heurísticas
"""

# Definimos el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos las heurísticas (estimaciones de costo al objetivo)
heuristicas = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Imprimimos las heurísticas
print("Heurísticas por nodo:")
for nodo, h in heuristicas.items():
    print(f"  Nodo {nodo}: {h}")

#La heurística (heuristicas) representa cuánto "falta" (aproximadamente) desde cada nodo hasta el objetivo (en este caso, F).
#Heurística de F es 0, porque ya es el objetivo.
#Nodo A: 6 - Nodo B: 4 - Nodo C: 4 - Nodo D: 2 - Nodo E: 1 - Nodo F: 0