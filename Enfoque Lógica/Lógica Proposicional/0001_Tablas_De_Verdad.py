"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Lógica Proposicional: Sintaxis y Semántica – Tablas de Verdad

Este programa genera la tabla de verdad de una expresión lógica proposicional compuesta.
Permite estudiar su semántica (valores de verdad) a partir de su sintaxis formal.
La lógica proposicional es la base para razonamiento lógico, resolución y verificación
de argumentos en Inteligencia Artificial simbólica.
"""
import itertools

# --- Evaluador simple de expresiones proposicionales ---
def evaluar(expr, valores):
    for var, val in valores.items():
        expr = expr.replace(var, str(val))
    return eval(expr)

# --- Generador de tabla de verdad ---
def tabla_de_verdad(expresion, variables):
    print("\nTabla de Verdad para:", expresion)
    print(" | ".join(variables) + " | Resultado")
    print("-" * (len(variables)*4 + 11))

    # Generar todas las combinaciones posibles de valores (0,1)
    for valores_binarios in itertools.product([0, 1], repeat=len(variables)):
        valores = dict(zip(variables, valores_binarios))
        try:
            resultado = int(evaluar(expresion, valores))
        except:
            resultado = "Error"
        fila = " | ".join(str(valores[v]) for v in variables)
        print(f"{fila} |    {resultado}")

# --- Variables proposicionales y expresión lógica ---
# Puedes usar:
# - and: conjunción (∧)
# - or: disyunción (∨)
# - not: negación (¬)
# - => implica usar una forma válida como: (not A or B)  para representar A → B
# - <=> se representa como igualdad lógica: A == B
# Ejemplo: "(A and B) or not C"
variables = ['A', 'B', 'C']
expresion = "(A and B) or not C"

# --- Generar tabla de verdad ---
tabla_de_verdad(expresion, variables)
