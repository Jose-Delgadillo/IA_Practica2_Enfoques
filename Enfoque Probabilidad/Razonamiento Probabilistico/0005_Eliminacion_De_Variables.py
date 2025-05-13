"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Eliminación de Variables

Este programa implementa la técnica de Eliminación de Variables (Variable Elimination),
una forma eficiente de realizar inferencia en redes bayesianas al eliminar variables ocultas
no relevantes para la consulta, usando factores para reducir el cómputo.
"""

from collections import defaultdict
from itertools import product

# Definición de la Red Bayesiana como una lista de factores
# Cada factor es un diccionario con claves de tuplas de valores de variables y una probabilidad

# Ejemplo: Red simple con 3 variables A, B, C
# A es raíz, B depende de A, C depende de A y B
factores = {
    'P(A)': {
        (True,): 0.2,
        (False,): 0.8
    },
    'P(B|A)': {
        (True, True): 0.75,
        (True, False): 0.25,
        (False, True): 0.1,
        (False, False): 0.9
    },
    'P(C|A,B)': {
        (True, True, True): 0.95,
        (True, True, False): 0.05,
        (True, False, True): 0.8,
        (True, False, False): 0.2,
        (False, True, True): 0.6,
        (False, True, False): 0.4,
        (False, False, True): 0.1,
        (False, False, False): 0.9
    }
}

# Lista de variables de cada factor (en el mismo orden que en las tuplas del factor)
estructura_factores = {
    'P(A)': ['A'],
    'P(B|A)': ['A', 'B'],
    'P(C|A,B)': ['A', 'B', 'C']
}

# Función para restringir un factor dado con una variable y su valor
def restringir(factor, var, val, estructura):
    nueva_tabla = {}
    idx = estructura.index(var)
    for tupla, prob in factor.items():
        if tupla[idx] == val:
            nueva_tupla = tupla[:idx] + tupla[idx+1:]
            nueva_tabla[nueva_tupla] = prob
    nueva_estructura = estructura[:]
    nueva_estructura.remove(var)
    return nueva_tabla, nueva_estructura

# Función para multiplicar dos factores
def multiplicar(f1, e1, f2, e2):
    variables = list(dict.fromkeys(e1 + e2))  # Evita duplicados
    nueva_tabla = {}

    for vals in product([True, False], repeat=len(variables)):
        asignacion = dict(zip(variables, vals))
        # Obtener valores para f1 y f2
        t1 = tuple(asignacion[v] for v in e1)
        t2 = tuple(asignacion[v] for v in e2)
        if t1 in f1 and t2 in f2:
            nueva_tabla[tuple(asignacion[v] for v in variables)] = f1[t1] * f2[t2]

    return nueva_tabla, variables

# Función para eliminar una variable sumando sobre ella
def eliminar_variable(factor, estructura, var):
    idx = estructura.index(var)
    nueva_tabla = defaultdict(float)
    for vals, prob in factor.items():
        nueva_tupla = vals[:idx] + vals[idx+1:]
        nueva_tabla[nueva_tupla] += prob
    nueva_estructura = estructura[:]
    nueva_estructura.remove(var)
    return dict(nueva_tabla), nueva_estructura

# Algoritmo de eliminación de variables
def eliminacion_de_variables(consulta, evidencia):
    # Copiamos los factores para no modificar los originales
    factores_activos = list(factores.items())
    estructuras = estructura_factores.copy()

    # Paso 1: Aplicar evidencia
    for var, val in evidencia.items():
        nuevos_factores = []
        for nombre, tabla in factores_activos:
            if var in estructuras[nombre]:
                tabla, estructuras[nombre] = restringir(tabla, var, val, estructuras[nombre])
            nuevos_factores.append((nombre, tabla))
        factores_activos = nuevos_factores

    # Paso 2: Eliminar variables ocultas (no en consulta ni evidencia)
    vars_consulta = set(consulta + list(evidencia.keys()))
    todas_vars = set(v for es in estructuras.values() for v in es)
    ocultas = list(todas_vars - vars_consulta)

    for var in ocultas:
        # Seleccionar factores donde aparece la variable
        relacionados = [(n, f) for n, f in factores_activos if var in estructuras[n]]
        if not relacionados:
            continue

        # Multiplicar todos los factores relacionados
        nombre, tabla = relacionados[0]
        estructura = estructuras[nombre]
        for n2, f2 in relacionados[1:]:
            tabla, estructura = multiplicar(tabla, estructura, f2, estructuras[n2])

        # Eliminar la variable
        tabla, estructura = eliminar_variable(tabla, estructura, var)

        # Actualizar la lista de factores
        for n, _ in relacionados:
            factores_activos = [(x, y) for x, y in factores_activos if x != n]
            del estructuras[n]
        nuevo_nombre = f'F_{var}'
        factores_activos.append((nuevo_nombre, tabla))
        estructuras[nuevo_nombre] = estructura

    # Paso 3: Multiplicar los factores restantes
    nombre, tabla = factores_activos[0]
    estructura = estructuras[nombre]
    for n, f in factores_activos[1:]:
        tabla, estructura = multiplicar(tabla, estructura, f, estructuras[n])

    # Paso 4: Normalizar para obtener distribución final
    total = sum(tabla.values())
    distribucion = {k: v / total for k, v in tabla.items()}
    return distribucion

# === Prueba ===
consulta = ['C']
evidencia = {'B': True}

resultado = eliminacion_de_variables(consulta, evidencia)
print("\n===== Resultado de Eliminación de Variables =====")
for valores, prob in resultado.items():
    print(f"{consulta} = {valores} -> {prob:.4f}")
