"""
Prácticas de Inteligencia Artificial
Planificación Condicional

Este programa implementa un planificador simple con planificación condicional.
La planificación condicional permite decidir qué acciones realizar según el estado
actual del mundo, considerando condiciones y ramificaciones en el plan.

La idea es que algunas acciones solo se ejecutan si se cumple cierta condición,
y el plan puede cambiar dependiendo de resultados o estados que surjan durante
la ejecución.
"""

# Definición del estado inicial como un conjunto de hechos (hechos verdaderos)
estado_actual = {'robot_en_pasillo', 'caja_en_sala', 'puerta_abierta_sala'}

# Funciones que representan acciones primitivas con sus precondiciones y efectos
def mover_robot(origen, destino):
    """Acción: Mover el robot de un lugar a otro si está en el origen y la puerta está abierta"""
    if f'robot_en_{origen}' in estado_actual and f'puerta_abierta_{destino}' in estado_actual:
        print(f"Moviendo robot de {origen} a {destino}")
        estado_actual.remove(f'robot_en_{origen}')
        estado_actual.add(f'robot_en_{destino}')
    else:
        print(f"No se puede mover el robot de {origen} a {destino} (condiciones no cumplidas)")

def tomar_caja(lugar):
    """Acción: Tomar la caja si está en el lugar y el robot está allí"""
    if f'caja_en_{lugar}' in estado_actual and f'robot_en_{lugar}' in estado_actual:
        print(f"Tomando caja en {lugar}")
        estado_actual.remove(f'caja_en_{lugar}')
        estado_actual.add('robot_sosteniendo_caja')
    else:
        print(f"No se puede tomar la caja en {lugar} (condiciones no cumplidas)")

def dejar_caja(lugar):
    """Acción: Dejar la caja en el lugar si el robot la sostiene y está en el lugar"""
    if 'robot_sosteniendo_caja' in estado_actual and f'robot_en_{lugar}' in estado_actual:
        print(f"Dejando caja en {lugar}")
        estado_actual.remove('robot_sosteniendo_caja')
        estado_actual.add(f'caja_en_{lugar}')
    else:
        print(f"No se puede dejar la caja en {lugar} (condiciones no cumplidas)")

# Planificación condicional: función que decide qué acciones ejecutar según estado
def planificar_condicional():
    """
    Plan simple que:
    - Mueve el robot al lugar donde está la caja
    - Toma la caja
    - Mueve el robot al destino
    - Deja la caja
    """
    # Paso 1: Mover robot al pasillo si no está ahí
    if 'robot_en_pasillo' not in estado_actual:
        mover_robot('sala', 'pasillo')
    
    # Paso 2: Mover robot a la sala si no está ahí (condicional)
    if 'robot_en_sala' not in estado_actual:
        mover_robot('pasillo', 'sala')

    # Paso 3: Intentar tomar la caja en la sala
    tomar_caja('sala')

    # Paso 4: Si robot sostiene la caja, mover a pasillo
    if 'robot_sosteniendo_caja' in estado_actual:
        mover_robot('sala', 'pasillo')
        # Paso 5: Dejar la caja en pasillo
        dejar_caja('pasillo')
    else:
        print("No se puede continuar con el plan: no se tiene la caja")

if __name__ == "__main__":
    print("Estado inicial:", estado_actual, "\n")
    print("Ejecutando planificación condicional...\n")
    planificar_condicional()
    print("\nEstado final:", estado_actual)
