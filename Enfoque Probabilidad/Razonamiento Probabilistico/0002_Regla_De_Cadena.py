"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Regla de la Cadena

La Regla de la Cadena permite descomponer la probabilidad conjunta de múltiples variables
como el producto de probabilidades condicionales.

Para tres variables A, B, C:
    P(A, B, C) = P(A) * P(B | A) * P(C | A, B)

Este ejemplo utiliza variables relacionadas con un sistema de alarma:
- Robo
- Terremoto
- Alarma
"""

# Probabilidades individuales y condicionales
P_robo = 0.01
P_terremoto = 0.02

# P(alarma | robo, terremoto)
P_alarma_dado_robo_terremoto = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

def probabilidad_conjunta(robo, terremoto, alarma):
    """
    Calcula la probabilidad conjunta: P(robo, terremoto, alarma)
    usando la Regla de la Cadena:
        P(robo, terremoto, alarma) = P(robo) * P(terremoto) * P(alarma | robo, terremoto)
    """
    P_R = P_robo if robo else 1 - P_robo
    P_T = P_terremoto if terremoto else 1 - P_terremoto
    P_A_dado_RT = P_alarma_dado_robo_terremoto[(robo, terremoto)] if alarma else 1 - P_alarma_dado_robo_terremoto[(robo, terremoto)]

    return P_R * P_T * P_A_dado_RT

# Probabilidad conjunta de que haya un robo, un terremoto y que suene la alarma
P_rta = probabilidad_conjunta(robo=True, terremoto=True, alarma=True)

# Mostrar resultado
print("======== Regla de la Cadena ========")
print(f"P(robo=True, terremoto=True, alarma=True) = {P_rta:.6f}")
