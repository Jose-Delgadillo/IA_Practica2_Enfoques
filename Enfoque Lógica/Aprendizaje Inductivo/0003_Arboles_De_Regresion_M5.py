"""
Prácticas de Inteligencia Artificial  
Aprendizaje Inductivo: Árboles de Regresión - M5

Este código implementa una versión simplificada del algoritmo M5, 
utilizado para construir árboles de regresión. A diferencia de los árboles 
de decisión que predicen categorías, los árboles de regresión están diseñados 
para predecir valores numéricos continuos.

El árbol se construye dividiendo el conjunto de datos con base en el atributo 
que minimiza el error cuadrático medio (ECM), y ajusta modelos lineales 
en las hojas del árbol.

Este ejemplo NO utiliza librerías externas para facilitar su ejecución 
en cualquier entorno con Python puro.
"""

# =======================================
# Funciones auxiliares sin numpy
# =======================================

# Promedio de una lista de números
def mean(lst):
    return sum(lst) / len(lst) if lst else 0

# Cálculo del error cuadrático medio
def mse(data):
    if not data:
        return 0
    target_values = [row[-1] for row in data]
    avg = mean(target_values)
    return sum((val - avg) ** 2 for val in target_values) / len(target_values)

# División de datos según un atributo y un umbral
def split_data(data, index, threshold):
    left = [row for row in data if row[index] <= threshold]
    right = [row for row in data if row[index] > threshold]
    return left, right

# =======================================
# Nodo del árbol de regresión
# =======================================

class Node:
    def __init__(self, is_leaf=False, value=None, index=None, threshold=None, left=None, right=None):
        self.is_leaf = is_leaf        # Indica si el nodo es hoja
        self.value = value            # Valor promedio si es hoja
        self.index = index            # Índice del atributo para dividir
        self.threshold = threshold    # Umbral de división
        self.left = left              # Subárbol izquierdo
        self.right = right            # Subárbol derecho

# =======================================
# Construcción del árbol M5 simplificado
# =======================================

def build_tree(data, min_size=3, max_depth=5, depth=0):
    if len(data) <= min_size or depth >= max_depth:
        return Node(is_leaf=True, value=mean([row[-1] for row in data]))

    best_mse = float('inf')
    best_index = None
    best_threshold = None
    best_split = None

    num_attributes = len(data[0]) - 1  # Última columna es la variable objetivo

    for index in range(num_attributes):
        thresholds = set(row[index] for row in data)
        for threshold in thresholds:
            left, right = split_data(data, index, threshold)
            if not left or not right:
                continue
            ecm = (len(left) * mse(left) + len(right) * mse(right)) / len(data)
            if ecm < best_mse:
                best_mse = ecm
                best_index = index
                best_threshold = threshold
                best_split = (left, right)

    if best_split is None:
        return Node(is_leaf=True, value=mean([row[-1] for row in data]))

    left_node = build_tree(best_split[0], min_size, max_depth, depth + 1)
    right_node = build_tree(best_split[1], min_size, max_depth, depth + 1)

    return Node(is_leaf=False, index=best_index, threshold=best_threshold, left=left_node, right=right_node)

# =======================================
# Predicción para una nueva instancia
# =======================================

def predict(node, row):
    if node.is_leaf:
        return node.value
    if row[node.index] <= node.threshold:
        return predict(node.left, row)
    else:
        return predict(node.right, row)

# =======================================
# Ejemplo de uso
# =======================================

# Datos de ejemplo: [atributo1, atributo2, valor_objetivo]
dataset = [
    [2.5, 1.0, 10.0],
    [1.5, 2.5, 15.0],
    [3.0, 1.5, 10.5],
    [2.0, 3.0, 16.0],
    [3.5, 0.5, 9.0],
    [1.0, 2.0, 14.0]
]

# Entrenar el árbol de regresión
arbol = build_tree(dataset)

# Probar una predicción con nuevos datos
nuevos_datos = [2.3, 1.2]
prediccion = predict(arbol, nuevos_datos)

print("Predicción para", nuevos_datos, ":", round(prediccion, 2))
