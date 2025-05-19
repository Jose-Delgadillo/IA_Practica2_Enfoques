"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Reglas de Producción  
Técnica: Reglas de Diagnóstico y Reglas Causales

Este programa ilustra cómo funcionan las reglas de diagnóstico y las reglas causales.
- Las **reglas causales** indican cómo ciertos hechos provocan otros.
- Las **reglas de diagnóstico** razonan hacia atrás: dada una observación, deducen causas posibles.

Se utiliza un motor de inferencia sencillo implementado en Python puro.
"""

# ----------------------------
# Base de conocimiento
# ----------------------------

hechos = set()

# Reglas causales: si "fiebre", entonces "sudoración"
reglas_causales = [
    ("fiebre", "sudoracion"),
    ("infeccion", "fiebre"),
    ("dolor_cabeza", "mareo"),
]

# Reglas de diagnóstico: si se observa "sudoración", entonces probablemente hubo "fiebre"
reglas_diagnostico = [
    ("sudoracion", "fiebre"),
    ("fiebre", "infeccion"),
    ("mareo", "dolor_cabeza"),
]

# ----------------------------
# Motor de inferencia causal (adelante)
# ----------------------------

def inferencia_causal(hechos_iniciales):
    """
    Aplica reglas causales hacia adelante: de causas conocidas, deduce efectos.
    """
    nuevos = set(hechos_iniciales)
    hechos_totales = set(hechos_iniciales)

    while nuevos:
        hecho = nuevos.pop()
        for causa, efecto in reglas_causales:
            if causa == hecho and efecto not in hechos_totales:
                hechos_totales.add(efecto)
                nuevos.add(efecto)
    return hechos_totales

# ----------------------------
# Motor de inferencia diagnóstica (hacia atrás)
# ----------------------------

def inferencia_diagnostico(observaciones):
    """
    Aplica reglas de diagnóstico hacia atrás: de síntomas u observaciones deduce causas posibles.
    """
    posibles_causas = set(observaciones)
    nuevos = set(observaciones)

    while nuevos:
        observado = nuevos.pop()
        for efecto, posible_causa in reglas_diagnostico:
            if efecto == observado and posible_causa not in posibles_causas:
                posibles_causas.add(posible_causa)
                nuevos.add(posible_causa)
    return posibles_causas

# ----------------------------
# Ejemplo de uso
# ----------------------------

print("==== Modo Causal ====")
hechos = {"infeccion"}
resultado_causal = inferencia_causal(hechos)
print("Hechos iniciales:", hechos)
print("Hechos deducidos (causal):", resultado_causal)

print("\n==== Modo Diagnóstico ====")
observaciones = {"sudoracion"}
resultado_diagnostico = inferencia_diagnostico(observaciones)
print("Observaciones:", observaciones)
print("Posibles causas (diagnóstico):", resultado_diagnostico)
