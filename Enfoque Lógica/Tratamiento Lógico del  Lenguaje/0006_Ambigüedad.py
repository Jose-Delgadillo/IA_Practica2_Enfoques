"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Ambigüedad en Gramáticas

Este código muestra un ejemplo clásico de ambigüedad en gramáticas
a través de la frase "Vi al hombre con el telescopio".

La ambigüedad ocurre cuando una oración puede ser analizada
(decorada) con más de un árbol sintáctico válido.

Aquí se implementan dos posibles análisis manuales para la frase,
mostrando la ambigüedad sin usar librerías externas.
"""

def analizar_ambiguedad(oracion):
    """
    Analiza la frase "Vi al hombre con el telescopio" de dos maneras:
    1. Interpretación 1: 'Vi [al hombre] [con el telescopio]' (yo uso el telescopio)
    2. Interpretación 2: 'Vi [al hombre con el telescopio]' (el hombre tiene el telescopio)
    """
    print(f"Oración: '{oracion}'")
    
    # Interpretación 1: Yo veo al hombre usando el telescopio
    arbol_1 = {
        'S': [
            ('V', 'Vi'),
            ('NP', [
                ('Det', 'al'),
                ('N', 'hombre')
            ]),
            ('PP', [
                ('P', 'con'),
                ('NP', [
                    ('Det', 'el'),
                    ('N', 'telescopio')
                ])
            ])
        ]
    }
    
    # Interpretación 2: Yo veo al hombre que tiene el telescopio
    arbol_2 = {
        'S': [
            ('V', 'Vi'),
            ('NP', [
                ('Det', 'al'),
                ('N', 'hombre'),
                ('PP', [
                    ('P', 'con'),
                    ('NP', [
                        ('Det', 'el'),
                        ('N', 'telescopio')
                    ])
                ])
            ])
        ]
    }
    
    print("\nInterpretación 1: Yo uso el telescopio para ver al hombre")
    print_arbol(arbol_1)
    
    print("\nInterpretación 2: El hombre tiene el telescopio")
    print_arbol(arbol_2)

def print_arbol(arbol, nivel=0):
    """Función recursiva para imprimir árboles sintácticos de forma legible."""
    indent = '  ' * nivel
    if isinstance(arbol, dict):
        for clave, hijos in arbol.items():
            print(f"{indent}{clave}:")
            for hijo in hijos:
                print_arbol(hijo, nivel + 1)
    elif isinstance(arbol, tuple):
        print(f"{indent}{arbol[0]} -> {arbol[1]}")
    elif isinstance(arbol, list):
        for elemento in arbol:
            print_arbol(elemento, nivel)
    else:
        print(f"{indent}{arbol}")

# Ejecutar el análisis de ambigüedad para la frase
frase = "Vi al hombre con el telescopio"
analizar_ambiguedad(frase)
