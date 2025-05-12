"""
Prácticas de Inteligencia Artificial
Satisfacción de Restricciones: Coloreado de Mapas
"""

def es_valido(asignacion, vecino, color):
    # Verifica que el color del vecino no sea igual
    return vecino not in asignacion or asignacion[vecino] != color

def backtracking(asignacion, variables, dominios, vecinos):
    # Si todas las variables están asignadas, devolver la solución
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionamos la siguiente variable no asignada
    var = next(v for v in variables if v not in asignacion)

    for color in dominios[var]:
        # Verificamos si el color es válido con todos los vecinos
        if all(es_valido(asignacion, vecino, color) for vecino in vecinos[var]):
            # Asignar y continuar recursivamente
            asignacion[var] = color
            resultado = backtracking(asignacion, variables, dominios, vecinos)
            if resultado:
                return resultado
            del asignacion[var]  # backtrack

    return None  # No se encontró solución

# Definimos el problema
variables = ['A', 'B', 'C', 'D']  # regiones
dominios = {var: ['Rojo', 'Verde', 'Azul'] for var in variables}

# Vecindad del mapa (por ejemplo, regiones conectadas)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Ejecutamos el backtracking
solucion = backtracking({}, variables, dominios, vecinos)

# Mostramos resultado
print("===== Problema CSP: Coloreado de Mapa =====")
if solucion:
    for region, color in solucion.items():
        print(f"{region} → {color}")
else:
    print("No se encontró solución")
