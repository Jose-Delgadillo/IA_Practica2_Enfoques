"""
Prácticas de Inteligencia Artificial
Enfoque: Razonamiento
Subtema: Sistemas Expertos con Factores de Certeza (CF)

Este programa implementa un sistema experto simple que utiliza reglas con factores de certeza
para razonar bajo incertidumbre. 

- Los hechos iniciales tienen un grado de certeza.
- Las reglas relacionan evidencias con conclusiones y tienen un CF que indica su fuerza.
- El motor de inferencia combina CFs para llegar a conclusiones con un grado de confianza.
"""

# Definición de los hechos iniciales con sus factores de certeza
hechos = {
    "fiebre": 0.9,
    "tos": 0.8,
    "dolor_garganta": 0.7,
    "fatiga": 0.6,
}

# Definición de las reglas del sistema experto
reglas = [
    {
        "evidencias": ["fiebre", "tos"],
        "conclusion": "gripe",
        "cf_regla": 0.85
    },
    {
        "evidencias": ["dolor_garganta", "fatiga"],
        "conclusion": "resfriado",
        "cf_regla": 0.7
    },
    {
        "evidencias": ["fiebre", "fatiga", "dolor_garganta"],
        "conclusion": "infección",
        "cf_regla": 0.9
    },
]

def combinar_cf(cf1, cf2):
    """
    Combina dos factores de certeza (CF) según las reglas de sistemas expertos (ejemplo basado en MYCIN):

    - Si ambos CFs son positivos:
        CF_combinado = cf1 + cf2 * (1 - cf1)
    - Si ambos CFs son negativos:
        CF_combinado = cf1 + cf2 * (1 + cf1)
    - Si signos opuestos:
        CF_combinado = (cf1 + cf2) / (1 - min(|cf1|, |cf2|))

    Args:
        cf1 (float): primer factor de certeza (-1 a 1)
        cf2 (float): segundo factor de certeza (-1 a 1)

    Returns:
        float: CF combinado
    """
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    elif cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    else:
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

def inferir(hechos, reglas):
    """
    Inferir conclusiones basadas en hechos y reglas, calculando factores de certeza.

    - Para cada regla:
        - Se obtiene el CF mínimo entre las evidencias presentes en los hechos (AND lógico).
        - Se multiplica este CF por el CF de la regla para obtener el CF de la conclusión.
        - Si la conclusión ya existe, se combinan los CFs.

    Args:
        hechos (dict): hechos con sus factores de certeza.
        reglas (list): reglas con evidencias, conclusión y CF.

    Returns:
        dict: conclusiones con sus factores de certeza combinados.
    """
    conclusiones = {}

    for regla in reglas:
        evidencias = regla["evidencias"]
        cf_regla = regla["cf_regla"]
        conclusion = regla["conclusion"]

        # Obtener CF de las evidencias, 0 si no está presente el hecho
        cf_evidencias = min([hechos.get(ev, 0) for ev in evidencias])

        # CF conclusión es producto de evidencias y regla
        cf_conclusion = cf_evidencias * cf_regla

        # Combinar con posible CF previo de la misma conclusión
        if conclusion in conclusiones:
            cf_prev = conclusiones[conclusion]
            cf_comb = combinar_cf(cf_prev, cf_conclusion)
            conclusiones[conclusion] = cf_comb
        else:
            conclusiones[conclusion] = cf_conclusion

    return conclusiones

if __name__ == "__main__":
    print("Hechos iniciales y sus factores de certeza:")
    for hecho, cf in hechos.items():
        print(f" - {hecho}: CF = {cf}")

    print("\nInferencia del sistema experto:")
    resultados = inferir(hechos, reglas)

    if resultados:
        for concl, cf in resultados.items():
            print(f" - {concl}: CF = {cf:.2f}")
    else:
        print("No se pudieron inferir conclusiones con los hechos dados.")
