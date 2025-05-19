"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Gramáticas - Jerarquía de Chomsky

Este código presenta una implementación básica para ilustrar la Jerarquía de Chomsky,
que clasifica gramáticas formales en cuatro niveles: tipo 0 (gramáticas irrestrictas),
tipo 1 (gramáticas sensibles al contexto), tipo 2 (gramáticas independientes del contexto)
y tipo 3 (gramáticas regulares).

El propósito es demostrar, mediante ejemplos simples, las diferencias en la estructura
y capacidad generativa de cada tipo de gramática.

El código está escrito en Python puro para facilitar su comprensión y ejecución.
"""

# Definición básica de gramáticas en la Jerarquía de Chomsky

# Gramática tipo 3: Gramática regular (ejemplo sencillo)
gramatica_tipo3 = {
    "S": ["aS", "b"]
}

# Gramática tipo 2: Gramática independiente del contexto (ejemplo)
gramatica_tipo2 = {
    "S": ["aSb", "ab"]
}

# Gramática tipo 1: Gramática sensible al contexto (ejemplo simplificado)
gramatica_tipo1 = {
    "AB": ["aABb", "ab"]
}

# Gramática tipo 0: Gramática irrestricta (ejemplo muy simple)
gramatica_tipo0 = {
    "S": ["SS", "a"]
}

# Función para generar cadenas a partir de una gramática dada (muy básica y limitada)
def generar_cadenas(gramatica, simbolo_inicial, max_profundidad=4):
    resultados = set()

    def expandir(cadena, profundidad):
        if profundidad > max_profundidad:
            return
        # Si la cadena no tiene símbolos no terminales (mayúsculas), es una cadena terminal
        if all(c.islower() for c in cadena):
            resultados.add(cadena)
            return
        # Expandir primer símbolo no terminal encontrado
        for i, c in enumerate(cadena):
            if c.isupper():
                no_terminal = c
                for produccion in gramatica.get(no_terminal, []):
                    nueva_cadena = cadena[:i] + produccion + cadena[i+1:]
                    expandir(nueva_cadena, profundidad +1)
                break

    expandir(simbolo_inicial, 0)
    return resultados

# Probar generación para cada tipo de gramática
print("Gramática Tipo 3 (Regular):")
print(generar_cadenas(gramatica_tipo3, "S"))

print("\nGramática Tipo 2 (Independiente del Contexto):")
print(generar_cadenas(gramatica_tipo2, "S"))

print("\nGramática Tipo 1 (Sensibles al Contexto) - Simplificada:")
print(generar_cadenas(gramatica_tipo1, "AB"))

print("\nGramática Tipo 0 (Irrestricta) - Simplificada:")
print(generar_cadenas(gramatica_tipo0, "S"))
