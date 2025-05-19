"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógica Modal

La lógica modal extiende la lógica proposicional clásica al introducir operadores modales, como:
- ◇ (posible): "es posible que P"
- □ (necesario): "es necesario que P"

Estos operadores se interpretan a través de mundos posibles conectados mediante una relación de accesibilidad.
En este ejemplo, simulamos un modelo de lógica modal donde los mundos están conectados, y evaluamos
si una proposición es posible o necesaria a partir de un mundo dado.
"""

# Definimos un conjunto de mundos posibles con sus proposiciones verdaderas
mundos = {
    "w1": {"p", "q"},
    "w2": {"q"},
    "w3": {"p"},
}

# Relación de accesibilidad entre mundos
accesibilidad = {
    "w1": ["w2", "w3"],
    "w2": ["w2"],
    "w3": ["w3"],
}

def posible(prop, mundo_actual):
    """
    Operador ◇ (posibilidad): 
    Devuelve True si prop es verdadera en al menos un mundo accesible.
    """
    for w in accesibilidad[mundo_actual]:
        if prop in mundos[w]:
            return True
    return False

def necesario(prop, mundo_actual):
    """
    Operador □ (necesidad): 
    Devuelve True si prop es verdadera en todos los mundos accesibles.
    """
    for w in accesibilidad[mundo_actual]:
        if prop not in mundos[w]:
            return False
    return True

# ----------------------------
# Ejemplos de evaluación modal
# ----------------------------

mundo = "w1"
print(f"Mundo actual: {mundo}")
print("Mundos accesibles:", accesibilidad[mundo])
print()

# Evaluamos posibilidad y necesidad de "p"
print("◇p (¿es posible p?) =", posible("p", mundo))
print("□p (¿es necesario p?) =", necesario("p", mundo))

# Evaluamos posibilidad y necesidad de "q"
print("\n◇q (¿es posible q?) =", posible("q", mundo))
print("□q (¿es necesario q?) =", necesario("q", mundo))

# Evaluamos necesidad de una proposición falsa en un mundo accesible
print("\n□r (¿es necesario r?) =", necesario("r", mundo))
