"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Red de Hamming, Hopfield, Hebb y Boltzmann

Este programa implementa ejemplos básicos de redes neuronales inspiradas en la biología:
- Hamming: para reconocimiento de patrones mediante comparación con prototipos.
- Hopfield: red de memoria asociativa capaz de estabilizar en patrones previamente memorizados.
- Hebb: basada en la regla de aprendizaje de Hebb ("neuronas que disparan juntas, se conectan").
- Boltzmann: una red estocástica que aprende una distribución de probabilidad sobre sus entradas.

Estas redes ilustran diferentes enfoques para el almacenamiento, recuperación y aprendizaje de patrones.
"""

import random
import math

# ----------------------------
# RED DE HEBB
# ----------------------------

def hebb_train(patrones):
    n = len(patrones[0])
    W = [[0 for _ in range(n)] for _ in range(n)]
    for p in patrones:
        for i in range(n):
            for j in range(n):
                if i != j:
                    W[i][j] += p[i] * p[j]
    return W

def hebb_predict(W, x):
    n = len(x)
    y = [0 for _ in range(n)]
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += W[i][j] * x[j]
        y[i] = 1 if suma >= 0 else -1
    return y

# ----------------------------
# RED DE HOPFIELD
# ----------------------------

def hopfield_train(patrones):
    return hebb_train(patrones)

def hopfield_predict(W, x, max_iter=10):
    n = len(x)
    y = x[:]
    for _ in range(max_iter):
        for i in range(n):
            suma = sum(W[i][j] * y[j] for j in range(n))
            y[i] = 1 if suma >= 0 else -1
    return y

# ----------------------------
# RED DE HAMMING
# ----------------------------

def hamming_predict(prototipos, x):
    """
    Compara el patrón x con cada prototipo y devuelve el más cercano
    """
    distancias = []
    for p in prototipos:
        distancia = sum([1 if p[i] != x[i] else 0 for i in range(len(x))])
        distancias.append(distancia)
    indice = distancias.index(min(distancias))
    return indice, prototipos[indice]

# ----------------------------
# MÁQUINA DE BOLTZMANN RESTRINGIDA (RBM)
# ----------------------------

class RBM:
    def __init__(self, n_visible, n_hidden):
        # Cantidad de neuronas visibles y ocultas
        self.n_visible = n_visible
        self.n_hidden = n_hidden
        # Inicializa pesos aleatorios pequeños
        self.W = [[random.uniform(-0.1, 0.1) for _ in range(n_visible)] for _ in range(n_hidden)]
        self.b = [0.0 for _ in range(n_visible)]  # Bias visible
        self.c = [0.0 for _ in range(n_hidden)]   # Bias oculto

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def sample_prob(self, probs):
        """Muestreo binario con probabilidad dada"""
        return [1 if random.random() < p else 0 for p in probs]

    def train(self, data, lr=0.1, epochs=1000):
        for epoch in range(epochs):
            for v0 in data:
                # Propagación hacia adelante
                h_probs = [self.sigmoid(sum(self.W[h][i] * v0[i] for i in range(self.n_visible)) + self.c[h])
                           for h in range(self.n_hidden)]
                h_sample = self.sample_prob(h_probs)

                # Reconstrucción
                v_probs = [self.sigmoid(sum(self.W[h][i] * h_sample[h] for h in range(self.n_hidden)) + self.b[i])
                           for i in range(self.n_visible)]
                v_sample = self.sample_prob(v_probs)

                # Segunda activación oculta
                h_probs1 = [self.sigmoid(sum(self.W[h][i] * v_sample[i] for i in range(self.n_visible)) + self.c[h])
                            for h in range(self.n_hidden)]

                # Actualización de pesos (Regla Contrastive Divergence)
                for h in range(self.n_hidden):
                    for i in range(self.n_visible):
                        self.W[h][i] += lr * (h_probs[h] * v0[i] - h_probs1[h] * v_sample[i])
                for i in range(self.n_visible):
                    self.b[i] += lr * (v0[i] - v_sample[i])
                for h in range(self.n_hidden):
                    self.c[h] += lr * (h_probs[h] - h_probs1[h])

    def reconstruct(self, v):
        h_probs = [self.sigmoid(sum(self.W[h][i] * v[i] for i in range(self.n_visible)) + self.c[h])
                   for h in range(self.n_hidden)]
        v_probs = [self.sigmoid(sum(self.W[h][i] * h_probs[h] for h in range(self.n_hidden)) + self.b[i])
                   for i in range(self.n_visible)]
        return v_probs


# ----------------------------
# EJEMPLOS DE USO
# ----------------------------

# Hebb
print("\n--- Red de Hebb ---")
patrones_hebb = [[1, -1, 1, -1], [-1, 1, -1, 1]]
W_hebb = hebb_train(patrones_hebb)
entrada_hebb = [1, -1, 1, -1]
salida_hebb = hebb_predict(W_hebb, entrada_hebb)
print("Entrada:", entrada_hebb)
print("Salida :", salida_hebb)

# Hopfield
print("\n--- Red de Hopfield ---")
W_hop = hopfield_train(patrones_hebb)
entrada_hop = [1, -1, 1, -1]
salida_hop = hopfield_predict(W_hop, entrada_hop)
print("Entrada:", entrada_hop)
print("Salida :", salida_hop)

# Hamming
print("\n--- Red de Hamming ---")
prototipos = [[1, 1, -1], [-1, -1, 1]]
entrada_hamming = [1, -1, -1]
idx, salida_hamming = hamming_predict(prototipos, entrada_hamming)
print("Entrada:", entrada_hamming)
print("Clase  :", idx)
print("Patrón :", salida_hamming)

# RBM
print("\n--- Máquina de Boltzmann (RBM) ---")
# Datos binarios para entrenamiento (ejemplo simple)
datos_rbm = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 0, 1]
]
rbm = RBM(n_visible=4, n_hidden=2)
rbm.train(datos_rbm, lr=0.1, epochs=500)
entrada_rbm = [1, 0, 1, 0]
salida_rbm = rbm.reconstruct(entrada_rbm)
print("Entrada      :", entrada_rbm)
print("Reconstruido :", [round(v, 2) for v in salida_rbm])
