"""
Prácticas de Inteligencia Artificial  
Tema: Razonamiento Probabilístico en el Tiempo  
Subtema: Algoritmo Hacia Adelante-Atrás

Este programa implementa el algoritmo hacia adelante-atrás para modelos ocultos de Markov (HMM).  
Este algoritmo se usa para obtener creencias más precisas sobre todos los estados de una secuencia temporal  
dado un conjunto completo de observaciones. Se combinan los resultados del filtrado hacia adelante y el paso hacia atrás.

Se usan dos estados ocultos (Saludable y Resfriado) y dos posibles observaciones (Normal y Fiebre).
"""

# Estados posibles
estados = ['Saludable', 'Resfriado']

# Observaciones posibles
observaciones = ['Normal', 'Fiebre']

# Distribución inicial
P_inicial = {
    'Saludable': 0.6,
    'Resfriado': 0.4
}

# Probabilidades de transición entre estados
P_transicion = {
    'Saludable': {'Saludable': 0.7, 'Resfriado': 0.3},
    'Resfriado': {'Saludable': 0.4, 'Resfriado': 0.6}
}

# Modelo de sensor: P(observación | estado)
P_sensor = {
    'Saludable': {'Normal': 0.9, 'Fiebre': 0.1},
    'Resfriado': {'Normal': 0.2, 'Fiebre': 0.8}
}

# Secuencia de observaciones (de t=0 a t=3)
evidencias = ['Normal', 'Fiebre', 'Fiebre', 'Normal']

def normalizar(distribucion):
    """Normaliza una distribución para que la suma sea 1"""
    total = sum(distribucion.values())
    return {k: v / total for k, v in distribucion.items()}

def hacia_adelante(evidencias):
    """Filtrado hacia adelante: genera lista de creencias en cada tiempo"""
    bel = P_inicial.copy()
    resultado = [normalizar(bel)]
    for e in evidencias:
        # Predicción + corrección con la evidencia
        bel_pred = {s: sum(P_transicion[s_prev][s] * bel[s_prev] for s_prev in estados) for s in estados}
        bel_corr = {s: P_sensor[s][e] * bel_pred[s] for s in estados}
        bel = normalizar(bel_corr)
        resultado.append(bel)
    return resultado

def hacia_atras(evidencias):
    """Paso hacia atrás: retorna lista de mensajes hacia atrás en cada tiempo"""
    n = len(evidencias)
    beta = {s: 1.0 for s in estados}  # Inicialización con 1s
    resultado = [beta.copy()]  # beta_t+1
    for e in reversed(evidencias):
        beta_nuevo = {}
        for s in estados:
            beta_nuevo[s] = sum(P_transicion[s][s2] * P_sensor[s2][e] * beta[s2] for s2 in estados)
        beta = normalizar(beta_nuevo)
        resultado.insert(0, beta.copy())  # Agregar al inicio
    return resultado

def hacia_adelante_atras(evidencias):
    """Algoritmo hacia adelante-atrás: combina paso adelante y atrás"""
    adelante = hacia_adelante(evidencias)
    atras = hacia_atras(evidencias[1:])  # Excluye la inicial

    posterior = []
    for t in range(len(evidencias)):
        combinado = {s: adelante[t+1][s] * atras[t][s] for s in estados}
        posterior.append(normalizar(combinado))
    return posterior

# === Ejecución ===
print("===== Algoritmo Hacia Adelante-Atrás =====")
print(f"Secuencia de evidencias: {evidencias}\n")

# Ejecutar algoritmo
creencias = hacia_adelante_atras(evidencias)

# Mostrar resultados
for t, distribucion in enumerate(creencias):
    print(f"t = {t}")
    for estado in estados:
        print(f"  P({estado} | evidencia) = {distribucion[estado]:.4f}")
    print()
