"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico en el Tiempo
Subtema: Hipótesis de Markov - Procesos de Markov

Este programa ilustra la Hipótesis de Markov: 
la suposición de que el estado futuro depende solo del estado actual y no 
de los estados anteriores (memoria de un solo paso). 
Simulamos una cadena de Markov para observar cómo los estados se 
transicionan en función solo del estado actual.
"""

import random

# Definimos una cadena de Markov simple
# Cada estado tiene una lista de posibles transiciones con sus respectivas probabilidades
transiciones = {
    'Saludable': [('Saludable', 0.7), ('Resfriado', 0.3)],
    'Resfriado': [('Saludable', 0.4), ('Resfriado', 0.6)]
}

# Función que determina el siguiente estado basándose únicamente en el estado actual
# Esto es precisamente la Hipótesis de Markov
def siguiente_estado(estado_actual):
    r = random.random()
    acumulado = 0.0
    for estado, prob in transiciones[estado_actual]:
        acumulado += prob
        if r < acumulado:
            return estado
    return transiciones[estado_actual][-1][0]  # Caso extremo de seguridad

# Simula una cadena de Markov durante varios pasos
def simular_proceso_markov(estado_inicial, pasos):
    secuencia = [estado_inicial]
    estado = estado_inicial
    for _ in range(pasos):
        estado = siguiente_estado(estado)
        secuencia.append(estado)
    return secuencia

# ==== Ejecución del proceso de Markov ====
estado_inicial = 'Saludable'
pasos = 15

print("===== Proceso de Markov: Hipótesis de Markov =====")
print(f"Estado inicial: {estado_inicial}")
print(f"Número de pasos: {pasos}\n")

secuencia_resultante = simular_proceso_markov(estado_inicial, pasos)

print("Secuencia de estados:")
print(" → ".join(secuencia_resultante))
