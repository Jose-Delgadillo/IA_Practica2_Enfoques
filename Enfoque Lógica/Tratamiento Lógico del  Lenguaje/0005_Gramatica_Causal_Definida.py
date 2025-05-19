"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Gramática Causal Definida

Este código implementa un parser simple con gramáticas causales definidas (DCG)
simuladas en Python, para analizar oraciones simples en español.

Se utiliza una función recursiva que corresponde a reglas gramaticales,
retornando un árbol sintáctico si la oración es válida.

Este código es puro Python sin librerías externas.
"""

# Reglas gramaticales: verbo, sustantivo, artículo, etc.
def verbo(tokens):
    if tokens and tokens[0] in ['ama', 'come', 'salta', 've', 'tiene']:
        return ('V', tokens[0]), tokens[1:]
    return None

def sustantivo(tokens):
    if tokens and tokens[0] in ['juan', 'maria', 'perro', 'manzana', 'pajaro']:
        return ('N', tokens[0]), tokens[1:]
    return None

def articulo(tokens):
    if tokens and tokens[0] in ['el', 'la', 'los', 'las', 'un', 'una']:
        return ('ART', tokens[0]), tokens[1:]
    return None

def nombre(tokens):
    # nombre -> articulo + sustantivo
    r1 = articulo(tokens)
    if r1:
        art, resto = r1
        r2 = sustantivo(resto)
        if r2:
            sn, resto2 = r2
            return ('NP', art, sn), resto2
    return None

def verbo_nombre(tokens):
    # verbo_nombre -> verbo + nombre
    r1 = verbo(tokens)
    if r1:
        v, resto = r1
        r2 = nombre(resto)
        if r2:
            np, resto2 = r2
            return ('VP', v, np), resto2
    return None

def oracion(tokens):
    # oracion -> nombre + verbo_nombre
    r1 = nombre(tokens)
    if r1:
        np, resto = r1
        r2 = verbo_nombre(resto)
        if r2:
            vp, resto2 = r2
            return ('S', np, vp), resto2
    return None

def analizar(texto):
    tokens = texto.lower().strip('.').split()
    resultado = oracion(tokens)
    if resultado and resultado[1] == []:
        arbol, _ = resultado
        print(f"Análisis exitoso para: '{texto}'")
        print("Árbol:", arbol)
    else:
        print(f"Error en análisis para: '{texto}'")

# Ejemplos de análisis
oraciones = [
    "El Juan ama la Maria.",
    "La Maria come una manzana.",
    "El perro salta.",
    "Juan ve el pajaro.",
    "La Maria tiene un perro."
]

for o in oraciones:
    analizar(o)
    print()
