"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Análisis Léxico

Este código implementa un analizador léxico simple que procesa una cadena de texto
y la divide en una lista de tokens o lexemas, clasificando cada token en categorías
básicas como palabras, números, signos de puntuación y espacios.

El análisis léxico es la primera etapa en el procesamiento del lenguaje natural,
transformando texto plano en unidades significativas para posteriores etapas como
el análisis sintáctico o semántico.

Este ejemplo está implementado en Python puro para facilitar su comprensión y ejecución.
"""

# Función para clasificar un carácter en tipo de token básico
def clasificar_caracter(c):
    if c.isalpha():
        return 'PALABRA'
    elif c.isdigit():
        return 'NUMERO'
    elif c.isspace():
        return 'ESPACIO'
    else:
        return 'PUNTUACION'

# Función para realizar el análisis léxico simple
def analizador_lexico(texto):
    tokens = []
    token_actual = ''
    tipo_actual = None

    for c in texto:
        tipo_c = clasificar_caracter(c)
        if tipo_c == tipo_actual:
            token_actual += c
        else:
            if token_actual:
                tokens.append((token_actual, tipo_actual))
            token_actual = c
            tipo_actual = tipo_c
    # Añadir el último token si existe
    if token_actual:
        tokens.append((token_actual, tipo_actual))
    return tokens

# Ejemplo de uso
texto_ejemplo = "Hola, ¿cómo estás? Tengo 2 gatos y 1 perro."

resultado = analizador_lexico(texto_ejemplo)

print("Tokens obtenidos del análisis léxico:")
for token, tipo in resultado:
    print(f"{token!r}: {tipo}")
