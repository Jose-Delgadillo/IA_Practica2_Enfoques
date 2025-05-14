"""
Prácticas de Inteligencia Artificial  
Tema: Razonamiento Probabilístico en el Tiempo  
Subtema: Modelos Ocultos de Markov (HMM)

Este programa implementa un modelo oculto de Markov (HMM) simple.
Un HMM consiste en:
- Estados ocultos que evolucionan con el tiempo según una matriz de transición.
- Observaciones visibles que dependen probabilísticamente del estado oculto actual.

El objetivo es calcular la probabilidad de una secuencia de observaciones 
dada una distribución inicial, una matriz de transición y un modelo de observación.

Se utiliza el algoritmo hacia adelante para este cálculo.
"""

# Estados ocultos
estados = ['Lluvia', 'Sol']

# Observaciones posibles
observaciones = ['Caminar', 'Comprar', 'Limpiar']

# Probabilidad inicial para cada estado
prob_inicial = {
    'Lluvia': 0.6,
    'Sol': 0.4
}

# Matriz de transición de estados
transicion = {
    'Lluvia': {'Lluvia': 0.7, 'Sol': 0.3},
    'Sol': {'Lluvia': 0.4, 'Sol': 0.6}
}

# Modelo de observación: P(observación | estado)
emision = {
    'Lluvia': {'Caminar': 0.1, 'Comprar': 0.4, 'Limpiar': 0.5},
    'Sol': {'Caminar': 0.6, 'Comprar': 0.3, 'Limpiar': 0.1}
}

# Secuencia de observaciones (visibles)
secuencia_observaciones = ['Caminar', 'Comprar', 'Limpiar']

def normalizar(probabilidades):
    """Normaliza una distribución para que sume 1"""
    total = sum(probabilidades.values())
    return {k: v / total for k, v in probabilidades.items()}

def algoritmo_adelante(observaciones):
    """Implementa el algoritmo hacia adelante para HMM"""
    alfas = []  # Almacenará las creencias en cada paso

    # Paso inicial con la primera observación
    alfa = {}
    primera_obs = observaciones[0]
    for estado in estados:
        alfa[estado] = prob_inicial[estado] * emision[estado][primera_obs]
    alfas.append(normalizar(alfa))

    # Iterar sobre el resto de observaciones
    for t in range(1, len(observaciones)):
        obs = observaciones[t]
        alfa_nuevo = {}
        for estado_actual in estados:
            suma = sum(
                alfas[-1][estado_anterior] * transicion[estado_anterior][estado_actual]
                for estado_anterior in estados
            )
            alfa_nuevo[estado_actual] = emision[estado_actual][obs] * suma
        alfas.append(normalizar(alfa_nuevo))

    return alfas

# === EJECUCIÓN ===
print("===== Modelo Oculto de Markov =====")
print(f"Secuencia de observaciones: {secuencia_observaciones}\n")

resultados = algoritmo_adelante(secuencia_observaciones)

# Mostrar resultados
for t, distribucion in enumerate(resultados):
    print(f"t = {t} (Obs: {secuencia_observaciones[t]})")
    for estado in estados:
        print(f"  P({estado}) = {distribucion[estado]:.4f}")
    print()
