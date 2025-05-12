"""
Prácticas de Inteligencia Artificial
Propagación de Restricciones: Salto Atrás Dirigido por Conflictos
"""
class ConflictDirectedBacktracking:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones
        self.asignaciones = {}
        self.conflictos = []

    # Verifica si una asignación es consistente con las restricciones
    def es_consistente(self, var, valor):
        for (x, y), restriccion in self.restricciones.items():
            if x == var and y in self.asignaciones:
                if not restriccion(valor, self.asignaciones[y]):
                    return False
            elif y == var and x in self.asignaciones:
                if not restriccion(self.asignaciones[x], valor):
                    return False
        return True

    # Encuentra el siguiente valor a asignar
    def selecciona_variable(self):
        # Elige una variable no asignada
        for var in self.variables:
            if var not in self.asignaciones:
                return var
        return None

    # Realiza el salto atrás inteligente
    def salta_atras(self):
        if self.conflictos:
            variable_conflictiva, valor_conflictivo = self.conflictos.pop()
            print(f"Conflicto encontrado en la asignación de {variable_conflictiva} = {valor_conflictivo}")
            self.asignaciones.pop(variable_conflictiva, None)  # Eliminar la asignación conflictiva
            self.dominios[variable_conflictiva].remove(valor_conflictivo)  # Eliminar el valor conflictivo
            return True
        return False

    # Resolución del CSP con Salto Atrás Dirigido por Conflictos
    def resolver(self):
        if len(self.asignaciones) == len(self.variables):
            return self.asignaciones  # Se ha encontrado una solución
        
        # Selecciona la siguiente variable para asignar
        variable = self.selecciona_variable()

        if variable is None:
            return None  # No hay más variables por asignar

        # Recorre los valores posibles en el dominio de la variable
        for valor in self.dominios[variable]:
            if self.es_consistente(variable, valor):
                # Asigna el valor a la variable y realiza la asignación
                self.asignaciones[variable] = valor

                # Verifica el estado actual
                resultado = self.resolver()
                if resultado:
                    return resultado

                # Si ocurre un conflicto, realiza un salto atrás dirigido
                if not self.salta_atras():
                    continue  # Si no hay más conflictos, sigue con el siguiente valor

                # Si no se puede resolver con los valores actuales, vuelve a intentar con el siguiente valor
                self.asignaciones.pop(variable, None)
                self.conflictos.append((variable, valor))  # Guarda el conflicto para retroceder
                self.dominios[variable].remove(valor)
        return None

# ================== Definición del problema ==================

# Variables, dominios y restricciones
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

# ================== Ejecutar Salto Atrás Dirigido por Conflictos ==================

solver = ConflictDirectedBacktracking(variables, dominios, restricciones)
solucion = solver.resolver()

print("===== Resultado Final =====")
if solucion:
    for var, valor in solucion.items():
        print(f"{var} = {valor}")
else:
    print("No se pudo encontrar una solución")
