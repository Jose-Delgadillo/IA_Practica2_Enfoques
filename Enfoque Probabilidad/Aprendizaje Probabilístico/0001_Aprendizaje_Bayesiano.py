"""
Prácticas de Inteligencia Artificial
Aprendizaje Probabilístico: Aprendizaje Bayesiano

Este programa ejemplifica cómo el conocimiento previo (probabilidad a priori) se ajusta
en función de la evidencia observada (verosimilitud), utilizando la Regla de Bayes para
calcular la probabilidad posterior de una hipótesis.

Se muestra cómo el aprendizaje se mejora con más datos, lo cual es fundamental
en problemas de inferencia probabilística, clasificación y diagnóstico automático.
"""

# Lista de posibles hipótesis
hipotesis = ['H1', 'H2', 'H3']

# Probabilidades a priori para cada hipótesis
p_hipotesis = {
    'H1': 0.3,
    'H2': 0.4,
    'H3': 0.3
}

# Verosimilitudes: probabilidad de observar la evidencia si cada hipótesis es cierta
# Por ejemplo: P(evidencia | H1)
verosimilitud = {
    'H1': 0.2,
    'H2': 0.6,
    'H3': 0.8
}

# Función que aplica la Regla de Bayes para obtener la probabilidad posterior
def aprendizaje_bayesiano(p_hipotesis, verosimilitud):
    posterior = {}

    # Calcular el denominador de la Regla de Bayes (probabilidad total de la evidencia)
    evidencia_total = sum(p_hipotesis[h] * verosimilitud[h] for h in hipotesis)

    # Calcular la probabilidad posterior para cada hipótesis
    for h in hipotesis:
        posterior[h] = (verosimilitud[h] * p_hipotesis[h]) / evidencia_total

    return posterior

# Ejecutar el aprendizaje bayesiano
posterior_actualizado = aprendizaje_bayesiano(p_hipotesis, verosimilitud)

# Mostrar los resultados
print("===== Aprendizaje Bayesiano =====")
print("Probabilidades a priori:")
for h in hipotesis:
    print(f"P({h}) = {p_hipotesis[h]}")

print("\nVerosimilitudes (P(Evidencia | H)):")
for h in hipotesis:
    print(f"P(Evidencia | {h}) = {verosimilitud[h]}")

print("\nProbabilidades posteriores:")
for h in hipotesis:
    print(f"P({h} | Evidencia) = {posterior_actualizado[h]:.4f}")
