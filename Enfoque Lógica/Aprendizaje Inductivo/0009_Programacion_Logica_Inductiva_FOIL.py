"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Programación Lógica Inductiva - FOIL

Este código implementa una versión simplificada del algoritmo FOIL (First Order
Inductive Learner), que es un método de aprendizaje inductivo para aprender reglas
lógicas de primer orden a partir de ejemplos positivos y negativos.

FOIL genera reglas lógicas en forma de cláusulas de Horn, construyendo condiciones
de predicado que cubren los ejemplos positivos mientras excluyen los negativos.

Este ejemplo utiliza Python puro, sin librerías externas, y está diseñado para 
ilustrar los conceptos básicos del aprendizaje inductivo en lógica de primer orden.
"""

# Representamos hechos y ejemplos con estructuras simples de tuplas y listas
# Variables en las reglas se representarán como strings que empiezan con mayúscula

# Ejemplos positivos: hechos que queremos cubrir con la regla
positivos = [
    ('padre', 'juan', 'carlos'),
    ('padre', 'juan', 'ana'),
    ('padre', 'pedro', 'maria')
]

# Ejemplos negativos: hechos que la regla no debe cubrir
negativos = [
    ('padre', 'ana', 'juan'),
    ('padre', 'carlos', 'juan'),
    ('padre', 'maria', 'pedro')
]

# Predicados base para construir reglas (en un sistema real vendrían del dominio)
predicados = [
    ('padre', 'X', 'Y'),
    ('madre', 'X', 'Y'),
    ('hermano', 'X', 'Y'),
    ('tio', 'X', 'Y')
]

# Variables usadas para construir reglas
variables = ['X', 'Y', 'Z']

def es_variable(token):
    """Determina si un token es variable (empieza con mayúscula)."""
    return isinstance(token, str) and token[0].isupper()

def sustituir(term, sustituciones):
    """
    Aplica las sustituciones a un término:
    Si es variable y está en sustituciones, devuelve la sustitución.
    Si es constante o variable no sustituida, devuelve el término original.
    """
    if es_variable(term):
        return sustituciones.get(term, term)
    return term

def unificar(hecho, regla, sustituciones):
    """
    Intenta unificar un hecho con una regla bajo las sustituciones actuales.
    Si se puede, devuelve las nuevas sustituciones; sino None.
    """
    if hecho[0] != regla[0] or len(hecho) != len(regla):
        return None

    nuevas_subs = dict(sustituciones)
    for h, r in zip(hecho[1:], regla[1:]):
        h_val = h
        r_val = r
        if es_variable(r_val):
            if r_val in nuevas_subs:
                # Si variable ya sustituida, verificar igualdad
                if nuevas_subs[r_val] != h_val:
                    return None
            else:
                nuevas_subs[r_val] = h_val
        else:
            if h_val != r_val:
                return None
    return nuevas_subs

def cubrir(hechos, regla):
    """
    Verifica cuántos hechos de la lista son cubiertos por la regla.
    """
    cubiertos = 0
    for hecho in hechos:
        if unificar(hecho, regla, {}):
            cubiertos += 1
    return cubiertos

def generar_reglas(base_predicados, variables):
    """
    Genera reglas candidatas combinando predicados y variables.
    Para simplicidad, sólo generamos reglas de la forma predicado(X,Y).
    """
    reglas = []
    for pred in base_predicados:
        for v1 in variables:
            for v2 in variables:
                regla = (pred[0], v1, v2)
                reglas.append(regla)
    return reglas

def seleccionar_mejor_regla(positivos, negativos, base_predicados, variables):
    """
    Selecciona la regla que cubre más positivos y menos negativos.
    Métrica simple: (positivos cubiertos - negativos cubiertos).
    """
    reglas = generar_reglas(base_predicados, variables)
    mejor_regla = None
    mejor_puntaje = -float('inf')

    for regla in reglas:
        pos_cubiertos = cubrir(positivos, regla)
        neg_cubiertos = cubrir(negativos, regla)
        puntaje = pos_cubiertos - neg_cubiertos
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_regla = regla

    return mejor_regla, mejor_puntaje

def main():
    regla, puntaje = seleccionar_mejor_regla(positivos, negativos, predicados, variables)
    if regla:
        print(f"Mejor regla encontrada: {regla} con puntaje {puntaje}")
    else:
        print("No se encontró una regla adecuada.")

if __name__ == "__main__":
    main()
