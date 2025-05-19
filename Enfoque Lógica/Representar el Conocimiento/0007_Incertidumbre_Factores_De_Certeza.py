"""
Prácticas de Inteligencia Artificial
Enfoque: Razonamiento
Subtema: Incertidumbre y Factores de Certeza

Este programa muestra cómo representar y combinar factores de certeza (CF) para
razonamiento bajo incertidumbre. Los factores de certeza permiten cuantificar
el grado de confianza en una conclusión basada en evidencias parciales.

Se modela un sistema experto simple con reglas que asocian evidencias con conclusiones
y sus correspondientes CF. También se muestra cómo combinar CFs usando las reglas clásicas.
"""

# Representación de hechos con factores de certeza
# Ejemplo: {"fiebre": 0.8} indica un 80% de certeza que hay fiebre
hechos = {
    "fiebre": 0.8,
    "tos": 0.6,
    "dolor_garganta": 0.7
}

# Reglas con factores de certeza asociados
# Cada regla asocia evidencias con conclusiones y su CF
reglas = [
    {
        "evidencias": ["fiebre", "tos"],
        "conclusion": "gripe",
        "cf_regla": 0.9  # grado de certeza de la regla
    },
    {
        "evidencias": ["dolor_garganta"],
        "conclusion": "resfriado",
        "cf_regla": 0.7
    }
]

def combinar_cf(cf1, cf2):
    """
    Combina dos factores de certeza según las reglas clásicas:
    Si ambos positivos:
        CFcombinado = cf1 + cf2*(1 - cf1)
    Si ambos negativos:
        CFcombinado = cf1 + cf2*(1 + cf1)
    Si signos opuestos:
        CFcombinado = (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))
    """
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    elif cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    else:
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

def inferir(hechos, reglas):
    """
    Inferir conclusiones combinando factores de certeza según las reglas y evidencias.
    """
    conclusiones = {}

    for regla in reglas:
        evidencias = regla["evidencias"]
        cf_regla = regla["cf_regla"]
        conclusion = regla["conclusion"]

        # Obtener CF mínimo de las evidencias en hechos
        cf_evidencias = min([hechos.get(ev, 0) for ev in evidencias])

        # Calcular CF para la conclusión: cf_evidencias * cf_regla
        cf_conclusion = cf_evidencias * cf_regla

        # Combinar CFs si la conclusión ya existe
        if conclusion in conclusiones:
            cf_antiguo = conclusiones[conclusion]
            cf_nuevo = combinar_cf(cf_antiguo, cf_conclusion)
            conclusiones[conclusion] = cf_nuevo
        else:
            conclusiones[conclusion] = cf_conclusion

    return conclusiones

if __name__ == "__main__":
    print("Hechos iniciales con factores de certeza:")
    for hecho, cf in hechos.items():
        print(f" - {hecho}: CF={cf}")

    print("\nAplicando reglas para inferir conclusiones con CF:")
    conclusiones = inferir(hechos, reglas)

    for concl, cf in conclusiones.items():
        print(f" - {concl}: CF={cf:.2f}")
