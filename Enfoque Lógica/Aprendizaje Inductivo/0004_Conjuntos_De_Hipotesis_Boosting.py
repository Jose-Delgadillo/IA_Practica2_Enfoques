"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Conjuntos de Hipótesis - Boosting

Este código implementa una versión simplificada del algoritmo AdaBoost,
un método de conjunto que combina múltiples clasificadores débiles 
(árboles de decisión de un nivel) para formar un clasificador fuerte.

Boosting ajusta los errores de predicción aumentando el peso de las 
instancias mal clasificadas para los siguientes clasificadores.

Este ejemplo NO usa librerías externas y funciona con datos sencillos
para facilitar su comprensión y ejecución.
"""

# Datos de ejemplo binarios (atributo único y clase binaria)
# Formato: [atributo, clase]
datos = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 0],
    [4, 1],
    [5, 0]
]

# Clasificador débil: umbral binario (stump)
def clasificador_debil(x, umbral, direccion):
    return 1 if (x > umbral if direccion == 1 else x <= umbral) else 0

# AdaBoost simplificado
def adaboost(datos, rondas=3):
    pesos = [1 / len(datos)] * len(datos)
    clasificadores = []

    for ronda in range(rondas):
        mejor_error = 1
        mejor_umbral = None
        mejor_dir = None
        mejor_pred = []

        # Probar todos los umbrales posibles
        for umbral in range(max(d[0] for d in datos)):
            for direccion in [1, -1]:
                predicciones = [clasificador_debil(d[0], umbral, direccion) for d in datos]
                error = sum(p for i, p in enumerate(pesos) if predicciones[i] != datos[i][1])

                if error < mejor_error:
                    mejor_error = error
                    mejor_umbral = umbral
                    mejor_dir = direccion
                    mejor_pred = predicciones

        # Calcular el peso del clasificador
        if mejor_error == 0:
            mejor_error = 1e-10  # Evitar división por cero
        alpha = 0.5 * (1.0 - mejor_error) / (mejor_error + 1e-10)
        clasificadores.append((mejor_umbral, mejor_dir, alpha))

        # Actualizar pesos
        for i in range(len(pesos)):
            if mejor_pred[i] == datos[i][1]:
                pesos[i] *= (1 - alpha)
            else:
                pesos[i] *= (1 + alpha)

        # Normalizar
        total = sum(pesos)
        pesos = [p / total for p in pesos]

    return clasificadores

# Clasificación final
def clasificar(x, clasificadores):
    score = 0
    for umbral, direccion, alpha in clasificadores:
        pred = clasificador_debil(x, umbral, direccion)
        score += alpha if pred == 1 else -alpha
    return 1 if score > 0 else 0

# Entrenar y evaluar
modelo = adaboost(datos, rondas=3)

print("Clasificación de nuevos ejemplos:")
for x in range(6):
    resultado = clasificar(x, modelo)
    print(f"Entrada: {x} → Clase predicha: {resultado}")
