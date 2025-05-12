"""
Prácticas de Inteligencia Artificial
Búsqueda de la Política: Método de Iteración de Políticas

Este programa implementa el algoritmo de **Iteración de Políticas**, un método para encontrar la política óptima de un agente en un entorno de Aprendizaje por Refuerzo. 
El agente busca aprender cuál es la acción óptima a tomar en cada estado para maximizar la recompensa esperada.

En la **Iteración de Políticas**:
1. Se comienza con una política arbitraria.
2. Se evalúa la política (se calcula el valor de cada estado bajo la política actual).
3. Se mejora la política (se selecciona la acción que maximiza la recompensa esperada en cada estado).

Este proceso se repite hasta que la política converge a la óptima.

"""

import random

# Definir el entorno (un pequeño grid de 3x3)
def entorno():
    """
    Define un entorno simple con 3 estados y 2 acciones.
    El agente se mueve en una cuadrícula de 3x3, con las siguientes acciones:
    - 0: Arriba
    - 1: Abajo
    - 2: Izquierda
    - 3: Derecha

    Se asignan recompensas a las acciones y transiciones entre estados.
    """
    # Definición de los estados, acciones y recompensas
    estados = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    acciones = [0, 1, 2, 3]  # Arriba, Abajo, Izquierda, Derecha
    
    # Recompensas en cada estado y acción
    recompensas = {
        0: [0, 0, -1, 1],
        1: [0, 0, 0, 0],
        2: [0, 0, 1, -1],
        3: [0, 0, 0, 0],
        4: [0, 0, 0, 0],
        5: [0, 0, 0, 0],
        6: [0, 0, 1, -1],
        7: [0, 0, 0, 0],
        8: [0, 0, 0, 0]
    }
    
    # Transiciones de estado
    transiciones = {
        0: [3, 3, 0, 1],  # Arriba, Abajo, Izquierda, Derecha
        1: [4, 4, 1, 2],
        2: [5, 5, 2, 3],
        3: [6, 6, 3, 0],
        4: [7, 7, 4, 1],
        5: [8, 8, 5, 2],
        6: [6, 6, 6, 3],
        7: [7, 7, 7, 4],
        8: [8, 8, 8, 5]
    }
    
    return estados, acciones, recompensas, transiciones

# Evaluación de la Política: Calcula el valor de cada estado
def evaluacion_politica(politica, V, estados, recompensas, transiciones, gamma=0.9):
    """
    Evalúa la política para obtener los valores de cada estado.
    
    :param politica: Política actual (acción a tomar en cada estado)
    :param V: Valores actuales de los estados
    :param estados: Lista de estados
    :param recompensas: Diccionario de recompensas por acción en cada estado
    :param transiciones: Diccionario de transiciones entre estados por acción
    :param gamma: Factor de descuento
    :return: El valor actualizado de cada estado
    """
    for estado in estados:
        accion = politica[estado]
        siguiente_estado = transiciones[estado][accion]
        V[estado] = recompensas[estado][accion] + gamma * V[siguiente_estado]
    return V

# Mejorar la política: Selecciona la acción que maximiza el valor esperado
def mejorar_politica(politica, V, estados, recompensas, transiciones):
    """
    Mejora la política seleccionando la acción que maximiza el valor esperado.
    
    :param politica: Política actual
    :param V: Valores de los estados
    :param estados: Lista de estados
    :param recompensas: Diccionario de recompensas por acción
    :param transiciones: Diccionario de transiciones de estados
    :return: La política mejorada
    """
    politica_mejorada = politica.copy()
    for estado in estados:
        mejor_accion = None
        max_valor = float('-inf')
        for accion in range(len(recompensas[estado])):
            siguiente_estado = transiciones[estado][accion]
            valor_esperado = recompensas[estado][accion] + V[siguiente_estado]
            if valor_esperado > max_valor:
                max_valor = valor_esperado
                mejor_accion = accion
        politica_mejorada[estado] = mejor_accion
    return politica_mejorada

# Algoritmo de Iteración de Políticas
def iteracion_politicas():
    """
    Implementación del algoritmo de Iteración de Políticas para encontrar la política óptima.
    """
    # Inicializar el entorno
    estados, acciones, recompensas, transiciones = entorno()
    
    # Inicialización de la política y valores
    politica = {estado: random.choice(acciones) for estado in estados}
    V = {estado: 0 for estado in estados}
    
    # Iteración de políticas
    politica_estable = False
    while not politica_estable:
        # Evaluación de la política
        V = evaluacion_politica(politica, V, estados, recompensas, transiciones)
        
        # Mejora de la política
        politica_nueva = mejorar_politica(politica, V, estados, recompensas, transiciones)
        
        # Verificar si la política ha convergido
        if politica == politica_nueva:
            politica_estable = True
        politica = politica_nueva
    
    return politica, V

# Ejecutar el algoritmo
politica_optima, valores_optimos = iteracion_politicas()

# Imprimir los resultados
print("Política Óptima:")
for estado, accion in politica_optima.items():
    print(f"Estado {estado}: Acción {accion}")

print("\nValores Óptimos de los Estados:")
for estado, valor in valores_optimos.items():
    print(f"Estado {estado}: Valor {valor}")
