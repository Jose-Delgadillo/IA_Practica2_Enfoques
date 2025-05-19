"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógica No Monotónica

La lógica no monotónica permite razonar con conocimiento incompleto o cambiante.
A diferencia de la lógica clásica (monótona), donde agregar hechos nunca invalida
conclusiones previas, en la lógica no monotónica **una conclusión puede dejar de
ser válida** cuando se agrega nueva información.

Este programa ilustra un caso clásico con "predeterminaciones" que se invalidan
ante nueva evidencia (por ejemplo: "los pájaros normalmente vuelan").
"""

# Base de conocimiento inicial
base_conocimiento = {
    "tiene_ala": ["loro", "avestruz", "murciélago"],
    "es_pajaro": ["loro", "avestruz"],
    "es_mamifero": ["murciélago"],
}

# Conocimiento por defecto (regla no monotónica):
# "Si algo es un pájaro, entonces normalmente vuela, a menos que se indique lo contrario"
def vuela(animal, excepciones):
    if animal in base_conocimiento["es_pajaro"]:
        if animal not in excepciones:
            return True  # vuela por defecto
    if animal in base_conocimiento["es_mamifero"]:
        return True if animal == "murciélago" else False
    return False

# Lista de excepciones conocidas (dinámica)
excepciones = ["avestruz"]  # sabemos que el avestruz no vuela

# Evaluaciones
animales = ["loro", "avestruz", "murciélago"]

for animal in animales:
    print(f"¿{animal.capitalize()} vuela? {'Sí' if vuela(animal, excepciones) else 'No'}")

# Añadimos nueva información: el loro está herido, ahora es una excepción
print("\nSe descubre que el loro está herido. Agregando excepción...")
excepciones.append("loro")

print("\nReevaluando con la nueva información:")
for animal in animales:
    print(f"¿{animal.capitalize()} vuela? {'Sí' if vuela(animal, excepciones) else 'No'}")
