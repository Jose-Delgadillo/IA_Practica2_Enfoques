"""
Prácticas de Inteligencia Artificial
Enfoque: Planificación
Subtema: Espacio de Estados

Este programa ilustra el concepto de espacio de estados en problemas de planificación.
El espacio de estados es el conjunto de todas las configuraciones posibles del mundo
que pueden alcanzarse a través de la aplicación de acciones desde un estado inicial.
Cada estado está representado por un conjunto de hechos (literales), y las acciones
modifican estos estados.

La búsqueda en el espacio de estados consiste en explorar estos estados hasta encontrar
uno que cumpla con el objetivo deseado. Aquí implementamos un sencillo explorador de
espacio de estados para un problema de manipulación de objetos con un robot.
"""

from copy import deepcopy

# Estado inicial: conjunto de hechos verdaderos
estado_inicial = {"robot_en(pasillo)", "puerta_abierta(sala)", "en(caja, sala)"}

# Objetivo a alcanzar
objetivo = {"en(caja, pasillo)"}

# Definición de acciones disponibles
acciones = [
    {
        "nombre": "mover_robot_sala_a_pasillo",
        "precondiciones": {"robot_en(sala)", "puerta_abierta(sala)"},
        "efectos_añadir": {"robot_en(pasillo)"},
        "efectos_eliminar": {"robot_en(sala)"}
    },
    {
        "nombre": "mover_robot_pasillo_a_sala",
        "precondiciones": {"robot_en(pasillo)", "puerta_abierta(sala)"},
        "efectos_añadir": {"robot_en(sala)"},
        "efectos_eliminar": {"robot_en(pasillo)"}
    },
    {
        "nombre": "mover_caja_sala_a_pasillo",
        "precondiciones": {"robot_en(sala)", "en(caja, sala)"},
        "efectos_añadir": {"en(caja, pasillo)"},
        "efectos_eliminar": {"en(caja, sala)"}
    }
]

def aplicar_accion(estado, accion):
    """
    Aplica una acción a un estado dado si se cumplen las precondiciones.
    Devuelve el nuevo estado o None si la acción no es aplicable.
    """
    if not accion["precondiciones"].issubset(estado):
        return None
    nuevo_estado = deepcopy(estado)
    nuevo_estado.difference_update(accion["efectos_eliminar"])
    nuevo_estado.update(accion["efectos_añadir"])
    return nuevo_estado

def explorar_espacio_estados(estado_actual, objetivo, acciones, visitados=None, plan=[]):
    """
    Función recursiva para explorar el espacio de estados y encontrar un plan
    que lleve del estado actual al objetivo.
    """
    if visitados is None:
        visitados = set()
    # Convertimos el conjunto a frozenset para poder usarlo en visitados
    estado_key = frozenset(estado_actual)
    if estado_key in visitados:
        return None
    visitados.add(estado_key)

    if objetivo.issubset(estado_actual):
        return plan

    for accion in acciones:
        nuevo_estado = aplicar_accion(estado_actual, accion)
        if nuevo_estado is not None:
            resultado = explorar_espacio_estados(nuevo_estado, objetivo, acciones, visitados, plan + [accion["nombre"]])
            if resultado is not None:
                return resultado
    return None

if __name__ == "__main__":
    print("Estado inicial:", estado_inicial)
    print("Objetivo:", objetivo)
    plan = explorar_espacio_estados(estado_inicial, objetivo, acciones)
    if plan:
        print("\nPlan encontrado para alcanzar el objetivo:")
        for i, paso in enumerate(plan, 1):
            print(f"  Paso {i}: {paso}")
    else:
        print("\nNo se encontró un plan que alcance el objetivo.")
