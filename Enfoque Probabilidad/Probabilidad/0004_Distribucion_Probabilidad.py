"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Distribución de Probabilidad

Una distribución de probabilidad representa todas las posibles asignaciones de probabilidad a los valores de una variable aleatoria.

Este programa define una variable aleatoria discreta que representa el clima, y muestra su distribución de probabilidad,
es decir, la probabilidad de que el clima sea Soleado, Nublado o Lluvioso.

El total de probabilidades debe sumar 1 (100%).
"""

# Definimos la variable aleatoria "Clima"
# y su distribución de probabilidad asociada
distribucion_clima = {
    "Soleado": 0.6,
    "Nublado": 0.3,
    "Lluvioso": 0.1
}

# Mostramos la distribución
print("======= Distribución de Probabilidad: Clima =======")
suma_total = 0
for estado, probabilidad in distribucion_clima.items():
    print(f"P(Clima = {estado}) = {probabilidad}")
    suma_total += probabilidad

# Verificamos si es una distribución válida (suma debe ser 1)
print("\n¿Distribución válida?:", "Sí" if abs(suma_total - 1.0) < 1e-6 else "No")
print(f"Suma total de probabilidades: {suma_total}")

