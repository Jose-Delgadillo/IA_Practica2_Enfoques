"""
Prácticas de Inteligencia Artificial
Enfoque: Planificación
Subtema: Planificación de Orden Parcial

Este programa implementa una versión simplificada de la planificación de orden parcial.
La planificación de orden parcial permite construir planes en los que las acciones no
necesariamente están totalmente ordenadas, sólo se imponen las restricciones de orden
mínimas necesarias para garantizar la corrección del plan.

El plan está representado por un conjunto de acciones y un conjunto de restricciones de
orden entre ellas. Se busca un plan que alcance el objetivo desde el estado inicial,
sin necesidad de fijar un orden lineal estricto desde el principio.

Este ejemplo es una simplificación educativa para ilustrar el concepto básico.
"""

from copy import deepcopy

# Estado inicial y objetivo (hechos)
estado_inicial = {"robot_en(pasillo)", "puerta_abierta(sala)", "en(caja, sala)"}
objetivo = {"en(caja, pasillo)"}

# Definición de las acciones disponibles con precondiciones y efectos
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

class PlanParcial:
    def __init__(self):
        # Acciones en el plan (lista)
        self.acciones = []
        # Restricciones de orden: lista de tuplas (accion_antes, accion_despues)
        self.restricciones_orden = []

    def añadir_accion(self, accion_nombre):
        if accion_nombre not in self.acciones:
            self.acciones.append(accion_nombre)

    def añadir_restriccion(self, antes, despues):
        if (antes, despues) not in self.restricciones_orden:
            self.restricciones_orden.append((antes, despues))

    def mostrar(self):
        print("Acciones en el plan:")
        for a in self.acciones:
            print(f" - {a}")
        print("\nRestricciones de orden:")
        for antes, despues in self.restricciones_orden:
            print(f" - {antes} < {despues}")

def chequeo_precondiciones(estado, precondiciones):
    """Verifica si todas las precondiciones están presentes en el estado actual."""
    return precondiciones.issubset(estado)

def aplicar_accion(estado, accion):
    """Aplica la acción al estado y devuelve el nuevo estado resultante."""
    if not chequeo_precondiciones(estado, accion["precondiciones"]):
        return None
    nuevo_estado = deepcopy(estado)
    nuevo_estado.difference_update(accion["efectos_eliminar"])
    nuevo_estado.update(accion["efectos_añadir"])
    return nuevo_estado

def planificar_orden_parcial(estado_actual, objetivo, acciones, plan=None, estado_accion=None):
    """
    Función recursiva para encontrar un plan de orden parcial.
    - estado_actual: estado inicial del mundo.
    - objetivo: conjunto de hechos deseados.
    - acciones: lista de acciones posibles.
    - plan: objeto PlanParcial que contiene las acciones y restricciones.
    - estado_accion: estado actual luego de aplicar las acciones planificadas.
    """
    if plan is None:
        plan = PlanParcial()
        estado_accion = estado_actual

    # Si el objetivo está cumplido en el estado actual, devolvemos el plan
    if objetivo.issubset(estado_accion):
        return plan

    # Buscar acciones que puedan avanzar hacia el objetivo
    for accion in acciones:
        # Verificar si la acción no está ya en el plan y si sus efectos contribuyen al objetivo
        if accion["nombre"] not in plan.acciones and any(e in objetivo for e in accion["efectos_añadir"]):
            # Comprobar si las precondiciones se cumplen para aplicar la acción
            if chequeo_precondiciones(estado_accion, accion["precondiciones"]):
                nuevo_estado = aplicar_accion(estado_accion, accion)
                if nuevo_estado:
                    plan.añadir_accion(accion["nombre"])
                    # Añadir restricción para mantener orden entre acciones (simplemente orden lineal aquí)
                    if len(plan.acciones) > 1:
                        plan.añadir_restriccion(plan.acciones[-2], plan.acciones[-1])
                    # Recursión para seguir planificando desde el nuevo estado
                    resultado = planificar_orden_parcial(estado_actual, objetivo, acciones, plan, nuevo_estado)
                    if resultado:
                        return resultado
    return None

if __name__ == "__main__":
    print("Estado inicial:", estado_inicial)
    print("Objetivo:", objetivo)
    plan = planificar_orden_parcial(estado_inicial, objetivo, acciones)
    if plan:
        print("\nPlan de orden parcial encontrado:")
        plan.mostrar()
    else:
        print("\nNo se encontró un plan de orden parcial que alcance el objetivo.")
