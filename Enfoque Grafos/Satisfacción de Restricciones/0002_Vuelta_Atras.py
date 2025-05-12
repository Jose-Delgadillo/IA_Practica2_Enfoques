"""
Prácticas de Inteligencia Artificial
Búsqueda de Vuelta Atrás (Backtracking)
Ejemplo simple de CSP: Asignación con restricciones
"""

# Verifica si una asignación actual es válida según las restricciones
def es_valido(variable, valor, asignacion, restricciones):
    for otra_variable in asignacion:
        # Si existe una restricción entre estas dos variables
        if (variable, otra_variable) in restricciones:
            if not restricciones[(variable, otra_variable)](valor, asignacion[otra_variable]):
                return False
        elif (otra_variable, variable) in restricciones:
            if not restricciones[(otra_variable, variable)](asignacion[otra_variable], valor):
                return False
    return True

# Algoritmo de backtracking genérico
def backtracking(asignacion, variables, dominios, restricciones):
    # Si todas las variables están asignadas, se encontró solución
    if len(asignacion) == len(variables):
        return asignacion

    # Elegimos la siguiente variable no asignada
    var = next(v for v in variables if v not in asignacion)

    # Probamos cada valor del dominio de esa variable
    for valor in dominios[var]:
        if es_valido(var, valor, asignacion, restricciones):
            asignacion[var] = valor
            resultado = backtracking(asignacion, variables, dominios, restricciones)
            if resultado:
                return resultado
            del asignacion[var]  # backtrack: eliminamos la asignación

    return None  # No se encontró solución

# ================== Definición del problema ==================

variables = ['X', 'Y', 'Z']
dominios = {
    'X': [1, 2, 3],
    'Y': [1, 2, 3],
    'Z': [1, 2, 3]
}

# Restricciones como funciones lambda
restricciones = {
    ('X', 'Y'): lambda x, y: x != y,
    ('Y', 'Z'): lambda y, z: y < z,
    ('X', 'Z'): lambda x, z: x != z
}

# ================== Ejecutar ==================
solucion = backtracking({}, variables, dominios, restricciones)

print("===== Búsqueda de Vuelta Atrás (Backtracking) =====")
if solucion:
    for var, val in solucion.items():
        print(f"{var} → {val}")
else:
    print("No se encontró solución")
