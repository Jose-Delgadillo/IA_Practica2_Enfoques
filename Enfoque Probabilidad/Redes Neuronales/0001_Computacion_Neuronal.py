"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Red Neuronal Multicapa (Perceptrón Multicapa - MLP)

Este programa implementa una red neuronal multicapa (MLP) sin el uso de librerías externas.
La red consta de una capa oculta y una capa de salida, con activación sigmoide.
Se entrena con el algoritmo de retropropagación (backpropagation) para aprender
la compuerta lógica XOR, un problema clásico que no puede resolverse con un perceptrón simple.
"""

import math
import random

# --------------------------
# Funciones auxiliares
# --------------------------

def sigmoide(x):
    """Función de activación sigmoide"""
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    """Derivada de la función sigmoide"""
    sx = sigmoide(x)
    return sx * (1 - sx)

# --------------------------
# Configuración de la red
# --------------------------

# Número de neuronas por capa
entrada = 2
oculta = 2
salida = 1

# Inicialización de pesos y sesgos (bias)
W1 = [[random.uniform(-1, 1) for _ in range(entrada)] for _ in range(oculta)]
b1 = [random.uniform(-1, 1) for _ in range(oculta)]

W2 = [random.uniform(-1, 1) for _ in range(oculta)]
b2 = random.uniform(-1, 1)

# Tasa de aprendizaje
lr = 0.5

# Datos de entrenamiento para XOR
datos = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

# --------------------------
# Entrenamiento de la red
# --------------------------

for epoca in range(10000):
    for x, y in datos:
        # FORWARD PASS

        # Capa oculta
        z1 = []
        a1 = []
        for i in range(oculta):
            suma = sum(W1[i][j] * x[j] for j in range(entrada)) + b1[i]
            z1.append(suma)
            a1.append(sigmoide(suma))

        # Capa de salida
        z2 = sum(W2[i] * a1[i] for i in range(oculta)) + b2
        a2 = sigmoide(z2)  # Predicción

        # BACKPROPAGATION

        # Error en salida
        error_salida = (a2 - y)
        delta_salida = error_salida * derivada_sigmoide(z2)

        # Error en capa oculta
        delta_oculta = []
        for i in range(oculta):
            delta = delta_salida * W2[i] * derivada_sigmoide(z1[i])
            delta_oculta.append(delta)

        # Actualización de pesos y sesgos
        for i in range(oculta):
            W2[i] -= lr * delta_salida * a1[i]
        b2 -= lr * delta_salida

        for i in range(oculta):
            for j in range(entrada):
                W1[i][j] -= lr * delta_oculta[i] * x[j]
            b1[i] -= lr * delta_oculta[i]

# --------------------------
# Pruebas con la red entrenada
# --------------------------

print("Prueba del modelo entrenado (XOR):")
for x, y in datos:
    # Forward pass
    z1 = [sum(W1[i][j] * x[j] for j in range(entrada)) + b1[i] for i in range(oculta)]
    a1 = [sigmoide(z) for z in z1]
    z2 = sum(W2[i] * a1[i] for i in range(oculta)) + b2
    a2 = sigmoide(z2)

    print(f"Entrada: {x} -> Predicción: {a2:.4f} (esperado: {y})")
