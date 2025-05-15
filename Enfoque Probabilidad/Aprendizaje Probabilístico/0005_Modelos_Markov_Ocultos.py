"""
Prácticas de Inteligencia Artificial
Aprendizaje Probabilístico: Modelos de Markov Ocultos (HMM)

Este programa implementa un modelo oculto de Markov (HMM) y el algoritmo de Viterbi.
Un HMM es una herramienta probabilística para modelar procesos donde se tienen estados ocultos
y observaciones visibles. El algoritmo de Viterbi permite encontrar la secuencia de estados más
probable que generó una secuencia de observaciones.
"""

# Estados ocultos posibles
estados = ['Soleado', 'Lluvioso']

# Observaciones posibles
observaciones = ['Caminar', 'Comprar', 'Limpiar']

# Probabilidad inicial de cada estado
prob_inicial = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Probabilidades de transición entre estados
transicion = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Probabilidades de emisión: probabilidad de observar algo dado un estado oculto
emision = {
    'Soleado': {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1},
    'Lluvioso': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5}
}

# Secuencia de observaciones que se han detectado
secuencia_observada = ['Caminar', 'Comprar', 'Limpiar']

# ----------------------------------
# Algoritmo de Viterbi
def viterbi(obs, estados, prob_inicial, transicion, emision):
    # Inicializar la tabla V
    V = [{}]  # V[t][estado] = probabilidad máxima de llegar a ese estado en el tiempo t
    camino = {}  # camino[estado] = secuencia de estados que lleva a ese estado

    # Paso de inicialización
    for estado in estados:
        V[0][estado] = prob_inicial[estado] * emision[estado][obs[0]]
        camino[estado] = [estado]

    # Iterar sobre la secuencia de observaciones
    for t in range(1, len(obs)):
        V.append({})
        nuevo_camino = {}

        for estado_actual in estados:
            # Calcular la mejor probabilidad y el estado anterior correspondiente
            max_prob, mejor_estado = max(
                [(V[t - 1][estado_anterior] * transicion[estado_anterior][estado_actual] * emision[estado_actual][obs[t]], estado_anterior)
                 for estado_anterior in estados],
                key=lambda x: x[0]
            )

            V[t][estado_actual] = max_prob
            nuevo_camino[estado_actual] = camino[mejor_estado] + [estado_actual]

        # Actualizar el camino con los mejores caminos hasta cada estado
        camino = nuevo_camino

    # Obtener la mejor probabilidad final y el estado asociado
    prob_final, estado_final = max((V[-1][estado], estado) for estado in estados)
    return prob_final, camino[estado_final]

# ----------------------------------
# Ejecutar el algoritmo Viterbi
probabilidad_max, mejor_secuencia = viterbi(secuencia_observada, estados, prob_inicial, transicion, emision)

# ----------------------------------
# Mostrar resultados
print("Secuencia observada:", secuencia_observada)
print("Mejor secuencia de estados ocultos:", mejor_secuencia)
print("Probabilidad máxima:", round(probabilidad_max, 4))
