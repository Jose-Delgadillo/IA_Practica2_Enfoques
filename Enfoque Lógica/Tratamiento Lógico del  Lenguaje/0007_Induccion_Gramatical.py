"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Inducción Gramatical

Este código ilustra un ejemplo básico y simplificado de inducción gramatical,
es decir, la construcción automática de reglas gramaticales a partir de
un conjunto pequeño de oraciones (corpus) de ejemplo.

El programa toma frases simples y extrae reglas gramaticales muy básicas
basadas en la estructura de palabras y su posición.

Este ejemplo NO utiliza librerías externas y es solo para fines ilustrativos.
"""

# Corpus de oraciones simples de ejemplo (listas de palabras)
corpus = [
    ["el", "gato", "come"],
    ["el", "perro", "ladra"],
    ["un", "gato", "duerme"],
    ["el", "perro", "come"],
]

# Función que induce reglas gramaticales simples:
# - Determina categorías para palabras según posición y aparición en corpus.
def inducir_gramatica(corpus):
    # Diccionario para categorías: palabra -> categoría
    categorias = {}

    # Reglas simples por posición:
    # posición 0: determinantes (Det)
    # posición 1: sustantivos (N)
    # posición 2: verbos (V)
    
    for oracion in corpus:
        if len(oracion) >= 3:
            det, sust, verbo = oracion[0], oracion[1], oracion[2]
            categorias[det] = 'Det'
            categorias[sust] = 'N'
            categorias[verbo] = 'V'
    
    # Generar reglas gramaticales básicas
    reglas = [
        "S -> Det N V",
        "Det -> " + " | ".join(sorted({w for w,c in categorias.items() if c == 'Det'})),
        "N -> " + " | ".join(sorted({w for w,c in categorias.items() if c == 'N'})),
        "V -> " + " | ".join(sorted({w for w,c in categorias.items() if c == 'V'})),
    ]
    
    return reglas

# Ejecutar inducción
reglas_inducidas = inducir_gramatica(corpus)

print("Gramática inducida a partir del corpus:")
for regla in reglas_inducidas:
    print(regla)
