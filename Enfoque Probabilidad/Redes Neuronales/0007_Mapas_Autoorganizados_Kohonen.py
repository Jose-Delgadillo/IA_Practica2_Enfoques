"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Mapas Autoorganizados de Kohonen (SOM)

Este programa implementa un Mapa Autoorganizado de Kohonen (Self-Organizing Map, SOM),
que es un tipo de red neuronal no supervisada. Los SOM proyectan datos de alta dimensión
en un espacio de menor dimensión (normalmente 2D), conservando la topología de los datos.

Esto se logra entrenando una red con vecinos autoajustables, donde las neuronas compiten
por representar patrones de entrada y se adaptan para parecerse a los datos observados.
"""

import random
import math

# -------------------------
# Parámetros del SOM
# -------------------------

ANCHO = 5          # Número de neuronas en la dimensión horizontal
ALTO = 5           # Número de neuronas en la dimensión vertical
DIMENSION = 2      # Dimensión del vector de entrada
EPOCAS = 100       # Número de iteraciones de entrenamiento
TASA_INICIAL = 0.1 # Tasa de aprendizaje inicial
RADIO_INICIAL = max(ANCHO, ALTO) / 2.0 # Radio inicial de vecindario

# -------------------------
# Funciones matemáticas
# -------------------------

def distancia_euclidiana(vec1, vec2):
    """Calcula la distancia euclidiana entre dos vectores."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec1, vec2)))

def vector_suma(vec1, vec2):
    """Suma dos vectores componente a componente."""
    return [a + b for a, b in zip(vec1, vec2)]

def vector_escala(vec, escalar):
    """Multiplica un vector por un escalar."""
    return [a * escalar for a in vec]

# -------------------------
# Inicialización del SOM
# -------------------------

def inicializar_som():
    """Crea una red SOM con pesos aleatorios entre 0 y 1."""
    return [[[random.random() for _ in range(DIMENSION)] for _ in range(ANCHO)] for _ in range(ALTO)]

# -------------------------
# Búsqueda de la BMU (Best Matching Unit)
# -------------------------

def encontrar_bmu(som, entrada):
    """Encuentra la neurona con el peso más cercano al vector de entrada."""
    mejor = None
    menor_distancia = float('inf')
    for i in range(ALTO):
        for j in range(ANCHO):
            distancia = distancia_euclidiana(som[i][j], entrada)
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor = (i, j)
    return mejor

# -------------------------
# Entrenamiento del SOM
# -------------------------

def entrenar_som(som, datos):
    """Entrena el SOM usando los datos de entrada."""
    for epoca in range(EPOCAS):
        # Calcular tasa y radio de vecindario decaídos
        tasa = TASA_INICIAL * (1 - epoca / EPOCAS)
        radio = RADIO_INICIAL * (1 - epoca / EPOCAS)
        radio_cuadrado = radio ** 2

        for entrada in datos:
            # 1. Encontrar la BMU
            bmu_i, bmu_j = encontrar_bmu(som, entrada)

            # 2. Actualizar pesos de la BMU y sus vecinos
            for i in range(ALTO):
                for j in range(ANCHO):
                    # Calcular distancia al cuadrado en el mapa
                    dist_cuadrada = (i - bmu_i) ** 2 + (j - bmu_j) ** 2
                    if dist_cuadrada <= radio_cuadrado:
                        influencia = math.exp(-dist_cuadrada / (2 * radio_cuadrado))
                        for d in range(DIMENSION):
                            som[i][j][d] += tasa * influencia * (entrada[d] - som[i][j][d])

        # Mostrar progreso
        if epoca % 10 == 0:
            print(f"Época {epoca}: tasa={round(tasa, 3)}, radio={round(radio, 3)}")

# -------------------------
# Prueba y visualización
# -------------------------

def mostrar_resultados(som, datos):
    """Muestra la ubicación de los datos en el mapa entrenado."""
    print("\nResultados después del entrenamiento:")
    for entrada in datos:
        bmu = encontrar_bmu(som, entrada)
        print(f"Entrada {entrada} mapeada en la neurona {bmu}")

# -------------------------
# Programa principal
# -------------------------

if __name__ == "__main__":
    # Datos de entrada artificiales (vectores 2D)
    datos = [
        [0.1, 0.2],
        [0.2, 0.1],
        [0.8, 0.9],
        [0.9, 0.8],
        [0.45, 0.55],
        [0.5, 0.4],
    ]

    som = inicializar_som()
    entrenar_som(som, datos)
    mostrar_resultados(som, datos)
