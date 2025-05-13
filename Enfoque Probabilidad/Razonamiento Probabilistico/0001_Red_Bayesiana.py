"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Red Bayesiana

Una Red Bayesiana es un modelo probabilístico gráfico que representa dependencias condicionales entre variables aleatorias mediante un grafo dirigido.

Este ejemplo muestra una red bayesiana simple con tres variables:
- Lluvia
- Aspersor (rociador de jardín)
- Césped mojado

Estructura de dependencias:
- Lluvia influye en si se enciende el aspersor
- Lluvia y el aspersor influyen en si el césped está mojado
"""

def probabilidad_marginal(prob_lluvia, prob_aspersor_dado_lluvia, prob_mojado_dado_lluvia_y_aspersor):
    """
    Calcula la probabilidad de que el césped esté mojado, considerando todas las combinaciones
    de lluvia y aspersor.
    """
    P_mojado = 0.0
    for lluvia in [True, False]:
        for aspersor in [True, False]:
            # Probabilidad de lluvia o no lluvia
            P_L = prob_lluvia if lluvia else 1 - prob_lluvia

            # Probabilidad de aspersor dado lluvia
            P_A_dado_L = prob_aspersor_dado_lluvia[lluvia] if aspersor else 1 - prob_aspersor_dado_lluvia[lluvia]

            # Probabilidad de césped mojado dado lluvia y aspersor
            P_M_dado_LA = prob_mojado_dado_lluvia_y_aspersor[(lluvia, aspersor)]

            # Regla de probabilidad total
            P_mojado += P_L * P_A_dado_L * P_M_dado_LA

    return P_mojado


# Definimos las probabilidades de la red bayesiana
P_lluvia = 0.3  # Probabilidad de que llueva

# Probabilidad de que se encienda el aspersor según si llueve
P_aspersor_dado_lluvia = {
    True: 0.01,   # Si llueve, rara vez se enciende el aspersor
    False: 0.4    # Si no llueve, es más probable que se encienda
}

# Probabilidad de que el césped esté mojado dado lluvia y aspersor
P_mojado_dado_lluvia_y_aspersor = {
    (True, True): 0.99,
    (True, False): 0.9,
    (False, True): 0.8,
    (False, False): 0.0
}

# Calcular probabilidad marginal de que el césped esté mojado
P_mojado = probabilidad_marginal(P_lluvia, P_aspersor_dado_lluvia, P_mojado_dado_lluvia_y_aspersor)

# Mostrar resultado
print("======== Red Bayesiana ========")
print(f"Probabilidad de que el césped esté mojado: {P_mojado:.4f}")
