"""
Prácticas de Inteligencia Artificial
Aprendizaje Probabilístico: k-NN, k-Medias y Clustering

Este programa implementa dos técnicas fundamentales del aprendizaje automático:
- k-NN (k-Nearest Neighbors): clasificación basada en ejemplos cercanos.
- k-Means: agrupamiento no supervisado basado en centroides.

Se generan datos sintéticos y se visualizan los resultados de agrupamiento.
"""

import random
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# -------------------------------
# Generar datos artificiales con 3 centros (clusters)
X, y_true = make_blobs(n_samples=150, centers=3, cluster_std=1.0, random_state=42)

# -------------------------------
# CLUSTERING CON K-MEANS

# Crear el modelo de K-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)  # Ajustar a los datos

# Obtener etiquetas asignadas por k-means
labels_kmeans = kmeans.labels_

# -------------------------------
# CLASIFICACIÓN CON K-NN

# Crear datos de entrenamiento aleatorios con etiquetas (supervisado)
# Tomaremos 20 puntos etiquetados aleatoriamente
indices_entrenamiento = random.sample(range(len(X)), 20)
X_entrenamiento = X[indices_entrenamiento]
y_entrenamiento = y_true[indices_entrenamiento]

# Crear el clasificador k-NN (usamos k=3 vecinos)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_entrenamiento, y_entrenamiento)

# Predecir etiquetas para todo el conjunto
y_pred = knn.predict(X)

# -------------------------------
# VISUALIZACIÓN DE RESULTADOS

# Mostrar resultados del clustering k-means
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Agrupamiento con K-Means")
plt.scatter(X[:, 0], X[:, 1], c=labels_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c='red', marker='x', label='Centroides')
plt.legend()

# Mostrar resultados del k-NN (clasificación supervisada)
plt.subplot(1, 2, 2)
plt.title("Clasificación con k-NN")
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='coolwarm')
plt.scatter(X_entrenamiento[:, 0], X_entrenamiento[:, 1],
            c='black', marker='x', label='Puntos etiquetados')
plt.legend()

plt.tight_layout()
plt.show()

#pip install scikit-learn matplotlib
