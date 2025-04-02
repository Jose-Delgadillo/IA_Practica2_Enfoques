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
        self