"""
Prácticas de Inteligencia Artificial
Tratamiento Lógico del Lenguaje: Análisis Semántico

Este código ilustra un análisis semántico muy básico, que interpreta oraciones simples 
en lenguaje natural para extraer relaciones sujetas-verbo-objeto, representándolas como 
estructuras de hechos lógicos.

El análisis semántico es la etapa que sigue al análisis sintáctico y tiene como objetivo 
comprender el significado de la oración, facilitando su uso en sistemas de razonamiento.

Este ejemplo está implementado en Python puro para facilitar su comprensión y ejecución.
"""

# Función simple para dividir la oración en palabras (tokens)
def tokenize(oracion):
    return oracion.strip('.').split()

# Función para extraer una relación sujeto-verbo-objeto básica de la oración
def extraer_relacion(oracion):
    tokens = tokenize(oracion)
    # En oraciones muy simples con estructura S V O, asignamos palabras
    if len(tokens) >= 3:
        sujeto = tokens[0]
        verbo = tokens[1]
        objeto = ' '.join(tokens[2:])
        return (sujeto, verbo, objeto)
    else:
        return None

# Ejemplo de oraciones simples
oraciones = [
    "Juan come manzanas.",
    "María lee un libro.",
    "El perro persigue al gato.",
    "Ana bebe agua."
]

print("Análisis semántico básico (relaciones sujeto-verbo-objeto):")
for oracion in oraciones:
    relacion = extraer_relacion(oracion)
    if relacion:
        sujeto, verbo, objeto = relacion
        print(f"Oración: '{oracion}'")
        print(f"  Sujeto: {sujeto}")
        print(f"  Verbo: {verbo}")
        print(f"  Objeto: {objeto}")
    else:
        print(f"No se pudo extraer relación de: {oracion}")
