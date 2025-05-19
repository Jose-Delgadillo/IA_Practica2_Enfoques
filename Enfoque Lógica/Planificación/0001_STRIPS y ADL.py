"""
Prácticas de Inteligencia Artificial
Enfoque: Planificación
Subtema: Algoritmos de Planificación - STRIPS y ADL

Este programa ilustra una versión simplificada de un planificador STRIPS, que es un formalismo
clásico para la planificación automática. 

STRIPS representa:
- Estados del mundo como conjuntos de hechos (literales).
- Operadores (acciones) con precondiciones, efectos que agregan hechos y efectos que eliminan hechos.
- El objetivo es encontrar una secuencia de acciones que, aplicadas desde el estado inicial,
  lleven a un estado donde se cumpla un conjunto de objetivos.

ADL (Action Description Language) extiende STRIPS permitiendo condiciones y efectos más complejos,
pero aquí implementamos el núcleo básico tipo STRIPS para fines didácticos.
"""

from copy import deepcopy

# Definición del estado inicial: conjunto de hechos verdaderos en el mundo
estado_inicial = {"en(caja, sala)", "robot_en(pasillo)", "puerta_abierta(sala)"}

# Objetivo a alcanzar: conjunto de hechos que deben ser verdaderos
objetivo = {"en(caja, pasillo)"}

# Definición de operadores (acciones)
acciones = [
    {
        "nombre": "mover_robot_sala_a_pasillo",
        "precondiciones": {"robot_en(sala)", "puerta_abierta(sala)"},
        "efectos_añadir": {"robot_en(pasillo)"},
        "efectos_eliminar": {"robot_en(sala)"}
    },
    {
        "nombre": "mover_robot_pasillo_a_sala",  # Acción añadida para mover robot del pasillo a la sala
        "precondiciones": {"robot_en(pasillo)", "puerta_abierta(sala)"},
        "efectos_añadir": {"robot_en(sala)"},
        "efectos_eliminar": {"robot_en(pasillo)"}
    },
    {
        "nombre": "abrir_puerta_sala",
        "precondiciones": {"robot_en(sala)", "puerta_cerrada(sala)"},
        "efectos_añadir": {"puerta_abierta(sala)"},
        "efectos_eliminar": {"puerta_cerrada(sala)"}
    },
    {
        "nombre": "mover_caja_sala_a_pasillo",
        "precondiciones": {"en(caja, sala)", "robot_en(sala)"},
        "efectos_añadir": {"en(caja, pasillo)"},
        "efectos_eliminar": {"en(caja, sala)"}
    },
    {
        "nombre": "cerrar_puerta_sala",
        "precondiciones": {"robot_en(sala)", "puerta_abierta(sala)"},
        "efectos_añadir": {"puerta_cerrada(sala)"},
        "efectos_eliminar": {"puerta_abierta(sala)"}
    },
]

def aplicar_accion(estado, accion):
    if not accion["precondiciones"].issubset(estado):
        return None
    nuevo_estado = deepcopy(estado)
    nuevo_estado.difference_update(accion["efectos_eliminar"])
    nuevo_estado.update(accion["efectos_añadir"])
    return nuevo_estado

def planificar(estado_actual, objetivo, acciones, plan=[]):
    if objetivo.issubset(estado_actual):
        return plan
    for accion in acciones:
        nuevo_estado = aplicar_accion(estado_actual, accion)
        if nuevo_estado is not None:
            # Evitar ciclos
            if nuevo_estado not in [p[1] for p in plan]:
                resultado = planificar(nuevo_estado, objetivo, acciones, plan + [(accion["nombre"], nuevo_estado)])
                if resultado is not None:
                    return resultado
    return None

if __name__ == "__main__":
    print("Estado inicial:", estado_inicial)
    print("Objetivo:", objetivo)
    plan_resultado = planificar(estado_inicial, objetivo, acciones)
    if plan_resultado is not None:
        print("\nPlan encontrado:")
        for i, (accion, estado) in enumerate(plan_resultado, 1):
            print(f"  Paso {i}: {accion}")
        print(f"\nObjetivo alcanzado en estado: {plan_resultado[-1][1]}")
    else:
        print("\nNo se encontró un plan para alcanzar el objetivo.")
