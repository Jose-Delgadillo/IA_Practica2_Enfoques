"""
Prácticas de Inteligencia Artificial
Vigilancia de Ejecución y Replanificación

Este programa simula un sistema de planificación condicional con vigilancia en la ejecución.
El sistema verifica después de cada acción si el estado es el esperado y, si ocurre un fallo
(o el estado cambia inesperadamente), intenta replanificar para lograr el objetivo.

Este mecanismo es esencial en sistemas reales donde el entorno puede ser incierto o dinámico.
"""

# Estado inicial del mundo: conjunto de hechos verdaderos
estado_actual = {'robot_en_pasillo', 'caja_en_sala', 'puerta_abierta_sala', 'puerta_abierta_pasillo'}

# Objetivo deseado: llevar la caja al pasillo
objetivo = {'caja_en_pasillo'}

# Definición de acciones con precondiciones y efectos
def mover_robot(origen, destino):
    """Mover robot si está en origen y la puerta destino está abierta"""
    if origen == destino:
        print(f"Error: Origen y destino iguales ({origen}), movimiento no válido.")
        return False

    if f'robot_en_{origen}' in estado_actual and f'puerta_abierta_{destino}' in estado_actual:
        print(f"Moviendo robot de {origen} a {destino}")
        estado_actual.remove(f'robot_en_{origen}')
        estado_actual.add(f'robot_en_{destino}')
        print(f"Estado actual: {estado_actual}")
        return True
    else:
        print(f"Error: No se puede mover el robot de {origen} a {destino}")
        print(f"Estado actual: {estado_actual}")
        return False

def tomar_caja(lugar):
    """Tomar caja si está en lugar y robot también"""
    if f'caja_en_{lugar}' in estado_actual and f'robot_en_{lugar}' in estado_actual:
        print(f"Tomando caja en {lugar}")
        estado_actual.remove(f'caja_en_{lugar}')
        estado_actual.add('robot_sosteniendo_caja')
        print(f"Estado actual: {estado_actual}")
        return True
    else:
        print(f"Error: No se puede tomar la caja en {lugar}")
        print(f"Estado actual: {estado_actual}")
        return False

def dejar_caja(lugar):
    """Dejar caja si robot la sostiene y está en lugar"""
    if 'robot_sosteniendo_caja' in estado_actual and f'robot_en_{lugar}' in estado_actual:
        print(f"Dejando caja en {lugar}")
        estado_actual.remove('robot_sosteniendo_caja')
        estado_actual.add(f'caja_en_{lugar}')
        print(f"Estado actual: {estado_actual}")
        return True
    else:
        print(f"Error: No se puede dejar la caja en {lugar}")
        print(f"Estado actual: {estado_actual}")
        return False

# Planificador simple que genera una lista de acciones condicionales para alcanzar el objetivo
def planificar():
    """
    Plan: mover robot a sala, tomar caja, mover robot a pasillo, dejar caja
    """
    plan = [
        ('mover_robot', 'pasillo', 'sala'),
        ('tomar_caja', 'sala'),
        ('mover_robot', 'sala', 'pasillo'),
        ('dejar_caja', 'pasillo'),
    ]
    return plan

# Función que verifica si el objetivo está cumplido
def objetivo_cumplido():
    return all(cond in estado_actual for cond in objetivo)

# Ejecutar plan con vigilancia y replanificación si alguna acción falla
def ejecutar_con_vigilancia():
    plan = planificar()
    print("Estado inicial:", estado_actual)
    print("Ejecutando plan con vigilancia...\n")

    for accion in plan:
        nombre = accion[0]
        args = accion[1:]

        # Ejecutar la acción correspondiente
        if nombre == 'mover_robot':
            exito = mover_robot(*args)
        elif nombre == 'tomar_caja':
            exito = tomar_caja(*args)
        elif nombre == 'dejar_caja':
            exito = dejar_caja(*args)
        else:
            print(f"Acción desconocida: {nombre}")
            exito = False

        # Vigilar ejecución: si falla, intentar replanificar
        if not exito:
            print("\n-- Fallo detectado, intentando replanificar --\n")
            # Replanificación simple: verificar estado y plan alternativo
            if 'robot_en_pasillo' not in estado_actual:
                print("Replan: mover robot a pasillo")
                # Mover solo si no está ya en pasillo
                if 'robot_en_pasillo' not in estado_actual:
                    # Buscar dónde está el robot para moverlo
                    lugares = ['sala', 'pasillo', 'otro']
                    origen_robot = next((l for l in lugares if f'robot_en_{l}' in estado_actual), None)
                    if origen_robot and origen_robot != 'pasillo':
                        mover_robot(origen_robot, 'pasillo')
            if 'caja_en_sala' not in estado_actual and 'robot_sosteniendo_caja' not in estado_actual:
                print("Replan: intentar tomar caja en sala")
                tomar_caja('sala')

            # Reintentar la acción actual tras replanificación
            print("Reintentando acción fallida...")
            if nombre == 'mover_robot':
                exito = mover_robot(*args)
            elif nombre == 'tomar_caja':
                exito = tomar_caja(*args)
            elif nombre == 'dejar_caja':
                exito = dejar_caja(*args)

            if not exito:
                print("No se pudo recuperar de la falla. Abortando plan.")
                break

        # Verificar si objetivo cumplido en cualquier momento
        if objetivo_cumplido():
            print("\nObjetivo alcanzado con éxito!")
            break

    else:
        print("\nPlan completado.")

    print("\nEstado final:", estado_actual)

if __name__ == "__main__":
    ejecutar_con_vigilancia()
