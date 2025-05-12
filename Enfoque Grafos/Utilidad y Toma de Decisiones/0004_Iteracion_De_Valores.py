"""
Prácticas de Inteligencia Artificial
Iteración de Valores en Procesos de Decisión de Markov (MDP)

Este algoritmo calcula los valores óptimos de cada estado
asumiendo que el agente sigue una política óptima.
Sirve para planificar en entornos donde las acciones tienen
resultados probabilísticos.
"""

# Lista de estados posibles
estados = ['A', 'B', 'C']

# Lista de acciones disponibles desde cada estado
acciones = ['izquierda', 'derecha']

# Diccionario que define las transiciones:
# transiciones[estado][accion] = lista de (probabilidad, estado_siguiente, recompensa)
transiciones = {
    'A': {
        'derecha': [(1.0, 'B', 5)],     # Si desde A vas a la derecha, llegas a B con recompensa 5
        'izquierda': [(1.0, 'A', 0)]    # Si desde A vas a la izquierda, te quedas en A sin recompensa
    },
    'B': {
        'derecha': [(1.0, 'C', 10)],    # Desde B, ir a la derecha lleva a C con recompensa 10
        'izquierda': [(1.0, 'A', 0)]    # Ir a la izquierda vuelve a A
    },
    'C': {
        'derecha': [(1.0, 'C', 0)],     # C es un estado terminal: no da más recompensas
        'izquierda': [(1.0, 'B', 0)]
    }
}

# Factor de descuento: cuánto valoramos las recompensas futuras
gamma = 0.9

# Umbral de cambio mínimo para considerar que la solución ya convergió
umbral = 0.01

# Diccionario que guarda el valor estimado de cada estado
# Inicialmente todos los valores son 0
valores = {s: 0 for s in estados}

# ======== ALGORITMO DE ITERACIÓN DE VALORES =========
def iteracion_valores():
    while True:
        delta = 0  # Para verificar el cambio máximo entre iteraciones
        nuevos_valores = valores.copy()  # Copia de valores actuales

        # Recorremos cada estado
        for estado in estados:
            mejores_valores = []

            # Recorremos cada acción válida desde ese estado
            for accion in acciones:
                if accion in transiciones[estado]:
                    suma = 0  # Esperanza de utilidad para esta acción

                    # Para cada transición posible desde esta acción:
                    for prob, siguiente_estado, recompensa in transiciones[estado][accion]:
                        # Fórmula del valor esperado: recompensa + valor del siguiente estado descontado
                        suma += prob * (recompensa + gamma * valores[siguiente_estado])
                    
                    # Guardamos la utilidad esperada de esta acción
                    mejores_valores.append(suma)

            # Elegimos el mayor valor entre todas las acciones
            if mejores_valores:
                nuevos_valores[estado] = max(mejores_valores)

                # Guardamos el mayor cambio en esta iteración
                delta = max(delta, abs(nuevos_valores[estado] - valores[estado]))

        # Actualizamos los valores
        valores.update(nuevos_valores)

        # Si los valores ya no cambian significativamente, salimos del bucle
        if delta < umbral:
            break

    return valores

# ======== EJECUCIÓN DEL ALGORITMO =========
valores_finales = iteracion_valores()

# ======== RESULTADOS =========
print("===== Iteración de Valores Finalizada =====")
for estado in estados:
    print(f"Valor óptimo de estado {estado}: {valores_finales[estado]:.2f}")
