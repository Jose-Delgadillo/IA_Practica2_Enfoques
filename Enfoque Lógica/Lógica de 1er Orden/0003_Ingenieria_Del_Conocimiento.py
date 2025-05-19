"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Ingeniería del Conocimiento

La Ingeniería del Conocimiento es el proceso de diseñar, construir y mantener sistemas
basados en conocimiento (SBC). Implica la captura, representación y uso del conocimiento
de expertos en un dominio particular para resolver problemas complejos.

Este ejemplo simula una pequeña base de conocimientos sobre diagnóstico de problemas en automóviles,
usando hechos, reglas y un motor de inferencia encadenado hacia adelante.
"""

# --------------------------------------
# Base de Conocimiento: Hechos y Reglas
# --------------------------------------

hechos = set()  # Contendrá hechos conocidos
reglas = [      # Reglas del tipo: (condiciones, conclusión)
    ({"no_arranca", "luces_debil"}, "bateria_muerta"),
    ({"motor_lento"}, "bujia_falla"),
    ({"bujia_falla"}, "necesita_mantenimiento"),
    ({"bateria_muerta"}, "reemplazar_bateria"),
    ({"combustible_bajo"}, "repostar_gasolina"),
]

# --------------------------------------
# Motor de Inferencia hacia Adelante
# --------------------------------------

def inferencia_adelante(hechos_iniciales, reglas):
    """
    Aplica encadenamiento hacia adelante para deducir nuevos hechos
    a partir de las reglas y los hechos actuales.
    """
    hechos = set(hechos_iniciales)  # copia local de los hechos
    nuevos = True  # bandera para saber si seguimos encontrando hechos nuevos

    while nuevos:
        nuevos = False
        for condiciones, conclusion in reglas:
            # Si todas las condiciones se cumplen y la conclusión no ha sido añadida
            if condiciones.issubset(hechos) and conclusion not in hechos:
                hechos.add(conclusion)
                nuevos = True
                print(f"Se infiere: {conclusion} (porque se cumple {condiciones})")

    return hechos

# --------------------------------------
# Simulación: Ingreso de hechos iniciales
# --------------------------------------

hechos_iniciales = {"no_arranca", "luces_debil"}
print("Hechos iniciales:", hechos_iniciales)

# Ejecutamos la inferencia
hechos_deducidos = inferencia_adelante(hechos_iniciales, reglas)

print("\nHechos finales deducidos:")
for hecho in hechos_deducidos:
    print("-", hecho)
