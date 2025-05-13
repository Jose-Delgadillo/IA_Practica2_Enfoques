"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico en el Tiempo - Procesos Estacionarios


Este programa modela un proceso estacionario simple. En un proceso estacionario, 
las probabilidades de transición entre estados no cambian con el tiempo. 
Simulamos una serie de pasos para observar cómo las distribuciones de estado 
tienden a estabilizarse (distribución estacionaria).
"""

import random
from collections import defaultdict

# Definimos una cadena de Markov con transiciones constantes (estacionarias)
transiciones_estacionarias = {
    'Soleado': [('Soleado', 0.8), ('Lluvioso', 0.2)],
    'Lluvioso': [('Soleado', 0.4), ('Lluvioso', 0.6)]
}

# Función para elegir el siguiente estado con base en las probabilidades
def siguiente_estado(estado_actual, transiciones):
    r = random.random()
    acumulado = 0.0
    for estado, prob in transiciones[estado_actual]:
        acumulado += prob
        if r < acumulado:
            return estado
    return transiciones[estado_actual][-1][0]  # Seguridad

# Simula el proceso por varios pasos, comenzando en un estado inicial
def simular_proceso(estado_inicial, transiciones, pasos):
    estado = estado_inicial
    secuencia = [estado]
    for _ in range(pasos):
        estado = siguiente_estado(estado, transiciones)
        secuencia.append(estado)
    return secuencia

# Simula muchas veces y cuenta en qué estados se termina
def estimar_distribucion_estacionaria(estado_inicial, transiciones, pasos, simulaciones):
    conteo = defaultdict(int)
    for _ in range(simulaciones):
        secuencia = simular_proceso(estado_inicial, transiciones, pasos)
        estado_final = secuencia[-1]
        conteo[estado_final] += 1

    total = sum(conteo.values())
    distribucion = {estado: round(cont / total, 4) for estado, cont in conteo.items()}
    return distribucion

# ==== Ejecución ====
estado_inicial = 'Soleado'
pasos = 20
simulaciones = 10000

print("===== Proceso Estacionario =====")
print(f"Estado inicial: {estado_inicial}")
print(f"Simulando {simulaciones} trayectorias de {pasos} pasos cada una...\n")

distribucion_final = estimar_distribucion_estacionaria(estado_inicial, transiciones_estacionarias, pasos, simulaciones)

print("Distribución estimada al final del proceso:")
for estado, prob in distribucion_final.items():
    print(f"P({estado}) ≈ {prob}")
