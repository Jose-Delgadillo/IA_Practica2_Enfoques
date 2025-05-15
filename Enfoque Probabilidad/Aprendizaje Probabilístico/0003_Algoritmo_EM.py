"""
Prácticas de Inteligencia Artificial
Aprendizaje Probabilístico: Algoritmo EM (Expectation-Maximization)

Este programa simula el algoritmo EM, el cual permite estimar los parámetros
de un modelo probabilístico con variables ocultas, como en el caso de una
mezcla de dos distribuciones Gaussiana. El algoritmo alterna entre dos pasos:
 - E (Esperanza): calcula la probabilidad de pertenencia a cada componente.
 - M (Maximización): actualiza los parámetros del modelo con base en esas probabilidades.
"""

import math
import random

# ---------- FUNCIONES AUXILIARES ----------

# Función de densidad de una distribución normal
def normal(x, media, desviacion):
    coef = 1.0 / (desviacion * math.sqrt(2 * math.pi))
    exponente = math.exp(-((x - media) ** 2) / (2 * desviacion ** 2))
    return coef * exponente

# ---------- DATOS Y PARAMETROS INICIALES ----------

# Datos de entrada (1 dimensión), podrían representar alturas, puntuaciones, etc.
datos = [5.9, 6.0, 6.1, 5.8, 6.2, 3.2, 3.3, 3.1, 3.0, 3.5]

# Inicializamos aleatoriamente los parámetros de dos Gaussianas
media1, desviacion1 = 6.0, 0.2
media2, desviacion2 = 3.0, 0.2

# Pesos (probabilidad de pertenencia a cada grupo)
peso1 = 0.5
peso2 = 0.5

# Número de iteraciones del algoritmo EM
iteraciones = 10

# ---------- ALGORITMO EM ----------

for iter in range(iteraciones):
    # Paso E: calcular responsabilidades (probabilidad de pertenencia a cada grupo)
    responsabilidades = []

    for x in datos:
        p1 = peso1 * normal(x, media1, desviacion1)
        p2 = peso2 * normal(x, media2, desviacion2)
        total = p1 + p2
        responsabilidades.append((p1 / total, p2 / total))  # γ(z_i)

    # Paso M: actualizar parámetros basados en las responsabilidades
    sum_responsabilidad1 = sum(r[0] for r in responsabilidades)
    sum_responsabilidad2 = sum(r[1] for r in responsabilidades)

    # Nuevas medias
    media1 = sum(r[0] * x for r, x in zip(responsabilidades, datos)) / sum_responsabilidad1
    media2 = sum(r[1] * x for r, x in zip(responsabilidades, datos)) / sum_responsabilidad2

    # Nuevas desviaciones estándar
    desviacion1 = math.sqrt(sum(r[0] * (x - media1) ** 2 for r, x in zip(responsabilidades, datos)) / sum_responsabilidad1)
    desviacion2 = math.sqrt(sum(r[1] * (x - media2) ** 2 for r, x in zip(responsabilidades, datos)) / sum_responsabilidad2)

    # Nuevos pesos
    peso1 = sum_responsabilidad1 / len(datos)
    peso2 = sum_responsabilidad2 / len(datos)

    # Imprimir resultados de la iteración
    print(f"\n--- Iteración {iter + 1} ---")
    print(f"Media 1: {media1:.4f}, Desviación 1: {desviacion1:.4f}, Peso 1: {peso1:.4f}")
    print(f"Media 2: {media2:.4f}, Desviación 2: {desviacion2:.4f}, Peso 2: {peso2:.4f}")

# ---------- CLASIFICACIÓN FINAL ----------

print("\nClasificación de los datos según la mayor responsabilidad:")
for x, (r1, r2) in zip(datos, responsabilidades):
    grupo = 1 if r1 > r2 else 2
    print(f"Dato: {x} -> Grupo {grupo}")
