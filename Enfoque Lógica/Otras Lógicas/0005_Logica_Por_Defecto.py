"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógica por Defecto

La lógica por defecto permite razonar en ausencia de información completa,
haciendo suposiciones que pueden ser retractadas si aparece evidencia contraria.

Este ejemplo ilustra una regla por defecto: 
   "Los pájaros generalmente vuelan, a menos que se sepa lo contrario".

Implementamos un mecanismo simple que permite razonar bajo suposiciones por defecto
y luego modificar las conclusiones si se obtiene nueva información que invalida esas suposiciones.
"""

# Base de conocimiento explícito
hechos = {
    "es_pajaro": ["loro", "avestruz", "pingüino"],
    "no_vuela": ["avestruz", "pingüino"]  # excepciones explícitas
}

# Regla por defecto: "Si algo es un pájaro, se asume que vuela, salvo prueba en contra"
def por_defecto_vuela(animal):
    if animal in hechos["es_pajaro"]:
        if animal in hechos["no_vuela"]:
            return False  # hay prueba en contra
        else:
            return True   # se aplica la suposición por defecto
    return False  # no se considera pájaro

# Evaluación inicial
animales = ["loro", "avestruz", "pingüino", "perro"]

print("Razonamiento inicial con lógica por defecto:\n")
for animal in animales:
    resultado = por_defecto_vuela(animal)
    print(f"¿{animal.capitalize()} vuela por defecto? {'Sí' if resultado else 'No'}")

# Ahora llega nueva información: el loro tiene el ala rota
print("\nNueva información: el loro tiene un ala rota. Se agrega a la lista de 'no_vuela'.\n")
hechos["no_vuela"].append("loro")

# Reevaluación con nueva información
print("Reevaluación con nueva información:")
for animal in animales:
    resultado = por_defecto_vuela(animal)
    print(f"¿{animal.capitalize()} vuela por defecto? {'Sí' if resultado else 'No'}")
