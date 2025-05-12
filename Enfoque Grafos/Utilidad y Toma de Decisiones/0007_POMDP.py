import random

# Posibles estados del entorno
estados = ['Bueno', 'Malo']

# Posibles acciones del agente
acciones = ['Reparar', 'Ignorar']

# Función de observación: el agente no siempre tiene una observación perfecta
def observar(estado_real):
    """
    Retorna una observación del estado real con posibilidad de error (sensor ruidoso).
    """
    if estado_real == 'Bueno':
        return random.choices(['Bueno', 'Malo'], weights=[0.85, 0.15])[0]
    else:
        return random.choices(['Malo', 'Bueno'], weights=[0.85, 0.15])[0]

# Transición estocástica basada en estado y acción
def transicion_estocastica(estado_actual, accion):
    """
    Devuelve el nuevo estado después de tomar una acción.
    Introduce una pequeña probabilidad de que 'Ignorar' algo bueno lo deteriore.
    """
    if estado_actual == 'Bueno':
        if accion == 'Ignorar':
            return random.choices(['Bueno', 'Malo'], weights=[0.9, 0.1])[0]  # 10% de posibilidad de que algo bueno se vuelva malo
        else:
            return 'Bueno'
    elif estado_actual == 'Malo':
        if accion == 'Reparar':
            return 'Bueno'
        else:
            return 'Malo'

# Función de recompensa
def recompensa(estado, accion):
    """
    Define la utilidad de cada combinación de estado y acción.
    """
    if estado == 'Bueno' and accion == 'Ignorar':
        return 10  # Ideal: no haces nada y todo sigue bien
    elif estado == 'Bueno' and accion == 'Reparar':
        return -2  # Gastaste esfuerzo innecesario
    elif estado == 'Malo' and accion == 'Reparar':
        return 8   # Arreglaste correctamente
    elif estado == 'Malo' and accion == 'Ignorar':
        return -5  # Ignoraste un problema

# Simulación del agente en el entorno
def simular_pomdp(iteraciones=10):
    estado_actual = random.choice(estados)  # Empieza en un estado aleatorio
    historial = []

    for i in range(iteraciones):
        print(f"\n=== Iteración {i + 1} ===")
        observacion = observar(estado_actual)  # El agente observa (con error posible)
        print(f"Estado real: {estado_actual}")
        print(f"Observación del agente: {observacion}")

        # Política simple: reparar si cree que está mal, ignorar si cree que está bien
        if observacion == 'Malo':
            accion = 'Reparar'
        else:
            accion = 'Ignorar'

        nuevo_estado = transicion_estocastica(estado_actual, accion)
        r = recompensa(estado_actual, accion)

        # Impresión del resultado
        if accion == 'Reparar':
            print("¡Chispas! Se está reparando algo.")
        else:
            print("El agente decide ignorar la situación.")

        print(f"Acción tomada: {accion}")
        print(f"Nuevo estado: {nuevo_estado}")
        print(f"Recompensa recibida: {r}")

        historial.append((estado_actual, observacion, accion, r))
        estado_actual = nuevo_estado

    return historial

# Ejecutar la simulación
if __name__ == "__main__":
    historial = simular_pomdp()
    print("\n===== Historial de decisiones =====")
    for paso in historial:
        estado, observacion, accion, recompensa = paso
        print(f"Estado: {estado} | Observó: {observacion} | Acción: {accion} | Recompensa: {recompensa}")
