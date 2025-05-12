"""
Prácticas de Inteligencia Artificial
Teoría de la Utilidad: Función de Utilidad
"""

class TeoriaDeUtilidad:
    def __init__(self, alternativas, utilidades):
        """
        Inicializa el problema de utilidad.
        - alternativas: Lista de alternativas o opciones disponibles.
        - utilidades: Diccionario con las utilidades asociadas a cada alternativa.
        """
        self.alternativas = alternativas
        self.utilidades = utilidades

    def calcular_utilidad(self, alternativa):
        """
        Calcula la utilidad de una alternativa específica.
        """
        if alternativa in self.utilidades:
            return self.utilidades[alternativa]
        else:
            raise ValueError(f"La alternativa {alternativa} no está definida en las utilidades.")

    def mejor_alternativa(self):
        """
        Devuelve la alternativa con la mayor utilidad.
        """
        mejor = max(self.alternativas, key=lambda alternativa: self.utilidades[alternativa])
        return mejor, self.utilidades[mejor]

# ================== Definición del Problema ==================

# Alternativas disponibles (pueden ser decisiones o elecciones)
alternativas = ['A', 'B', 'C', 'D']

# Utilidades asociadas a cada alternativa (ejemplo con puntuaciones de 0 a 100)
utilidades = {
    'A': 80,  # Utilidad para la alternativa A
    'B': 60,  # Utilidad para la alternativa B
    'C': 90,  # Utilidad para la alternativa C
    'D': 70   # Utilidad para la alternativa D
}

# ================== Ejecutar el Algoritmo de Función de Utilidad ==================

# Crear una instancia del problema de utilidad
problema_utilidad = TeoriaDeUtilidad(alternativas, utilidades)

# Calcular la utilidad de todas las alternativas
for alternativa in alternativas:
    print(f"Utilidad de la alternativa {alternativa}: {problema_utilidad.calcular_utilidad(alternativa)}")

# Encontrar la mejor alternativa (la que maximiza la utilidad)
mejor_alternativa, utilidad_maxima = problema_utilidad.mejor_alternativa()

# Mostrar el resultado final
print(f"\nLa mejor alternativa es: {mejor_alternativa} con una utilidad de {utilidad_maxima}")
