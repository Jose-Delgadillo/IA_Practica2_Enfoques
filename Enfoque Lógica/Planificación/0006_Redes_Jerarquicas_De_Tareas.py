"""
Redes Jerárquicas de Tareas (HTN) - Ejemplo Simple

Este código modela:
- Tareas primitivas: acciones ejecutables
- Tareas compuestas: tareas que se descomponen en subtareas
- Un planificador HTN que descompone tareas compuestas recursivamente
- Plan resultante: secuencia de tareas primitivas para lograr la tarea objetivo

"""

# Definimos tareas primitivas como funciones simples (simulan acciones)
def mover_robot(origen, destino):
    print(f"Acción: mover robot de {origen} a {destino}")

def tomar_objeto(objeto, lugar):
    print(f"Acción: tomar {objeto} en {lugar}")

def dejar_objeto(objeto, lugar):
    print(f"Acción: dejar {objeto} en {lugar}")

# Definimos la estructura HTN usando diccionarios

# Tareas primitivas
tareas_primitivas = {
    'mover_robot': mover_robot,
    'tomar_objeto': tomar_objeto,
    'dejar_objeto': dejar_objeto
}

# Tareas compuestas con descomposiciones (lista de subtareas)
tareas_compuestas = {
    'trasladar_objeto': [
        ('mover_robot', 'pasillo', 'sala'),
        ('tomar_objeto', 'caja', 'sala'),
        ('mover_robot', 'sala', 'pasillo'),
        ('dejar_objeto', 'caja', 'pasillo')
    ],
    'preparar_entrega': [
        ('trasladar_objeto',),
        ('mover_robot', 'pasillo', 'oficina')
    ]
}

# Planificador HTN simple
def planificar(tarea):
    """
    Recibe una tarea (string o tupla)
    - Si es tarea primitiva, la ejecuta
    - Si es compuesta, descompone y planifica cada subtarea
    """
    if tarea[0] in tareas_primitivas:
        # Ejecutar tarea primitiva
        func = tareas_primitivas[tarea[0]]
        args = tarea[1:] if len(tarea) > 1 else []
        func(*args)
    elif tarea[0] in tareas_compuestas:
        # Descomponer tarea compuesta
        subtareas = tareas_compuestas[tarea[0]]
        for st in subtareas:
            # Si subtarea es solo string, convertir a tupla
            subt = st if isinstance(st, tuple) else (st,)
            planificar(subt)
    else:
        print(f"Tarea desconocida: {tarea[0]}")

# Ejemplo de uso:

if __name__ == "__main__":
    print("Planificación HTN para 'preparar_entrega':\n")
    planificar(('preparar_entrega',))
