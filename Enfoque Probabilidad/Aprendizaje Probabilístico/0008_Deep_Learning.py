"""
Prácticas de Inteligencia Artificial
Aprendizaje Profundo: Red Neuronal Feedforward (con Python puro)

Este programa implementa una red neuronal simple de una capa oculta, usando solo Python.
No utiliza librerías externas como NumPy ni TensorFlow, lo que permite entender desde cero
cómo funcionan las redes neuronales a bajo nivel.

La red se entrena con el algoritmo de retropropagación (backpropagation) para resolver el
problema lógico XOR, que no puede ser resuelto por una sola neurona.

Entradas: dos valores binarios (0 o 1)
Salida: un valor cercano a 0 o 1 dependiendo del resultado del XOR
"""

import random
import math

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la sigmoide (necesaria para backpropagation)
def sigmoid_deriv(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

# Entradas y salidas esperadas del problema XOR
datos_entrada = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

salidas_esperadas = [
    0,
    1,
    1,
    0
]

# Inicializamos pesos y sesgos con valores aleatorios pequeños
def inicializar_pesos(filas, columnas):
    return [[random.uniform(-1, 1) for _ in range(columnas)] for _ in range(filas)]

def inicializar_bias(filas):
    return [random.uniform(-1, 1) for _ in range(filas)]

# Estructura de red: 2 entradas, 2 neuronas ocultas, 1 salida
W1 = inicializar_pesos(2, 2)   # Pesos de entrada a capa oculta
b1 = inicializar_bias(2)       # Bias de capa oculta

W2 = inicializar_pesos(2, 1)   # Pesos de capa oculta a salida
b2 = inicializar_bias(1)       # Bias de salida

# Hiperparámetros
epocas = 10000
tasa_aprendizaje = 0.5

# Entrenamiento
for epoca in range(epocas):
    error_total = 0
    for x, y_esperado in zip(datos_entrada, salidas_esperadas):
        # === Forward Pass ===
        # Capa oculta
        z1 = [sum(x[i] * W1[i][j] for i in range(2)) + b1[j] for j in range(2)]
        a1 = [sigmoid(z1j) for z1j in z1]

        # Capa de salida
        z2 = sum(a1[i] * W2[i][0] for i in range(2)) + b2[0]
        a2 = sigmoid(z2)  # salida final

        # === Cálculo del error ===
        error = (y_esperado - a2) ** 2
        error_total += error

        # === Backpropagation ===
        # Derivada del error respecto a la salida
        d_a2 = -(y_esperado - a2)
        d_z2 = d_a2 * sigmoid_deriv(z2)

        # Gradientes de los pesos de salida
        for i in range(2):
            W2[i][0] -= tasa_aprendizaje * d_z2 * a1[i]

        b2[0] -= tasa_aprendizaje * d_z2

        # Backpropagation a capa oculta
        d_a1 = [d_z2 * W2[i][0] for i in range(2)]
        d_z1 = [d_a1[j] * sigmoid_deriv(z1[j]) for j in range(2)]

        for i in range(2):
            for j in range(2):
                W1[i][j] -= tasa_aprendizaje * d_z1[j] * x[i]

        for j in range(2):
            b1[j] -= tasa_aprendizaje * d_z1[j]

    if epoca % 1000 == 0:
        print(f"Época {epoca} - Error total: {error_total:.4f}")

# === Evaluación final ===
print("\nResultados después del entrenamiento:")
for x in datos_entrada:
    z1 = [sum(x[i] * W1[i][j] for i in range(2)) + b1[j] for j in range(2)]
    a1 = [sigmoid(z1j) for z1j in z1]
    z2 = sum(a1[i] * W2[i][0] for i in range(2)) + b2[0]
    a2 = sigmoid(z2)
    print(f"Entrada: {x} -> Predicción: {a2:.4f}")
