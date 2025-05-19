"""
Prácticas de Inteligencia Artificial  
Enfoque: Resolución de Problemas  
Técnica: Algoritmos de Búsqueda Local

Los algoritmos de búsqueda local son métodos que exploran el espacio de soluciones
moviéndose desde un estado hacia vecinos cercanos, con el objetivo de encontrar
una solución óptima o aceptable.

Este programa implementa el algoritmo de **ascenso de colinas (hill climbing)**,
que intenta mejorar la solución paso a paso, siempre eligiendo un vecino mejor.

Ejemplo: Optimización de la función f(x) = -x^2 + 4x (máximo en x = 2)
"""

import random

# ----------------------------
# Función objetivo
# ----------------------------

def funcion_objetivo(x):
    """Función a maximizar"""
    return -x**2 + 4*x

# ----------------------------
# Vecinos
# ----------------------------

def generar_vecinos(x, paso=0.1):
    """
    Genera dos vecinos cercanos al estado actual: uno a la izquierda y otro a la derecha.
    """
    return [x - paso, x + paso]

# ----------------------------
# Algoritmo de Ascenso de Colinas
# ----------------------------

def ascenso_de_colinas(x_inicial, max_iter=1000, paso=0.1):
    """
    Implementación del algoritmo de hill climbing.
    Comienza desde un punto aleatorio y avanza hacia donde la función mejora.
    """
    x_actual = x_inicial
    valor_actual = funcion_objetivo(x_actual)

    for i in range(max_iter):
        vecinos = generar_vecinos(x_actual, paso)
        mejor_vecino = x_actual
        mejor_valor = valor_actual

        for vecino in vecinos:
            valor_vecino = funcion_objetivo(vecino)
            if valor_vecino > mejor_valor:
                mejor_vecino = vecino
                mejor_valor = valor_vecino

        if mejor_valor == valor_actual:
            # No se encontró mejora
            break

        x_actual = mejor_vecino
        valor_actual = mejor_valor

    return x_actual, valor_actual

# ----------------------------
# Ejecución del algoritmo
# ----------------------------

# Se parte de un punto aleatorio entre 0 y 4
x_inicial = random.uniform(0, 4)
x_max, valor_max = ascenso_de_colinas(x_inicial)

print(f"Punto inicial: {x_inicial:.4f}")
print(f"Máximo encontrado en x = {x_max:.4f}")
print(f"Valor de la función: f(x) = {valor_max:.4f}")
