"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Inferencia por Enumeración

La inferencia por enumeración consiste en calcular la probabilidad de una variable de consulta 
dada alguna evidencia, usando la ley de la probabilidad total para recorrer todos los estados posibles.

Este ejemplo utiliza una red bayesiana del tipo:
- Robo y Terremoto influyen en Alarma
- Alarma influye en JuanLlama y MariaLlama
"""

from itertools import product

# Definición de la Red Bayesiana mediante Tablas de Probabilidad (P)

P = {
    'Robo': {True: 0.001, False: 0.999},
    'Terremoto': {True: 0.002, False: 0.998},
    'Alarma': {
        (True, True): {True: 0.95, False: 0.05},
        (True, False): {True: 0.94, False: 0.06},
        (False, True): {True: 0.29, False: 0.71},
        (False, False): {True: 0.001, False: 0.999}
    },
    'JuanLlama': {
        True: {True: 0.90, False: 0.10},
        False: {True: 0.05, False: 0.95}
    },
    'MariaLlama': {
        True: {True: 0.70, False: 0.30},
        False: {True: 0.01, False: 0.99}
    }
}

# Lista de padres para cada nodo
padres = {
    'Robo': [],
    'Terremoto': [],
    'Alarma': ['Robo', 'Terremoto'],
    'JuanLlama': ['Alarma'],
    'MariaLlama': ['Alarma']
}

# Función para obtener la probabilidad condicional o marginal
def probabilidad(variable, valor, asignacion):
    if padres[variable] == []:
        return P[variable][valor]
    else:
        valores_padres = tuple(asignacion[p] for p in padres[variable])
        return P[variable][valores_padres][valor]

# Enumeración recursiva
def enumerar_todas(variables, asignacion):
    if not variables:
        return 1.0
    Y = variables[0]
    resto = variables[1:]
    if Y in asignacion:
        prob = probabilidad(Y, asignacion[Y], asignacion)
        return prob * enumerar_todas(resto, asignacion)
    else:
        total = 0
        for y in [True, False]:
            asignacion[Y] = y
            prob = probabilidad(Y, y, asignacion)
            total += prob * enumerar_todas(resto, asignacion)
            del asignacion[Y]
        return total

# Inference by enumeration: P(X | e)
def inferencia_por_enumeracion(variable_consulta, evidencia):
    resultado = {}
    for valor in [True, False]:
        evidencia[variable_consulta] = valor
        prob = enumerar_todas(list(P.keys()), evidencia.copy())
        resultado[valor] = prob
        del evidencia[variable_consulta]
    
    # Normalización
    total = sum(resultado.values())
    for val in resultado:
        resultado[val] /= total
    return resultado

# Ejemplo: P(Robo | JuanLlama=True, MariaLlama=True)
evidencia = {'JuanLlama': True, 'MariaLlama': True}
consulta = 'Robo'

resultado = inferencia_por_enumeracion(consulta, evidencia)

# Mostrar resultados
print("======= Inferencia por Enumeración =======")
print(f"Consulta: P({consulta} | {evidencia})")
for val in resultado:
    print(f"P({consulta}={val}) = {resultado[val]:.5f}")
