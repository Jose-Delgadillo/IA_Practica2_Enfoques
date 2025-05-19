"""
Simulación simple de Planificación Continua y Multiagente

- Dos agentes con planes separados.
- Ejecución paso a paso simulando tiempo continuo.
- Coordinación simple para evitar conflictos.
"""

# Estado global
estado = {
    'robot1_pos': 'base',
    'robot2_pos': 'base',
    'objeto_en': 'zonaA',
    'robot1_carga': False,
    'robot2_carga': False,
    'tarea_robot1_completa': False,
    'tarea_robot2_completa': False,
}

# Planes para cada robot: lista de acciones a ejecutar en orden
plan_robot1 = [
    ('mover', 'base', 'zonaA'),
    ('cargar', 'zonaA'),
    ('mover', 'zonaA', 'base'),
    ('descargar', 'base')
]

plan_robot2 = [
    ('esperar', 'robot1'),
    ('mover', 'base', 'zonaB'),
    ('mover', 'zonaB', 'base'),  # Vuelve para cargar objeto en base
    ('cargar', 'base'),          # Carga el objeto en base
    ('mover', 'base', 'zonaB'),  # Lleva objeto a zonaB
    ('descargar', 'zonaB')
]


# Funciones de acciones
def mover(robot, origen, destino):
    key_pos = f'{robot}_pos'
    if estado[key_pos] == origen:
        print(f"{robot} se mueve de {origen} a {destino}")
        estado[key_pos] = destino
        return True
    else:
        print(f"{robot} no está en {origen} para moverse")
        return False

def cargar(robot, lugar):
    key_pos = f'{robot}_pos'
    key_carga = f'{robot}_carga'
    if estado[key_pos] == lugar and estado['objeto_en'] == lugar and not estado[key_carga]:
        print(f"{robot} carga el objeto en {lugar}")
        estado['objeto_en'] = None
        estado[key_carga] = True
        return True
    else:
        print(f"{robot} no puede cargar objeto en {lugar}")
        return False

def descargar(robot, lugar):
    key_pos = f'{robot}_pos'
    key_carga = f'{robot}_carga'
    if estado[key_pos] == lugar and estado[key_carga]:
        print(f"{robot} descarga el objeto en {lugar}")
        estado['objeto_en'] = lugar
        estado[key_carga] = False
        # Marcar tarea como completa
        estado[f'tarea_{robot}_completa'] = True
        return True
    else:
        print(f"{robot} no puede descargar objeto en {lugar}")
        return False

def esperar(robot_esperado):
    # Esperar hasta que el robot esperado termine su tarea
    if estado.get(f'tarea_{robot_esperado}_completa', False):
        print(f"Continuando porque {robot_esperado} terminó su tarea.")
        return True
    else:
        print(f"Esperando que {robot_esperado} termine su tarea...")
        return False

# Ejecutar plan paso a paso para cada robot
def ejecutar_planes_continuos():
    puntero1 = 0
    puntero2 = 0
    max_pasos = 20
    paso = 0

    print("Estado inicial:", estado)
    print("Ejecutando planes de robots con planificación continua...\n")

    while paso < max_pasos:
        paso += 1
        print(f"\n--- Paso {paso} ---")

        # Ejecutar siguiente acción robot1
        if puntero1 < len(plan_robot1):
            accion1 = plan_robot1[puntero1]
            resultado1 = ejecutar_accion('robot1', accion1)
            if resultado1:
                puntero1 += 1
        else:
            print("Robot1 completó su plan.")

        # Ejecutar siguiente acción robot2
        if puntero2 < len(plan_robot2):
            accion2 = plan_robot2[puntero2]
            resultado2 = ejecutar_accion('robot2', accion2)
            if resultado2:
                puntero2 += 1
        else:
            print("Robot2 completó su plan.")

        # Condición para salir si ambos completaron sus planes
        if puntero1 >= len(plan_robot1) and puntero2 >= len(plan_robot2):
            print("\n¡Ambos robots completaron sus tareas!")
            break

# Función para ejecutar acción según el plan
def ejecutar_accion(robot, accion):
    tipo = accion[0]

    if tipo == 'mover':
        _, origen, destino = accion
        return mover(robot, origen, destino)
    elif tipo == 'cargar':
        _, lugar = accion
        return cargar(robot, lugar)
    elif tipo == 'descargar':
        _, lugar = accion
        return descargar(robot, lugar)
    elif tipo == 'esperar':
        _, robot_esperado = accion
        return esperar(robot_esperado)
    else:
        print(f"Acción desconocida: {tipo}")
        return False

if __name__ == "__main__":
    ejecutar_planes_continuos()
