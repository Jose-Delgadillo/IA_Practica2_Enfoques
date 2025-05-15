"""
Prácticas de Inteligencia Artificial
Aprendizaje Probabilístico: Agrupamiento No Supervisado (K-Means)

Este programa implementa el algoritmo de agrupamiento K-Means, el cual divide un conjunto de puntos
en k grupos (clusters) basándose en su cercanía a los centroides. No se requiere conocimiento previo
de las clases, por lo que se considera un método de aprendizaje no supervisado.
"""

import random
import math

# ---------------------------
# Función para calcular distancia euclidiana entre dos puntos
def distancia(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# ---------------------------
# Inicializar centroides aleatorios dentro del rango de los datos
def inicializar_centroides(k, datos):
    dimensiones = len(datos[0])
    centroides = []
    for _ in range(k):
        centroide = [random.uniform(min(d[i] for d in datos), max(d[i] for d in datos)) for i in range(dimensiones)]
        centroides.append(centroide)
    return centroides

# ---------------------------
# Asignar cada punto de datos al centroide más cercano
def asignar_a_clusters(datos, centroides):
    clusters = [[] for _ in centroides]
    for punto in datos:
        distancias = [distancia(punto, centroide) for centroide in centroides]
        indice_mas_cercano = distancias.index(min(distancias))
        clusters[indice_mas_cercano].append(punto)
    return clusters

# ---------------------------
# Recalcular los centroides como el promedio de los puntos en cada grupo
def actualizar_centroides(clusters):
    nuevos_centroides = []
    for grupo in clusters:
        if grupo:
            nuevo_centroide = [sum(d[i] for d in grupo) / len(grupo) for i in range(len(grupo[0]))]
        else:
            # Si un cluster queda vacío, se reasigna un centroide aleatorio
            nuevo_centroide = [random.random() for _ in range(len(grupo[0]))]
        nuevos_centroides.append(nuevo_centroide)
    return nuevos_centroides

# ---------------------------
# Algoritmo principal K-Means
def k_means(datos, k, iteraciones=10):
    centroides = inicializar_centroides(k, datos)

    for i in range(iteraciones):
        print(f"\n--- Iteración {i + 1} ---")
        clusters = asignar_a_clusters(datos, centroides)

        # Mostrar los clusters actuales
        for idx, grupo in enumerate(clusters):
            print(f"Cluster {idx + 1}: {grupo}")

        # Actualizar centroides
        centroides = actualizar_centroides(clusters)

        # Mostrar centroides
        for idx, c in enumerate(centroides):
            print(f"Centroide {idx + 1}: {c}")

    return clusters, centroides

# ---------------------------
# Datos de entrada: puntos 2D simulados
datos = [
    [1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0],
    [1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0],
    [9.0, 3.0]
]

# Número de grupos (clusters)
k = 3

# Ejecutar el algoritmo K-Means
clusters, centroides = k_means(datos, k)

# ---------------------------
# Mostrar resultados finales
print("\n--- Resultado Final ---")
for i, grupo in enumerate(clusters):
    print(f"Cluster {i + 1} (Centroide: {centroides[i]}): {grupo}")
