"""
Prácticas de Inteligencia Artificial
Tratamiento Probabilístico del Lenguaje:
Gramáticas Probabilísticas Lexicalizadas

Una Gramática Probabilística Lexicalizada (L-PCFG) es una extensión de las PCFG,
donde cada regla de producción está asociada no solo a una probabilidad,
sino también a una palabra "cabeza léxica" (head word) que representa el núcleo semántico
de una frase o constituyente.

Estas gramáticas son útiles para modelar dependencias léxicas (como verbos con sus sujetos y objetos),
y mejorar el análisis sintáctico, ya que capturan información léxica en la estructura de la oración.

Este ejemplo genera oraciones sencillas con una estructura sintáctica simple y
asigna las cabezas léxicas a los constituyentes no terminales.
"""

import random

# Gramática probabilística lexicalizada: cada regla tiene probabilidad y reglas con cabezas
# Formato: { no_terminal: [(probabilidad, expansión, función para calcular la cabeza)] }

LPCFG = {
    "S": [
        (1.0, ["NP", "VP"], lambda heads: heads[1])  # La cabeza de S es la del VP
    ],
    "NP": [
        (0.5, ["Det", "N"], lambda heads: heads[1]),          # cabeza léxica = sustantivo
        (0.5, ["Det", "Adj", "N"], lambda heads: heads[2])    # cabeza léxica = sustantivo
    ],
    "VP": [
        (0.6, ["V"], lambda heads: heads[0]),                 # cabeza léxica = verbo
        (0.4, ["V", "NP"], lambda heads: heads[0])            # cabeza léxica = verbo
    ],
    "Det": [
        (0.5, ["el"], lambda _: "el"),
        (0.5, ["la"], lambda _: "la")
    ],
    "N": [
        (0.4, ["gato"], lambda _: "gato"),
        (0.4, ["perro"], lambda _: "perro"),
        (0.2, ["alfombra"], lambda _: "alfombra")
    ],
    "Adj": [
        (0.5, ["negro"], lambda _: "negro"),
        (0.5, ["grande"], lambda _: "grande")
    ],
    "V": [
        (0.5, ["duerme"], lambda _: "duerme"),
        (0.5, ["ladra"], lambda _: "ladra")
    ]
}

def expandir_con_cabeza(simbolo):
    """
    Expande recursivamente un símbolo no terminal según las reglas de la L-PCFG.
    Devuelve:
      - una lista de palabras terminales (la oración generada),
      - la palabra cabeza léxica del constituyente actual.
    """
    if simbolo not in LPCFG:
        # Terminal: devuelve la palabra y su propia cabeza (es ella misma)
        return [simbolo], simbolo

    # Elegir regla con base en la probabilidad
    reglas = LPCFG[simbolo]
    probs = [p for p, _, _ in reglas]
    elecciones = [r for _, r, _ in reglas]
    funciones = [f for _, _, f in reglas]

    indice = random.choices(range(len(reglas)), weights=probs)[0]
    expansion = elecciones[indice]
    funcion_cabeza = funciones[indice]

    resultado = []
    cabezas = []

    for sub in expansion:
        sub_oracion, sub_cabeza = expandir_con_cabeza(sub)
        resultado.extend(sub_oracion)
        cabezas.append(sub_cabeza)

    cabeza_final = funcion_cabeza(cabezas)
    return resultado, cabeza_final

# Generar una oración y mostrar la cabeza léxica de la oración completa
oracion, cabeza = expandir_con_cabeza("S")
print("Oración generada:")
print(" ".join(oracion))
print("Cabeza léxica de la oración (verbo principal):", cabeza)
