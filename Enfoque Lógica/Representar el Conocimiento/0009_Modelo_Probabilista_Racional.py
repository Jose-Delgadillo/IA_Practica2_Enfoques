"""
Prácticas de Inteligencia Artificial
Enfoque: Razonamiento Probabilístico
Subtema: Modelo Probabilista Racional

Este programa ilustra un modelo probabilista racional para agentes inteligentes,
donde el agente elige la acción que maximiza la probabilidad de alcanzar un objetivo
dado el estado actual del entorno y un modelo probabilístico de las transiciones.

El modelo asume:
- Un conjunto de estados posibles.
- Un conjunto de acciones posibles.
- Un modelo probabilístico P(s' | s, a) que da la probabilidad de transicionar al estado s' al tomar acción a en estado s.
- Una función objetivo que indica el estado deseado.

El agente calcula para cada acción la probabilidad de alcanzar el estado objetivo desde el estado actual.
"""

# Definición de estados (por simplicidad estados representados como strings)
estados = ["s0", "s1", "s2", "s3", "objetivo"]

# Definición de acciones posibles
acciones = ["a0", "a1"]

# Modelo probabilístico de transición: P(s' | s, a)
# Representado como un diccionario anidado:
# transiciones[estado_actual][accion] = lista de (estado_siguiente, probabilidad)
transiciones = {
    "s0": {
        "a0": [("s1", 0.7), ("s2", 0.3)],
        "a1": [("s2", 1.0)]
    },
    "s1": {
        "a0": [("objetivo", 0.9), ("s3", 0.1)],
        "a1": [("s0", 0.4), ("objetivo", 0.6)]
    },
    "s2": {
        "a0": [("s3", 1.0)],
        "a1": [("objetivo", 0.8), ("s1", 0.2)]
    },
    "s3": {
        "a0": [("objetivo", 1.0)],
        "a1": [("s0", 0.5), ("s2", 0.5)]
    },
    "objetivo": {
        "a0": [("objetivo", 1.0)],
        "a1": [("objetivo", 1.0)]
    }
}

# Estado objetivo que queremos alcanzar
estado_objetivo = "objetivo"

def probabilidad_alcanzar_objetivo(estado_actual, accion, profundidad=3):
    """
    Calcula recursivamente la probabilidad de alcanzar el estado objetivo desde
    un estado dado al tomar una acción específica, explorando transiciones
    hasta una profundidad límite para evitar loops infinitos.

    Args:
        estado_actual (str): estado actual del agente.
        accion (str): acción a evaluar.
        profundidad (int): profundidad máxima de exploración recursiva.

    Returns:
        float: probabilidad estimada de alcanzar el estado objetivo.
    """
    if profundidad == 0:
        # Limitar profundidad para evitar recursión infinita
        return 0.0

    # Si ya estamos en el estado objetivo, probabilidad es 1
    if estado_actual == estado_objetivo:
        return 1.0

    # Obtener lista de transiciones posibles desde estado_actual con acción
    transiciones_posibles = transiciones.get(estado_actual, {}).get(accion, [])

    prob_total = 0.0

    # Para cada posible estado siguiente y su probabilidad,
    # calculamos la probabilidad de alcanzar el objetivo desde allí,
    # y la ponderamos por la probabilidad de la transición.
    for (estado_siguiente, prob_transicion) in transiciones_posibles:
        # Si el estado siguiente es el objetivo, sumar probabilidad directa
        if estado_siguiente == estado_objetivo:
            prob_total += prob_transicion
        else:
            # Recursión: elegir la mejor acción desde el nuevo estado para maximizar probabilidad
            mejor_prob_accion = 0.0
            for a in acciones:
                p = probabilidad_alcanzar_objetivo(estado_siguiente, a, profundidad-1)
                if p > mejor_prob_accion:
                    mejor_prob_accion = p
            prob_total += prob_transicion * mejor_prob_accion

    return prob_total

def elegir_mejor_accion(estado_actual):
    """
    Dado un estado actual, evalúa todas las acciones posibles y selecciona
    aquella con la mayor probabilidad de alcanzar el estado objetivo.

    Args:
        estado_actual (str): estado en el que se encuentra el agente.

    Returns:
        tuple: (mejor_accion (str), probabilidad (float))
    """
    mejor_accion = None
    mejor_prob = -1

    for accion in acciones:
        p = probabilidad_alcanzar_objetivo(estado_actual, accion)
        print(f"Acción '{accion}' tiene probabilidad estimada de {p:.4f} de alcanzar el objetivo desde estado '{estado_actual}'.")
        if p > mejor_prob:
            mejor_prob = p
            mejor_accion = accion

    return mejor_accion, mejor_prob

if __name__ == "__main__":
    estado_inicial = "s0"
    print(f"Estado inicial: {estado_inicial}")
    accion_optima, prob_optima = elegir_mejor_accion(estado_inicial)
    print(f"\nLa mejor acción desde el estado '{estado_inicial}' es '{accion_optima}' con probabilidad {prob_optima:.4f} de alcanzar el objetivo.")
