"""
Prácticas de Inteligencia Artificial
Tema: Probabilidad - Regla de Bayes

La Regla de Bayes nos permite actualizar nuestras creencias sobre una hipótesis a partir de nueva evidencia.

Fórmula:
    P(H | E) = (P(E | H) * P(H)) / P(E)

Donde:
    H: Hipótesis (por ejemplo, que una persona tenga una enfermedad)
    E: Evidencia (por ejemplo, que el test sea positivo)
"""

# Datos del problema (ejemplo típico de diagnóstico médico)
P_enfermedad = 0.01               # Probabilidad previa de tener la enfermedad
P_no_enfermedad = 1 - P_enfermedad

P_positivo_dado_enfermedad = 0.99  # Sensibilidad: P(+ | enfermedad)
P_positivo_dado_no_enfermedad = 0.05  # Falsos positivos: P(+ | no enfermedad)

# Queremos calcular: P(enfermedad | positivo)

# Paso 1: Calcular la probabilidad total del test positivo (P(E))
P_positivo = (P_positivo_dado_enfermedad * P_enfermedad) + (P_positivo_dado_no_enfermedad * P_no_enfermedad)

# Paso 2: Aplicar la Regla de Bayes
P_enfermedad_dado_positivo = (P_positivo_dado_enfermedad * P_enfermedad) / P_positivo

# Mostramos resultados
print("======== Regla de Bayes ========")
print(f"P(Enfermedad | Test Positivo) = {P_enfermedad_dado_positivo:.4f}")
print(f"P(Enfermedad) = {P_enfermedad}")
print(f"P(Positivo | Enfermedad) = {P_positivo_dado_enfermedad}")
print(f"P(Positivo | No Enfermedad) = {P_positivo_dado_no_enfermedad}")
print(f"P(Positivo) = {P_positivo:.4f}")

#Aunque el test es bastante preciso (99% de sensibilidad), la enfermedad es muy rara (1%), lo que hace que 
# incluso un resultado positivo tenga una baja probabilidad real de indicar enfermedad (probablemente cerca del 16%).