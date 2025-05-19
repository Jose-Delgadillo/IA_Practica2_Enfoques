"""
Prácticas de Inteligencia Artificial
Enfoque: Planificación
Subtema: Grafos de Planificación (GRAPHPLAN)

Este programa implementa una versión simplificada del algoritmo GRAPHPLAN, que utiliza
una estructura en forma de grafo para representar estados y acciones en niveles alternos,
con el objetivo de encontrar un plan para alcanzar un conjunto de objetivos a partir
de un estado inicial.

GRAPHPLAN construye un grafo de planificación con niveles de proposiciones y niveles
de acciones, detectando exclusiones mutuas para evitar conflictos. Busca un plan
por medio de búsqueda regresiva sobre el grafo.
"""

from collections import defaultdict

# Estado inicial: conjunto de hechos verdaderos
estado_inicial = {"robot_en(pasillo)", "puerta_abierta(sala)", "en(caja, sala)"}

# Objetivo a alcanzar
objetivo = {"en(caja, pasillo)"}

# Definición de acciones con precondiciones y efectos
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

def acciones_applicables(proposiciones):
    """
    Devuelve la lista de acciones aplicables dado un conjunto de proposiciones.
    Una acción es aplicable si todas sus precondiciones están en proposiciones.
    """
    aplicables = []
    for a in acciones:
        if a["precondiciones"].issubset(proposiciones):
            aplicables.append(a)
    return aplicables

def construir_grafo_planificacion(estado_inicial, max_niveles=10):
    """
    Construye el grafo de planificación: niveles alternos de proposiciones y acciones.
    - Cada nivel de proposiciones es un conjunto de hechos posibles.
    - Cada nivel de acciones contiene las acciones aplicables en el nivel anterior.
    Se para si el nivel de proposiciones no cambia respecto al anterior (estabilidad)
    o si se alcanza el máximo de niveles.
    """
    niveles_proposiciones = [set(estado_inicial)]
    niveles_acciones = []

    for nivel in range(max_niveles):
        # Acciones aplicables al nivel actual de proposiciones
        aplicables = acciones_applicables(niveles_proposiciones[-1])
        niveles_acciones.append(set(a["nombre"] for a in aplicables))

        # Nuevo nivel de proposiciones: efectos de acciones aplicables + proposiciones previas
        nuevo_nivel_prop = set(niveles_proposiciones[-1])
        for a in aplicables:
            nuevo_nivel_prop.update(a["efectos_añadir"])

        # Si no hay cambios, el grafo está estable
        if nuevo_nivel_prop == niveles_proposiciones[-1]:
            break
        niveles_proposiciones.append(nuevo_nivel_prop)

    return niveles_proposiciones, niveles_acciones

def es_objetivo_alcanzable(objetivo, nivel_proposiciones):
    """
    Verifica si el objetivo está contenido en el conjunto de proposiciones
    del nivel dado.
    """
    return objetivo.issubset(nivel_proposiciones)

def buscar_plan(niveles_proposiciones, niveles_acciones, objetivo, nivel_actual):
    """
    Busca recursivamente un plan regresivo desde el nivel actual hacia atrás.
    Devuelve lista de acciones o None si no se encuentra plan.
    """

    # Caso base: nivel 0 (estado inicial)
    if nivel_actual == 0:
        # El estado inicial debe contener el objetivo para éxito
        if objetivo.issubset(niveles_proposiciones[0]):
            return []
        else:
            return None

    # Conjunto de proposiciones en el nivel actual
    prop_nivel = niveles_proposiciones[nivel_actual]
    # Conjunto de acciones en el nivel anterior
    acciones_nivel = niveles_acciones[nivel_actual - 1]

    # Intentamos cubrir cada proposición del objetivo con una acción que la produzca
    plan_acciones = []

    for objetivo_simple in objetivo:
        # Buscar acciones que añadan la proposición objetivo_simple
        acciones_posibles = []
        for a in acciones:
            if a["nombre"] in acciones_nivel and objetivo_simple in a["efectos_añadir"]:
                acciones_posibles.append(a)

        if not acciones_posibles:
            # No hay acción que produzca esta proposición en este nivel
            return None

        # Intentamos usar la primera acción válida (simplificación)
        accion_elegida = acciones_posibles[0]
        plan_acciones.append(accion_elegida["nombre"])

        # Los precondiciones de esta acción se vuelven el nuevo objetivo a alcanzar en nivel anterior
        subplan = buscar_plan(niveles_proposiciones, niveles_acciones,
                              accion_elegida["precondiciones"], nivel_actual - 1)
        if subplan is None:
            return None
        plan_acciones = subplan + plan_acciones

    # Eliminar duplicados manteniendo orden
    plan_final = []
    [plan_final.append(x) for x in plan_acciones if x not in plan_final]

    return plan_final

if __name__ == "__main__":
    print("Estado inicial:", estado_inicial)
    print("Objetivo:", objetivo)

    niveles_prop, niveles_acc = construir_grafo_planificacion(estado_inicial)

    # Mostrar niveles generados
    print("\nNiveles de proposiciones:")
    for i, nivel in enumerate(niveles_prop):
        print(f"Nivel {i}: {nivel}")

    print("\nNiveles de acciones:")
    for i, nivel in enumerate(niveles_acc):
        print(f"Nivel {i}: {nivel}")

    # Verificar si objetivo es alcanzable en el último nivel
    if not es_objetivo_alcanzable(objetivo, niveles_prop[-1]):
        print("\nNo se puede alcanzar el objetivo con el grafo construido.")
    else:
        plan = buscar_plan(niveles_prop, niveles_acc, objetivo, len(niveles_prop) - 1)
        if plan is None:
            print("\nNo se encontró un plan que alcance el objetivo.")
        else:
            print("\nPlan encontrado (orden lineal simplificado):")
            for paso, accion in enumerate(plan, 1):
                print(f"{paso}. {accion}")
