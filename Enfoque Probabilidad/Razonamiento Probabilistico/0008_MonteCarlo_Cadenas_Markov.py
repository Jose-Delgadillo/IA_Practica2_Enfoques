"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Monte Carlo para Cadenas de Markov

Este programa simula una Cadena de Markov usando el método de Monte Carlo.
El objetivo es estimar la distribución de probabilidad estacionaria a través
de múltiples simulaciones aleatorias de los estados de la cadena.
"""

import random
from collections import defaultdict

# Definición de la Cadena de Markov como un diccionario de transiciones
# Cada estado tiene una lista de posibles estados siguientes con sus probabilidades
cadena_markov = {
    'A': [('A', 0.1), ('B', 0.6), ('C', 0.3)],
    'B': [('A', 0.4), ('B', 0.2), ('C', 0.4)],
    'C': [('A', 0.3), ('B', 0.3), ('C', 0.4)]
}

# Función para realizar una transición desde un estado actual
def siguiente_estado(estado_actual):
    transiciones = cadena_markov[estado_actual]
    r = random.random()
    acumulador = 0.0
    for estado, prob in transiciones:
        acumulador += prob
        if r < acumulador:
            return estado
    return transiciones[-1][0]  # Por seguridad, retorna el último si no entró antes

# Simulación Monte Carlo
def simulacion_monte_carlo(inicio, pasos, repeticiones):
    conteo_estados = defaultdict(int)

    for _ in range(repeticiones):
        estado = inicio
        for _ in range(pasos):
            estado = siguiente_estado(estado)
        conteo_estados[estado] += 1

    total = sum(conteo_estados.values())
    distribucion = {estado: round(conteo / total, 4) for estado, conteo in conteo_estados.items()}
    return distribucion

# ===== Ejecución =====
estado_inicial = 'A'
pasos_por_simulacion = 20
num_simulaciones = 10000

print("===== Monte Carlo para Cadenas de Markov =====")
print(f"Estado inicial: {estado_inicial}")
print(f"Simulaciones: {num_simulaciones}, Pasos por simulación: {pasos_por_simulacion}")

resultado = simulacion_monte_carlo(estado_inicial, pasos_por_simulacion, num_simulaciones)

print("\nDistribución estimada de estados (largo plazo):")
for estado, prob in resultado.items():
    print(f"P({estado}) ≈ {prob}")
