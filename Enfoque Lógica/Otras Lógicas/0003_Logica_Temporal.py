"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógica Temporal

La lógica temporal es una extensión de la lógica clásica que introduce operadores que
razonan sobre el tiempo. Estos operadores permiten expresar proposiciones como:
- F(p): "eventualmente p" (en el futuro)
- G(p): "siempre p" (siempre será verdadero)
- X(p): "próximo p" (p será verdadero en el siguiente instante)
- P(p): "anteriormente p" (fue verdadero en el pasado)

Este programa simula un sistema de evaluación temporal sobre una línea de tiempo discreta,
donde se analiza si una proposición cumple con estos operadores.
"""

# Línea de tiempo simulada: lista de estados (instantes)
# Cada instante contiene un conjunto de proposiciones verdaderas en ese momento
tiempo = [
    {"p"},          # t0
    {"q"},          # t1
    {"p", "q"},     # t2
    {"r"},          # t3
    set(),          # t4
    {"p"},          # t5
]

# Operador F(p): "eventualmente p" en algún instante futuro
def eventualmente(prop, tiempo, t):
    for i in range(t, len(tiempo)):
        if prop in tiempo[i]:
            return True
    return False

# Operador G(p): "siempre p" en todos los instantes futuros
def siempre(prop, tiempo, t):
    for i in range(t, len(tiempo)):
        if prop not in tiempo[i]:
            return False
    return True

# Operador X(p): "próximo p", es decir, si p ocurre en el siguiente instante
def siguiente(prop, tiempo, t):
    if t + 1 < len(tiempo):
        return prop in tiempo[t + 1]
    return False

# Operador P(p): "anteriormente p", si ocurrió en algún instante pasado
def anteriormente(prop, tiempo, t):
    for i in range(0, t):
        if prop in tiempo[i]:
            return True
    return False

# -------------------------------
# Evaluaciones en un instante dado
# -------------------------------
t_actual = 2
print(f"Instante actual: t{t_actual}")
print("Proposiciones verdaderas en este instante:", tiempo[t_actual])
print()

# Evaluaciones para la proposición 'p'
print("F(p): eventualmente p =", eventualmente("p", tiempo, t_actual))
print("G(p): siempre p =", siempre("p", tiempo, t_actual))
print("X(p): próximo p =", siguiente("p", tiempo, t_actual))
print("P(p): anteriormente p =", anteriormente("p", tiempo, t_actual))

# Evaluaciones para la proposición 'r'
print("\nF(r): eventualmente r =", eventualmente("r", tiempo, t_actual))
print("G(r): siempre r =", siempre("r", tiempo, t_actual))
print("X(r): próximo r =", siguiente("r", tiempo, t_actual))
print("P(r): anteriormente r =", anteriormente("r", tiempo, t_actual))
