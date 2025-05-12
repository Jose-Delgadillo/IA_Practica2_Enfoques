"""
Prácticas de Inteligencia Artificial
Comprobación Hacia Delante (Forward Checking)
"""

import copy

# Verifica si un valor asignado es válido respecto a las restricciones
def es_valido(variable, valor, asignacion, restricciones):
    for otra_variable in asignacion:
        if (variable, otra_variable) in restricciones:
            if not restricciones[(variable, otra_variable)](valor, asignacion[otra_variable]):
                return False
        elif (otra_variable, variable) in restricciones:
            if not restricciones[(otra_variable, variable)](asignacion[otra_variable], valor):
                return False
    return True

# Función principal con comprobación hacia adelante
def forward_checking(asignacion, variables, dominios, restricciones):
    if len(asignacion) == len(variables):
        return asignacion

    # Escoge la siguiente variable no asignada
    var = next(v for v in variables if v not in asignacion)

    for valor in dominios[var]:
        if es_valido(var, valor, asignacion, restricciones):
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[var] = valor

            # Copia profunda de dominios para modificar sin afectar ramas anteriores
            nuevos_dominios = copy.deepcopy(dominios)
            nuevos_dominios[var] = [valor]

            # Comprobación hacia adelante: eliminamos valores inconsistentes
            falló = False
            for otra_var in variables:
                if otra_var not in nueva_asignacion:
                    valores_validos = []
                    for val in nuevos_dominios[otra_var]:
                        if es_valido(otra_var, val, nueva_asignacion, restricciones):
                            valores_validos.append(val)
                    if not valores_validos:
                        falló = True  # sin valores válidos, hacer backtrack
                        break
                    nuevos_dominios[otra_var] = valores_validos

            if not falló:
                resultado = forward_checking(nueva_asignacion, variables, nuevos_dominios, restricciones)
                if resultado:
                    return resultado

    return None  # No se encontró solución

# ================== Definición del problema ==================

variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Restricciones: todas las variables deben ser diferentes
restricciones = {
    ('A', 'B'): lambda a, b: a != b,
    ('B', 'C'): lambda b, c: b != c,
    ('A', 'C'): lambda a, c: a != c
}

# ================== Ejecutar ==================
solucion = forward_checking({}, variables, dominios, restricciones)

print("===== Comprobación Hacia Delante (Forward Checking) =====")
if solucion:
    for var, val in solucion.items():
        print(f"{var} → {val}")
else:
    print("No se encontró solución")
