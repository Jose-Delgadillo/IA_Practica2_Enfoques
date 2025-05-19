"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Mejor Hipótesis Actual

Este código implementa una simulación básica del algoritmo de búsqueda
de la mejor hipótesis actual (también conocida como "versión más específica")
en un espacio de hipótesis tipo CANDIDATE-ELIMINATION.

Se representa cada hipótesis como una lista de atributos, donde un valor
concreto representa una condición específica, y el símbolo '?' representa
cualquier valor (generalización).

Este ejemplo NO utiliza librerías externas y está orientado a datos categóricos.
"""

# Conjunto de entrenamiento simple: cada entrada es (atributos, clase)
# Los atributos son de forma: [color, forma, tamaño]
datos = [
    (["rojo", "círculo", "grande"], "sí"),
    (["rojo", "cuadro", "grande"], "sí"),
    (["azul", "círculo", "grande"], "no"),
    (["rojo", "círculo", "pequeño"], "sí")
]

# Hipótesis inicial: la más específica posible (⊥)
# Usamos None para representar que no se ha generalizado aún
hipotesis = [None, None, None]

# Función para actualizar la mejor hipótesis actual
def actualizar_hipotesis(h, x):
    nueva = []
    for i in range(len(h)):
        if h[i] is None:
            nueva.append(x[i])  # Iniciar con primer ejemplo positivo
        elif h[i] == x[i]:
            nueva.append(h[i])  # Coincide, se conserva
        else:
            nueva.append("?")   # Generalizar
    return nueva

# Algoritmo: actualiza la hipótesis solo con ejemplos positivos
for atributos, clase in datos:
    if clase == "sí":
        hipotesis = actualizar_hipotesis(hipotesis, atributos)

# Mostrar la mejor hipótesis encontrada
print("Mejor hipótesis actual:", hipotesis)

# Clasificación de un nuevo ejemplo
nuevo = ["rojo", "cuadro", "grande"]

def clasificar(h, x):
    for i in range(len(h)):
        if h[i] != "?" and h[i] != x[i]:
            return "no"
    return "sí"

print("Ejemplo:", nuevo)
print("Clasificación:", clasificar(hipotesis, nuevo))
