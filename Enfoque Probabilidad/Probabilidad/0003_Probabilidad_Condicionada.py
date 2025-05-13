"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Probabilidad Condicionada y Normalización

Este programa demuestra cómo calcular probabilidades condicionadas y cómo normalizar los resultados.

La probabilidad condicionada P(A|B) expresa la probabilidad de que ocurra el evento A,
dado que sabemos que ocurrió el evento B.

Ejemplo:
Supongamos que tenemos un sensor que detecta si hay humo.
Queremos saber la probabilidad de que haya fuego dado que hay humo (P(Fuego|Humo)).

Datos:
- P(Fuego) = 0.01            → Probabilidad de que haya fuego.
- P(¬Fuego) = 0.99           → Probabilidad de que NO haya fuego.
- P(Humo|Fuego) = 0.9        → Probabilidad de que haya humo si hay fuego.
- P(Humo|¬Fuego) = 0.1       → Probabilidad de que haya humo si NO hay fuego.
"""

# Probabilidades a priori
P_Fuego = 0.01
P_NoFuego = 0.99

# Probabilidades condicionales
P_Humo_dado_Fuego = 0.9
P_Humo_dado_NoFuego = 0.1

# Paso 1: Cálculo de la probabilidad conjunta
# P(Fuego ∩ Humo) = P(Humo|Fuego) * P(Fuego)
# P(¬Fuego ∩ Humo) = P(Humo|¬Fuego) * P(¬Fuego)
P_Humo_y_Fuego = P_Humo_dado_Fuego * P_Fuego
P_Humo_y_NoFuego = P_Humo_dado_NoFuego * P_NoFuego

# Paso 2: Normalización
# P(Fuego|Humo) = P(Fuego ∩ Humo) / [P(Fuego ∩ Humo) + P(¬Fuego ∩ Humo)]
normalizador = P_Humo_y_Fuego + P_Humo_y_NoFuego
P_Fuego_dado_Humo = P_Humo_y_Fuego / normalizador
P_NoFuego_dado_Humo = P_Humo_y_NoFuego / normalizador

# Resultados
print("======= Probabilidad Condicionada y Normalización =======")
print(f"P(Humo ∩ Fuego)     = {P_Humo_y_Fuego:.5f}")
print(f"P(Humo ∩ ¬Fuego)    = {P_Humo_y_NoFuego:.5f}")
print(f"Suma para normalizar= {normalizador:.5f}\n")

print(f"P(Fuego|Humo)       = {P_Fuego_dado_Humo:.5f}")
print(f"P(¬Fuego|Humo)      = {P_NoFuego_dado_Humo:.5f}")

# Comprobación
print(f"\nVerificación: P(Fuego|Humo) + P(¬Fuego|Humo) = {P_Fuego_dado_Humo + P_NoFuego_dado_Humo:.5f}")

#P(Fuego|Humo)       = 0.08333
#P(¬Fuego|Humo)      = 0.91667
#Aunque la probabilidad de que haya fuego es solo del 1%, al detectar humo, la probabilidad sube a más del 8%.