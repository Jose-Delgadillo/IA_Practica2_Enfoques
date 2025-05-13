"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Probabilidad a Priori

Este programa demuestra el uso de la probabilidad a priori (también conocida como probabilidad marginal),
la cual representa nuestro conocimiento inicial sobre un evento, antes de observar evidencia o datos adicionales.

En IA, estas probabilidades son útiles para modelar lo que un agente "cree" sobre el mundo antes de hacer observaciones.

Escenario:
Supongamos que un robot intenta determinar el tipo de clima con base en información histórica.
Sabemos que:
- El 60% de los días son soleados.
- El 30% son nublados.
- El 10% son lluviosos.

Estas probabilidades reflejan el conocimiento previo del robot sobre el clima: su creencia a priori.
"""

# Definimos las probabilidades a priori
P_soleado = 0.6     # Probabilidad de que el día sea soleado
P_nublado = 0.3     # Probabilidad de que el día sea nublado
P_lluvioso = 0.1    # Probabilidad de que el día sea lluvioso

# Mostramos las probabilidades
print("======= Probabilidad a Priori =======")
print(f"P(Soleado)  = {P_soleado}")
print(f"P(Nublado)  = {P_nublado}")
print(f"P(Lluvioso) = {P_lluvioso}")

# Comprobación: la suma de las probabilidades debe ser igual a 1
suma_total = P_soleado + P_nublado + P_lluvioso
print(f"\nSuma total de probabilidades: {suma_total}")
if abs(suma_total - 1.0) < 1e-6:
    print("✔ Las probabilidades están correctamente normalizadas.")
else:
    print("✘ Error: Las probabilidades no suman 1.")
