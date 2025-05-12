"""
Prácticas de Inteligencia Artificial
Búsqueda Local con Acondicionamiento del Corte (Poda)
"""

import random

class CorteCondicionamiento:
    def __init__(self, variables, dominios, restricciones, max_iter=100):
        """
        Inicializa el algoritmo de Búsqueda Local con Acondicionamiento del Corte.
        - variables: Lista de las variables del problema.
        - dominios: Diccionario con los dominios de cada variable (posibles valores).
        - restricciones: Diccionario con las restricciones entre variables.
        - max_iter: Número máximo de iteraciones para la búsqueda local.
        """
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones
        self.max_iter = max_iter
        self.asignacion = {var: random.choice(dominio) for var, dominio in dominios.items()}  # Asignación aleatoria

    def es_consistente(self, variable, valor):
        """
        Verifica si la asignación de un valor a una variable no viola ninguna restricción.
        """
        for otra_variable, otro_valor in self.asignacion.items():
            if (variable, otra_variable) in self.restricciones:
                if not self.restricciones[(variable, otra_variable)](valor, otro_valor):
                    return False
            if (otra_variable, variable) in self.restricciones:
                if not self.restricciones[(otra_variable, variable)](otro_valor, valor):
                    return False
        return True

    def contar_conflictos(self, variable, valor):
        """
        Cuenta cuántos conflictos tendría una asignación dada a una variable.
        """
        conflictos = 0
        for otra_variable, otro_valor in self.asignacion.items():
            if (variable, otra_variable) in self.restricciones:
                if not self.restricciones[(variable, otra_variable)](valor, otro_valor):
                    conflictos += 1
            if (otra_variable, variable) in self.restricciones:
                if not self.restricciones[(otra_variable, variable)](otro_valor, valor):
                    conflictos += 1
        return conflictos

    def resolver(self):
        """
        Resuelve el CSP utilizando el algoritmo de búsqueda local con acondicionamiento del corte (poda).
        """
        for _ in range(self.max_iter):
            # Verificamos si ya hemos encontrado una solución válida
            if self.satisface_restricciones():
                return self.asignacion

            # Seleccionamos una variable que tiene conflictos
            variable_conflictiva = self.seleccionar_variable_conflictiva()

            # Si no hay más conflictos, significa que hemos encontrado la solución
            if variable_conflictiva is None:
                continue

            # Buscamos el valor que minimiza los conflictos
            valor_min_conflictos = self.minimizar_conflictos(variable_conflictiva)

            # Asignamos el valor a la variable
            self.asignacion[variable_conflictiva] = valor_min_conflictos

            # Realizamos un acondicionamiento (corte) si la solución ya es insostenible
            if self.poda_corte(variable_conflictiva):
                break

        return None  # No se encontró solución dentro del número máximo de iteraciones

    def seleccionar_variable_conflictiva(self):
        """
        Selecciona la variable con el mayor número de conflictos.
        """
        variable_conflictiva = None
        max_conflictos = 0

        # Buscamos la variable con el mayor número de conflictos
        for variable in self.variables:
            if variable not in self.asignacion:
                conflictos = sum(1 for otra_variable in self.variables if (variable, otra_variable) in self.restricciones)
                if conflictos > max_conflictos:
                    max_conflictos = conflictos
                    variable_conflictiva = variable

        return variable_conflictiva

    def minimizar_conflictos(self, variable):
        """
        Asigna el valor a la variable que minimiza los conflictos.
        """
        min_conflictos = float('inf')
        valor_min_conflictos = None

        # Probamos todos los valores en el dominio de la variable
        for valor in self.dominios[variable]:
            conflictos = self.contar_conflictos(variable, valor)
            if conflictos < min_conflictos:
                min_conflictos = conflictos
                valor_min_conflictos = valor

        return valor_min_conflictos

    def satisface_restricciones(self):
        """
        Verifica si la asignación actual satisface todas las restricciones.
        """
        for (var1, var2), restr in self.restricciones.items():
            if not restr(self.asignacion.get(var1), self.asignacion.get(var2)):
                return False
        return True

    def poda_corte(self, variable):
        """
        Realiza una poda de corte si encontramos que el problema ya no tiene solución.
        Este corte interrumpe la búsqueda si se llega a una asignación insostenible.
        """
        # Si alguna variable ya ha sido asignada a un valor insostenible, cortamos la búsqueda
        for var in self.variables:
            if var not in self.asignacion:
                if not self.es_consistente(var, random.choice(self.dominios[var])):
                    print(f"Se ha producido un corte en la búsqueda debido a que la variable {var} no puede ser consistente.")
                    return True
        return False


# ================== Definición del Problema ==================

# Variables del CSP
variables = ['X', 'Y', 'Z']

# Dominios de cada variable
dominios = {
    'X': ['rojo', 'azul', 'verde'],
    'Y': ['rojo', 'azul', 'verde'],
    'Z': ['rojo', 'azul', 'verde']
}

# Restricciones: las variables deben tener diferentes valores (es decir, no pueden tener el mismo color)
restricciones = {
    ('X', 'Y'): lambda x, y: x != y,
    ('Y', 'X'): lambda y, x: y != x,
    ('Y', 'Z'): lambda y, z: y != z,
    ('Z', 'Y'): lambda z, y: z != y,
    ('X', 'Z'): lambda x, z: x != z,
    ('Z', 'X'): lambda z, x: z != x
}

# ================== Ejecutar el Algoritmo de Acondicionamiento de Corte ==================

corte_solver = CorteCondicionamiento(variables, dominios, restricciones)
solucion = corte_solver.resolver()  # Aplicamos el algoritmo con acondicionamiento del corte.

# ================== Mostrar el Resultado ==================

print("===== Resultado Final =====")
if solucion:
    for var, valor in solucion.items():
        print(f"{var} tiene el valor: {valor}")
else:
    print("No se encontró una solución.")
