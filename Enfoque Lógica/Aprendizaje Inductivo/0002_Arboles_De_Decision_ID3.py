"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Árboles de Decisión - ID3

Este código implementa el algoritmo ID3 (Iterative Dichotomiser 3),
un método de aprendizaje supervisado que genera árboles de decisión
basado en la métrica de ganancia de información (entropía).

Los árboles de decisión permiten clasificar datos nuevos mediante 
preguntas binarias basadas en atributos.

Este ejemplo NO usa librerías externas para facilitar su ejecución.
"""

import math
from collections import Counter

# -----------------------------------
# FUNCIONES AUXILIARES: ENTROPÍA E ID3
# -----------------------------------

def entropia(conj_clases):
    """
    Calcula la entropía del conjunto de etiquetas (clases).
    """
    total = len(conj_clases)
    conteo = Counter(conj_clases)
    return -sum((count/total) * math.log2(count/total) for count in conteo.values())

def ganancia_informacion(data, atributo, clase_idx):
    """
    Calcula la ganancia de información de un atributo.
    """
    total = len(data)
    valores = set(fila[atributo] for fila in data)
    entropia_total = entropia([fila[clase_idx] for fila in data])
    entropia_condicional = 0

    for valor in valores:
        subconjunto = [fila for fila in data if fila[atributo] == valor]
        peso = len(subconjunto) / total
        entropia_valor = entropia([fila[clase_idx] for fila in subconjunto])
        entropia_condicional += peso * entropia_valor

    return entropia_total - entropia_condicional

def id3(data, atributos, clase_idx):
    """
    Algoritmo ID3 para construir un árbol de decisión recursivamente.
    """
    clases = [fila[clase_idx] for fila in data]

    # Caso 1: todas las clases son iguales
    if clases.count(clases[0]) == len(clases):
        return clases[0]

    # Caso 2: no quedan atributos para dividir
    if not atributos:
        return Counter(clases).most_common(1)[0][0]

    # Elegir el mejor atributo
    mejor = max(atributos, key=lambda a: ganancia_informacion(data, a, clase_idx))

    # Crear el nodo del árbol
    arbol = {mejor: {}}
    valores = set(fila[mejor] for fila in data)

    for valor in valores:
        subconjunto = [fila for fila in data if fila[mejor] == valor]
        if not subconjunto:
            arbol[mejor][valor] = Counter(clases).most_common(1)[0][0]
        else:
            nuevos_atributos = [a for a in atributos if a != mejor]
            arbol[mejor][valor] = id3(subconjunto, nuevos_atributos, clase_idx)

    return arbol

def imprimir_arbol(arbol, indent=0):
    """
    Imprime el árbol de forma legible.
    """
    if isinstance(arbol, dict):
        for atributo, ramas in arbol.items():
            for valor, subarbol in ramas.items():
                print("  " * indent + f"[{atributo} = {valor}]")
                imprimir_arbol(subarbol, indent + 1)
    else:
        print("  " * indent + f"=> Clase: {arbol}")

# -----------------------------------
# EJEMPLO DE USO
# -----------------------------------

# Datos: Outlook, Temp, Humidity, Windy, Play
datos = [
    ['Sunny', 'Hot', 'High', False, 'No'],
    ['Sunny', 'Hot', 'High', True, 'No'],
    ['Overcast', 'Hot', 'High', False, 'Yes'],
    ['Rain', 'Mild', 'High', False, 'Yes'],
    ['Rain', 'Cool', 'Normal', False, 'Yes'],
    ['Rain', 'Cool', 'Normal', True, 'No'],
    ['Overcast', 'Cool', 'Normal', True, 'Yes'],
    ['Sunny', 'Mild', 'High', False, 'No'],
    ['Sunny', 'Cool', 'Normal', False, 'Yes'],
    ['Rain', 'Mild', 'Normal', False, 'Yes'],
    ['Sunny', 'Mild', 'Normal', True, 'Yes'],
    ['Overcast', 'Mild', 'High', True, 'Yes'],
    ['Overcast', 'Hot', 'Normal', False, 'Yes'],
    ['Rain', 'Mild', 'High', True, 'No'],
]

atributos = [0, 1, 2, 3]  # índices de Outlook, Temp, Humidity, Windy
clase_idx = 4  # índice de la clase "Play"

# Entrenamiento del árbol de decisión
arbol_decision = id3(datos, atributos, clase_idx)

# Impresión del árbol generado
print("Árbol de Decisión (ID3):\n")
imprimir_arbol(arbol_decision)
