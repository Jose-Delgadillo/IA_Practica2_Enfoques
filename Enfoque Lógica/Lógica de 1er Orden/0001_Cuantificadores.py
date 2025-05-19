"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Lógica de Primer Orden  
Técnica: Sintaxis y Semántica – Cuantificadores

Este programa demuestra el uso y evaluación de cuantificadores lógicos:
- El cuantificador universal (∀): "para todo"
- El cuantificador existencial (∃): "existe al menos uno"

A través de ejemplos simples, se simula la evaluación de fórmulas lógicas con estos cuantificadores
usando Python puro, sobre un dominio finito de elementos.
"""

# ----------------------------
# Definimos un dominio (universo de discurso)
# ----------------------------
universo = [1, 2, 3, 4, 5]

# ----------------------------
# Predicados (funciones que representan condiciones)
# ----------------------------

def es_par(x):
    """Predicado: x es un número par"""
    return x % 2 == 0

def mayor_que_dos(x):
    """Predicado: x es mayor que 2"""
    return x > 2

# ----------------------------
# Cuantificador Universal: ∀x P(x)
# ----------------------------

def cuantificador_universal(predicado, dominio):
    """
    Verifica si el predicado es verdadero para TODOS los elementos del dominio.
    Equivale a ∀x P(x)
    """
    for x in dominio:
        if not predicado(x):
            return False  # Si hay uno falso, toda la fórmula es falsa
    return True

# ----------------------------
# Cuantificador Existencial: ∃x P(x)
# ----------------------------

def cuantificador_existencial(predicado, dominio):
    """
    Verifica si el predicado es verdadero para ALGÚN elemento del dominio.
    Equivale a ∃x P(x)
    """
    for x in dominio:
        if predicado(x):
            return True  # Si hay al menos uno verdadero, es verdadero
    return False

# ----------------------------
# Evaluaciones
# ----------------------------

print("Universo:", universo)

# ∀x es_par(x)
print("\n¿Todos los elementos son pares? (∀x es_par(x))")
print(cuantificador_universal(es_par, universo))  # Falso

# ∃x es_par(x)
print("\n¿Existe al menos un elemento par? (∃x es_par(x))")
print(cuantificador_existencial(es_par, universo))  # Verdadero

# ∀x mayor_que_dos(x)
print("\n¿Todos los elementos son mayores que 2? (∀x mayor_que_dos(x))")
print(cuantificador_universal(mayor_que_dos, universo))  # Falso

# ∃x mayor_que_dos(x)
print("\n¿Existe al menos un elemento mayor que 2? (∃x mayor_que_dos(x))")
print(cuantificador_existencial(mayor_que_dos, universo))  # Verdadero
