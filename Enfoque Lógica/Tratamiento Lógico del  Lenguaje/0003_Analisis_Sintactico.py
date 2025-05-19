"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Análisis Sintáctico

Este código muestra un ejemplo simple de análisis sintáctico para oraciones en español,
usando una gramática muy básica y recursiva para construir árboles sintácticos.

El análisis sintáctico consiste en determinar la estructura gramatical de una oración,
identificando sus componentes principales como sujeto, verbo y objeto.

Este ejemplo está implementado en Python puro sin librerías externas, para facilitar su comprensión.
"""

# Definición de una gramática muy simple: reglas para frases nominales (SN), verbales (SV) y oraciones (S)
GRAMATICA = {
    'S': [['SN', 'SV']],
    'SN': [['Det', 'N'], ['N']],
    'SV': [['V', 'SN'], ['V']],
    'Det': ['el', 'la', 'un', 'una', 'los', 'las'],
    'N': ['juan', 'maria', 'perro', 'gato', 'libro', 'agua', 'manzana'],
    'V': ['come', 'lee', 'bebe', 'persigue']
}

# Función para verificar si una palabra es un determinante
def es_det(palabra):
    return palabra in GRAMATICA['Det']

# Función para verificar si una palabra es un sustantivo
def es_n(palabra):
    return palabra in GRAMATICA['N']

# Función para verificar si una palabra es un verbo
def es_v(palabra):
    return palabra in GRAMATICA['V']

# Parser simple que intenta analizar una frase nominal (SN)
def parse_SN(tokens):
    # Caso Det + N
    if len(tokens) >= 2 and es_det(tokens[0]) and es_n(tokens[1]):
        return ('SN', [tokens[0], tokens[1]]), tokens[2:]
    # Caso N solo
    if len(tokens) >= 1 and es_n(tokens[0]):
        return ('SN', [tokens[0]]), tokens[1:]
    return None, tokens

# Parser simple que intenta analizar una frase verbal (SV)
def parse_SV(tokens):
    # Caso V + SN
    if len(tokens) >= 2 and es_v(tokens[0]):
        sn, resto = parse_SN(tokens[1:])
        if sn:
            return ('SV', [tokens[0], sn]), resto
        else:
            return ('SV', [tokens[0]]), tokens[1:]
    # Caso V solo
    if len(tokens) >= 1 and es_v(tokens[0]):
        return ('SV', [tokens[0]]), tokens[1:]
    return None, tokens

# Parser para una oración (S)
def parse_S(tokens):
    sn, resto = parse_SN(tokens)
    if not sn:
        return None, tokens
    sv, resto2 = parse_SV(resto)
    if not sv:
        return None, tokens
    return ('S', [sn, sv]), resto2

# Función para analizar la oración y mostrar el árbol sintáctico
def analizar(oracion):
    tokens = oracion.lower().strip('.').split()
    arbol, resto = parse_S(tokens)
    if arbol and not resto:
        print(f"Análisis sintáctico correcto para: '{oracion}'")
        print("Árbol sintáctico:", arbol)
    else:
        print(f"Error de análisis sintáctico en: '{oracion}'")

# Ejemplos de oraciones para analizar
oraciones = [
    "Juan come manzana.",
    "La María lee un libro.",
    "El perro persigue el gato.",
    "Ana bebe agua."
]

for o in oraciones:
    analizar(o)
