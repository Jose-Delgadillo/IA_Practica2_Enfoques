"""
Prácticas de Inteligencia Artificial
Tratamiento Probabilístico del Lenguaje:
Gramáticas Probabilísticas Independientes del Contexto (PCFG)

Este programa implementa una gramática probabilística libre de contexto (PCFG),
donde cada regla de producción tiene una probabilidad asociada. Estas gramáticas se
utilizan para modelar lenguajes naturales permitiendo no solo generar frases gramaticalmente
correctas, sino también estimar qué tan probables son, lo cual es útil en tareas como análisis
sintáctico probabilístico o desambiguación de estructuras.

Este ejemplo simula el análisis de oraciones sencillas como "el gato duerme".
"""

import random

# Definimos una Gramática Probabilística Libre de Contexto como un diccionario:
# Cada clave es un símbolo no terminal, y su valor es una lista de tuplas:
# (probabilidad, expansión), donde expansión es una lista de símbolos (terminales o no terminales)

PCFG = {
    "S": [
        (1.0, ["NP", "VP"])  # S → NP VP con probabilidad 1.0
    ],
    "NP": [
        (0.5, ["Det", "N"]),     # NP → Det N
        (0.5, ["Det", "Adj", "N"])  # NP → Det Adj N
    ],
    "VP": [
        (0.6, ["V"]),             # VP → V
        (0.4, ["V", "NP"])        # VP → V NP
    ],
    "Det": [
        (0.5, ["el"]),            # Det → "el"
        (0.5, ["la"])             # Det → "la"
    ],
    "N": [
        (0.4, ["gato"]),
        (0.4, ["perro"]),
        (0.2, ["alfombra"])
    ],
    "Adj": [
        (0.5, ["negro"]),
        (0.5, ["grande"])
    ],
    "V": [
        (0.5, ["duerme"]),
        (0.5, ["ladra"])
    ]
}

def expandir_simbolo(simbolo):
    """
    Esta función toma un símbolo (no terminal o terminal) y lo expande recursivamente
    según las reglas de la gramática PCFG. Si es terminal, lo devuelve directamente.
    """
    if simbolo not in PCFG:
        return [simbolo]  # símbolo terminal
    else:
        # Escoger una regla de producción aleatoria basada en su probabilidad
        reglas = PCFG[simbolo]
        probs = [p for p, _ in reglas]
        elecciones = [r for _, r in reglas]
        eleccion = random.choices(elecciones, weights=probs)[0]

        # Expandir recursivamente cada símbolo de la expansión
        resultado = []
        for sub in eleccion:
            resultado.extend(expandir_simbolo(sub))
        return resultado

# Generar una oración aleatoria a partir del símbolo inicial 'S'
oracion_generada = expandir_simbolo("S")
print("Oración generada por la PCFG:")
print(" ".join(oracion_generada))
