"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Ponderación de Verosimilitud

Este método permite hacer inferencias aproximadas en redes bayesianas
cuando se tiene evidencia. A diferencia del muestreo por rechazo,
no descarta las muestras que no coinciden con la evidencia, sino que
les asigna un peso (verosimilitud) que indica qué tan consistentes
son con dicha evidencia.
"""

import random
from collections import defaultdict, Counter

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

# Función auxiliar para muestrear valores booleanos
def sample_boolean(prob):
    return random.random() < prob

# Ponderación de Verosimilitud
def ponderacion_verosimilitud(n_muestras, evidencia):
    muestras_ponderadas = []

    for _ in range(n_muestras):
        muestra = {}
        peso = 1.0

        # Muestra A
        a = sample_boolean(P['A'][True])
        muestra['A'] = a

        # B depende de A
        if 'B' in evidencia:
            prob_b = P['B|A'][(a,)][evidencia['B']]
            peso *= prob_b
            muestra['B'] = evidencia['B']
        else:
            b = sample_boolean(P['B|A'][(a,)][True])
            muestra['B'] = b

        # C depende de B
        b_val = muestra['B']
        if 'C' in evidencia:
            prob_c = P['C|B'][(b_val,)][evidencia['C']]
            peso *= prob_c
            muestra['C'] = evidencia['C']
        else:
            c = sample_boolean(P['C|B'][(b_val,)][True])
            muestra['C'] = c

        muestras_ponderadas.append((muestra, peso))

    return muestras_ponderadas

# Función para estimar la distribución de una variable ponderada por pesos
def estimar_distribucion_ponderada(muestras_ponderadas, variable):
    conteo_ponderado = defaultdict(float)
    for muestra, peso in muestras_ponderadas:
        conteo_ponderado[muestra[variable]] += peso

    total = sum(conteo_ponderado.values())
    distribucion = {k: v / total for k, v in conteo_ponderado.items()}
    return distribucion

# ==== Prueba del método ====
n = 1000
evidencia = {'B': True}

print("\n===== Ponderación de Verosimilitud =====")
muestras = ponderacion_verosimilitud(n, evidencia)
distribucion = estimar_distribucion_ponderada(muestras, 'C')

for val, prob in distribucion.items():
    print(f"P(C={val} | B=True) ≈ {prob:.4f}")
