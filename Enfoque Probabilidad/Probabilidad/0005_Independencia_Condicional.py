"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Independencia Condicional

La independencia condicional describe una situación en la que dos eventos (o variables aleatorias) A y B son independientes
dado un tercer evento C. Es decir:
    P(A | B, C) = P(A | C)

Este programa muestra un ejemplo sencillo basado en una red causal:
    Causa: Lluvia
    Evidencia: Césped mojado
    Variable intermedia: Rociador activado

La idea es mostrar que, dado que sabemos si el césped está mojado, el conocimiento del rociador no nos aporta
información adicional sobre si llovió o no.
"""

# Definimos las probabilidades condicionales (hipotéticas) basadas en observaciones
P_lluvia = 0.2                     # P(Lluvia)
P_rociador = 0.3                  # P(Rociador)
P_cesped_mojado_dado_lluvia_y_rociador = 0.99
P_cesped_mojado_dado_lluvia_y_no_rociador = 0.9
P_cesped_mojado_dado_no_lluvia_y_rociador = 0.8
P_cesped_mojado_dado_no_lluvia_y_no_rociador = 0.0

# Queremos mostrar que:
# P(Lluvia | Césped mojado, Rociador) ≈ P(Lluvia | Césped mojado)

# Suponemos valores observados para los eventos
lluvia = True
rociador = True
cesped_mojado = True

# Para simplificar, simulamos valores que muestran independencia condicional

# Probabilidades hipotéticas
P_lluvia_y_rociador_y_mojado = 0.2 * 0.3 * 0.99
P_lluvia_y_mojado = 0.2 * (0.3 * 0.99 + 0.7 * 0.9)
P_mojado_y_rociador = (0.2 * 0.3 * 0.99) + (0.8 * 0.3 * 0.8)
P_mojado = P_lluvia_y_mojado + 0.8 * (0.3 * 0.8 + 0.7 * 0)

# Cálculos de probabilidades condicionales
P_lluvia_dado_mojado_y_rociador = P_lluvia_y_rociador_y_mojado / P_mojado_y_rociador
P_lluvia_dado_mojado = P_lluvia_y_mojado / P_mojado

# Mostramos los resultados
print("======= Independencia Condicional =======")
print(f"P(Lluvia | Césped mojado, Rociador) ≈ {P_lluvia_dado_mojado_y_rociador:.4f}")
print(f"P(Lluvia | Césped mojado) ≈ {P_lluvia_dado_mojado:.4f}")

print("\n¿Es aproximadamente igual?:", "Sí" if abs(P_lluvia_dado_mojado_y_rociador - P_lluvia_dado_mojado) < 0.05 else "No")
