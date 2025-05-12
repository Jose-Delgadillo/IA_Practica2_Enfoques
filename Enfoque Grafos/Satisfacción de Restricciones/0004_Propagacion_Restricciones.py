"""
Prácticas de Inteligencia Artificial
Propagación de Restricciones: Algoritmo AC-3 
"""

from collections import deque

# Revisa si un arco (X, Y) es consistente y modifica el dominio si es necesario
def revisar(arco, dominios, restricciones):
    x, y = arco
    revisado = False
    for val_x in dominios[x][:]:
        # Si no hay ningún valor en y que satisfaga la restricción, se elimina val_x
        if not any(restricciones[(x, y)](val_x, val_y) for val_y in dominios[y]):
            dominios[x].remove(val_x)
            revisado = True
    return revisado

# Algoritmo AC-3
def ac3(variables, dominios, restricciones):
    cola = deque(restricciones.keys())

    while cola:
        arco = cola.popleft()
        if revisar(arco, dominios, restricciones):
            if not dominios[arco[0]]:
                return False  # Dominio vacío → inconsistencia
            # Se vuelven a añadir arcos relacionados con la variable modificada
            for vecino in variables:
                if vecino != arco[0] and (vecino, arco[0]) in restricciones:
                    cola.append((vecino, arco[0]))
    return True

# ================== Definición del problema ==================

variables = ['X', 'Y', 'Z']
dominios = {
    'X': [1, 2, 3],
    'Y': [1, 2, 3],
    'Z': [1, 2, 3]
}

# Restricciones: variables deben ser diferentes
restricciones = {
    ('X', 'Y'): lambda x, y: x != y,
    ('Y', 'X'): lambda y, x: y != x,
    ('Y', 'Z'): lambda y, z: y != z,
    ('Z', 'Y'): lambda z, y: z != y,
    ('X', 'Z'): lambda x, z: x != z,
    ('Z', 'X'): lambda z, x: z != x
}

# ================== Ejecutar AC-3 ==================

exito = ac3(variables, dominios, restricciones)

print("===== Propagación de Restricciones (AC-3) =====")
if exito:
    for var in variables:
        print(f"{var} → dominio reducido: {dominios[var]}")
else:
    print("No hay solución posible (dominio vacío)")
