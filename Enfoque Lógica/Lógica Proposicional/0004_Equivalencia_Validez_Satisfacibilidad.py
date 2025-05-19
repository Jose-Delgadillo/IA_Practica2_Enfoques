"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Lógica Proposicional: Equivalencia, Validez y Satisfacibilidad

Este programa evalúa proposiciones lógicas para determinar:
- **Equivalencia lógica**: si dos proposiciones tienen la misma tabla de verdad.
- **Validez**: si una proposición es verdadera en todas las combinaciones de valores.
- **Satisfacibilidad**: si existe al menos una combinación que hace verdadera una proposición.

Usamos tablas de verdad completas sin librerías externas para representar las funciones lógicas.
"""
from itertools import product

# --- Definir conectivos lógicos como funciones ---
def NOT(p): return not p
def AND(p, q): return p and q
def OR(p, q): return p or q
def IMPLIES(p, q): return (not p) or q
def IFF(p, q): return p == q  # bicondicional: si y solo si

# --- Construir tabla de verdad para una proposición ---
def tabla_verdad(expr, variables):
    resultados = []
    for valores in product([False, True], repeat=len(variables)):
        contexto = dict(zip(variables, valores))
        resultado = expr(**contexto)
        resultados.append((valores, resultado))
    return resultados

# --- Comprobar validez: ¿siempre True? ---
def es_valida(tabla):
    return all(resultado for _, resultado in tabla)

# --- Comprobar satisfacibilidad: ¿al menos un True? ---
def es_satisfacible(tabla):
    return any(resultado for _, resultado in tabla)

# --- Comprobar equivalencia entre dos expresiones ---
def son_equivalentes(expr1, expr2, variables):
    t1 = tabla_verdad(expr1, variables)
    t2 = tabla_verdad(expr2, variables)
    return all(r1 == r2 for (_, r1), (_, r2) in zip(t1, t2))

# --- Ejemplo de uso ---
# Variables: p, q
# Proposición: (p → q) ≡ (¬p ∨ q)

def proposicion1(p, q):
    return IMPLIES(p, q)

def proposicion2(p, q):
    return OR(NOT(p), q)

# Generar y mostrar tablas
vars = ["p", "q"]
tabla1 = tabla_verdad(proposicion1, vars)
tabla2 = tabla_verdad(proposicion2, vars)

print("Tabla de verdad de (p → q):")
for fila in tabla1:
    print(f"{fila[0]} => {fila[1]}")

print("\nTabla de verdad de (¬p ∨ q):")
for fila in tabla2:
    print(f"{fila[0]} => {fila[1]}")

# Equivalencia
print("\n¿Son equivalentes?:", son_equivalentes(proposicion1, proposicion2, vars))

# Validez y satisfacibilidad
print("¿Es (p → q) válida?:", es_valida(tabla1))
print("¿Es (p → q) satisfacible?:", es_satisfacible(tabla1))
