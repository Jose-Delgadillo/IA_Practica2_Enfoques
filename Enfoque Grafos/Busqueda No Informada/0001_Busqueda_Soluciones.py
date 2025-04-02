"""
Prácticas de Inteligencia artificial
Ejemplos de estructura de datos para busqueda en grafos.
"""
# %% Acción
class Accion:
    def __init_(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


# %% Estado
class Estado:
    def __innit__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

    def __str__(self):
        return self.nombre


# %% Problema
class Problema:
    def __init__(self, estado_inicial, estados_objetivos, acciones):
        self.estado_inicial = estado_inicial
        self.estados_objetivos = estados_objetivos
        self acciones = acciones

    def __str__(self):
        msg = "Estado Inicial: {0} -> Objetivos: {1}"
        return msg.format(self.estado_inicial.nombre,
                          self.estados_objetivos)
    def es_objetivo(self, estado):
        return estado in self.estados_objetivos
    
    def resultado(self, estado, accion):
        if estado.nombre not i self.acciones.keys():
            return None
        acciones_estado = self.acciones[estado.nombre]
        if accion.nombre not in acciones_estado.keys():
            return None
        return acciones_estado[accion.nombre]
    

# %% Definiciones
if __name__ == '__main__':
    accN = Accion('norte')