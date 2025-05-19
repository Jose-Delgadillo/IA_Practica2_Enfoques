"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógicas de Orden Superior

Las lógicas de orden superior extienden la lógica de primer orden permitiendo cuantificar no solo
sobre individuos, sino también sobre predicados y funciones. Esto permite una mayor expresividad,
aunque con un costo en la complejidad del razonamiento.

Este programa simula un pequeño sistema de inferencia con lógica de segundo orden, en donde
cuantificamos sobre predicados. Dado un conjunto de datos y una propiedad general, el sistema
verifica si una propiedad se cumple para todos los elementos del dominio.
"""

# Simulación simple de lógica de segundo orden en Python

# Dominio de ejemplo: números enteros del 1 al 5
dominio = [1, 2, 3, 4, 5]

# Predicados de ejemplo (funciones booleanas)
def es_par(x):
    return x % 2 == 0

def es_menor_que_10(x):
    return x < 10

# Lógica de segundo orden: cuantificación sobre predicados
def para_todo_predicado(propiedad, predicado, dominio):
    """
    Verifica si la propiedad se cumple para todos los elementos donde el predicado es verdadero.
    """
    for x in dominio:
        if predicado(x) and not propiedad(x):
            return False
    return True

def existe_predicado(propiedad, lista_de_predicados, dominio):
    """
    Verifica si existe un predicado en la lista que haga que la propiedad se cumpla para algún elemento.
    """
    for p in lista_de_predicados:
        for x in dominio:
            if p(x) and propiedad(x):
                return True
    return False

# -------------------------
# Ejemplo de uso
# -------------------------

print("Dominio:", dominio)

# Verificar si todos los números pares son menores que 10
print("\n¿Todos los números pares son menores que 10?")
resultado1 = para_todo_predicado(es_menor_que_10, es_par, dominio)
print("Resultado:", resultado1)

# Verificar si existe un predicado que implique la propiedad de ser menor que 10
print("\n¿Existe algún predicado que implique ser menor que 10?")
resultado2 = existe_predicado(es_menor_que_10, [es_par], dominio)
print("Resultado:", resultado2)
