"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Incertidumbre

Este programa ilustra cómo se puede modelar la incertidumbre en la Inteligencia Artificial usando conceptos básicos de probabilidad.

Objetivo:
Mostrar cómo calcular y representar probabilidades simples y condicionales
en un entorno donde hay incertidumbre sobre lo que está ocurriendo.

Ejemplo:
Imaginemos un sensor que detecta si está lloviendo, pero no es 100% confiable.
- La probabilidad de que llueva realmente (P(Lluvia)) es del 30%.
- El sensor puede decir que "hay lluvia" o "no hay lluvia".
- El sensor detecta lluvia correctamente el 90% de las veces.
- Pero a veces da falsas alarmas (detecta lluvia cuando no la hay) con 10%.

Este escenario es común en IA cuando los agentes deben tomar decisiones con
información incompleta o ruidosa.

"""

# Probabilidades conocidas
P_lluvia = 0.3               # Probabilidad de que llueva
P_no_lluvia = 1 - P_lluvia   # Probabilidad de que no llueva

# Sensor: Probabilidad de detección dado que llueve
P_sensor_si_lluvia = 0.9     # Sensor detecta lluvia correctamente
P_sensor_si_no_lluvia = 0.1  # Sensor da falsa alarma

# Probabilidad total de que el sensor diga que llueve (Teorema de la probabilidad total)
P_sensor_lluvia = (
    P_sensor_si_lluvia * P_lluvia +
    P_sensor_si_no_lluvia * P_no_lluvia
)

# Aplicando el Teorema de Bayes:
# ¿Cuál es la probabilidad de que realmente esté lloviendo si el sensor dice que sí?
P_lluvia_dado_sensor = (
    (P_sensor_si_lluvia * P_lluvia) / P_sensor_lluvia
)

# Mostrar resultados
print("======= Escenario de Incertidumbre con Sensor =======")
print(f"P(Lluvia): {P_lluvia:.2f}")
print(f"P(No Lluvia): {P_no_lluvia:.2f}")
print(f"P(Sensor detecta lluvia | Lluvia): {P_sensor_si_lluvia:.2f}")
print(f"P(Sensor detecta lluvia | No Lluvia): {P_sensor_si_no_lluvia:.2f}")
print()
print(f"P(Sensor dice que llueve): {P_sensor_lluvia:.2f}")
print(f"P(Realmente está lloviendo | Sensor dice que llueve): {P_lluvia_dado_sensor:.2f}")
