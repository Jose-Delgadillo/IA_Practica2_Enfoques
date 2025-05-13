"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Muestreo Directo y Muestreo por Rechazo

Este programa implementa dos métodos de inferencia probabilística basados en muestreo:
- Muestreo Directo: Se generan muestras completas directamente a partir de la distribución.
- Muestreo por Rechazo: Se generan muestras completas, pero se descartan aquellas que no coinciden con la evidencia.
Ambos métodos permiten aproximar distribuciones de probabilidad cuando la enumeración exacta es muy costosa.
"""

import random
from collections import Counter

# Red Bayesiana simple
# A es raíz, B depende de A, C depende de B

P = {
    'A': {True: 0.3, False: 0.7},
    'B|A': {
        (True,): {True: 0.8, False: 0.2},
        (False,): {True: 0.1, False: 0.9}
    },
    'C|B': {
        (True,): {True: 0.9, False: 0.1},
        (False,): {True: 0.2, False: 0.8}
    }
}

# Función auxiliar para hacer muestreo binario con una probabilidad dada
def sample_boolean(prob):
    return random.random() < prob

# Muestreo Directo (Forward Sampling)
def muestreo_directo(n_muestras):
    muestras = []
    for _ in range(n_muestras):
        muestra = {}

        # Muestra A
        a = sample_boolean(P['A'][True])
        muestra['A'] = a

        # Muestra B dado A
        b = sample_boolean(P['B|A'][(a,)][True])
        muestra['B'] = b

        # Muestra C dado B
        c = sample_boolean(P['C|B'][(b,)][True])
        muestra['C'] = c

        muestras.append(muestra)

    return muestras

# Muestreo por Rechazo
def muestreo_por_rechazo(n_muestras, evidencia):
    muestras = []
    intentos = 0
    while len(muestras) < n_muestras and intentos < n_muestras * 10:  # evitar bucles infinitos
        muestra = {}

        # Muestra A
        a = sample_boolean(P['A'][True])
        muestra['A'] = a

        # Muestra B dado A
        b = sample_boolean(P['B|A'][(a,)][True])
        muestra['B'] = b

        # Muestra C dado B
        c = sample_boolean(P['C|B'][(b,)][True])
        muestra['C'] = c

        intentos += 1

        # Verificar si la muestra coincide con la evidencia
        cumple = all(muestra.get(var) == val for var, val in evidencia.items())
        if cumple:
            muestras.append(muestra)

    return muestras

# Función para estimar distribución de una variable a partir de muestras
def estimar_distribucion(muestras, variable):
    contador = Counter(muestra[variable] for muestra in muestras)
    total = sum(contador.values())
    distribucion = {k: v / total for k, v in contador.items()}
    return distribucion

# ==== Prueba ====
n = 1000
print("\n===== Muestreo Directo =====")
muestras_directo = muestreo_directo(n)
dist_directa = estimar_distribucion(muestras_directo, 'C')
for val, prob in dist_directa.items():
    print(f"P(C={val}) ≈ {prob:.4f}")

print("\n===== Muestreo por Rechazo (evidencia: B=True) =====")
evidencia = {'B': True}
muestras_rechazo = muestreo_por_rechazo(n, evidencia)
if muestras_rechazo:
    dist_rechazo = estimar_distribucion(muestras_rechazo, 'C')
    for val, prob in dist_rechazo.items():
        print(f"P(C={val} | B=True) ≈ {prob:.4f}")
else:
    print("No se obtuvieron muestras suficientes que coincidan con la evidencia.")
