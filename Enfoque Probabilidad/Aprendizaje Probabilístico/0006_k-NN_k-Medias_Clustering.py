import random
import math

# ---------- FUNCIONES AUXILIARES ----------

def distancia_euclidiana(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

def generar_datos(n, centros, dispersion=1.0):
    datos = []
    for cx, cy in centros:
        for _ in range(n):
            x = random.gauss(cx, dispersion)
            y = random.gauss(cy, dispersion)
            datos.append((x, y))
    return datos

# ---------- K-MEANS CLUSTERING ----------

def k_means(datos, k, iteraciones=100):
    centroides = random.sample(datos, k)
    for _ in range(iteraciones):
        clusters = [[] for _ in range(k)]
        for punto in datos:
            distancias = [distancia_euclidiana(punto, c) for c in centroides]
            indice = distancias.index(min(distancias))
            clusters[indice].append(punto)

        nuevos_centroides = []
        for cluster in clusters:
            if cluster:
                nuevo_centro = tuple(sum(p[i] for p in cluster) / len(cluster) for i in range(len(cluster[0])))
            else:
                nuevo_centro = random.choice(datos)
            nuevos_centroides.append(nuevo_centro)

        if nuevos_centroides == centroides:
            break
        centroides = nuevos_centroides

    return clusters, centroides

# ---------- K-NN CLASIFICADOR ----------

def knn_clasificar(puntos_etiquetados, nuevo_punto, k=3):
    distancias = [(distancia_euclidiana(punto, nuevo_punto), etiqueta) for punto, etiqueta in puntos_etiquetados]
    distancias.sort(key=lambda x: x[0])
    k_vecinos = distancias[:k]
    
    etiquetas = {}
    for _, etiqueta in k_vecinos:
        etiquetas[etiqueta] = etiquetas.get(etiqueta, 0) + 1
    
    return max(etiquetas.items(), key=lambda x: x[1])[0]

# ---------- MAIN ----------

# Generar datos simulados
centros = [(2, 2), (8, 3), (3, 7)]
datos = generar_datos(n=20, centros=centros)

# Ejecutar k-means
k = 3
clusters, centroides = k_means(datos, k)

print("\n--- Agrupamiento por k-Means ---")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1} (centro: {centroides[i]}):")
    for punto in cluster:
        print(f"  {punto}")
    print()

# Crear conjunto etiquetado para k-NN (usamos los clusters como clases)
datos_etiquetados = []
for i, cluster in enumerate(clusters):
    for punto in cluster:
        datos_etiquetados.append((punto, f"Clase {i + 1}"))

# Clasificar un nuevo punto con k-NN
nuevo_punto = (5, 5)
etiqueta_predicha = knn_clasificar(datos_etiquetados, nuevo_punto, k=3)

print("--- Clasificación k-NN ---")
print(f"Punto nuevo: {nuevo_punto}")
print(f"Clasificación predicha: {etiqueta_predicha}")
