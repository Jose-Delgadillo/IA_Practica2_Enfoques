"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Listas de Decisión - K-DL y K-DT

Este código implementa dos enfoques de clasificación:
- K-DL (K-decision lists): Listas de reglas if-then-else encadenadas.
- K-DT (K-decision trees): Árboles de decisión con profundidad máxima K.

Ambos métodos restringen la complejidad del modelo con una cota K,
para evitar sobreajuste y facilitar la interpretación.

Este ejemplo NO usa librerías externas y trabaja con datos binarios simples.
"""

# Datos binarios con dos atributos y clase 0 o 1
# Formato: [x1, x2, clase]
datos = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# Implementación de una lista de decisión (K-DL)
def k_dl(datos):
    reglas = []

    # Generamos reglas simples tipo: si x1==v1 y x2==v2 entonces clase
    for x1 in [0, 1]:
        for x2 in [0, 1]:
            for clase in [0, 1]:
                regla = lambda x, a1=x1, a2=x2, c=clase: c if x[0] == a1 and x[1] == a2 else None
                cubre = [fila for fila in datos if regla(fila) == fila[2]]
                if len(cubre) >= 2:  # Regla fuerte si acierta al menos 2 veces
                    reglas.append(regla)

    return reglas

# Clasificación con lista de decisión
def clasificar_dl(x, reglas):
    for regla in reglas:
        resultado = regla(x)
        if resultado is not None:
            return resultado
    return 0  # Por defecto

# Implementación de un árbol de decisión de profundidad 1 (K-DT con K=1)
def k_dt(datos, atributo=0):
    conteo = {0: 0, 1: 0}
    for fila in datos:
        if fila[atributo] == 1:
            conteo[fila[2]] += 1
    return 1 if conteo[1] > conteo[0] else 0

# Clasificación con árbol de profundidad 1
def clasificar_dt(x, atributo, clase_si_1):
    return clase_si_1 if x[atributo] == 1 else 1 - clase_si_1

# Entrenar ambos modelos
reglas_dl = k_dl(datos)
atributo_dt = 0
clase_dt = k_dt(datos, atributo=atributo_dt)

# Evaluar entradas
print("Evaluación con K-DL:")
for x in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    pred = clasificar_dl(x, reglas_dl)
    print(f"Entrada: {x} → Clase: {pred}")

print("\nEvaluación con K-DT (atributo x1):")
for x in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    pred = clasificar_dt(x, atributo_dt, clase_dt)
    print(f"Entrada: {x} → Clase: {pred}")
