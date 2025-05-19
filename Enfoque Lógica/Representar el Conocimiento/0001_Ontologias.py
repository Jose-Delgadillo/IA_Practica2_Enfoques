"""
Prácticas de Inteligencia Artificial
Enfoque: Representar el Conocimiento
Subtema: Ingeniería del Conocimiento – Ontologías

Este programa simula una ontología simple utilizando estructuras básicas de Python.
Una ontología es una representación formal de un conjunto de conceptos y relaciones
en un dominio específico. Permite organizar y estructurar el conocimiento de forma jerárquica
y relacional.

Aquí representamos conceptos (clases), instancias (objetos) y relaciones entre ellos.
"""

# ---------- DEFINICIÓN DE LA ONTOLOGÍA ----------

# Clases del dominio
clases = {
    "Animal": {
        "subclases": ["Mamífero", "Ave"],
        "propiedades": ["respira", "se alimenta"]
    },
    "Mamífero": {
        "subclases": ["Humano", "Perro"],
        "propiedades": ["tiene pelo", "es de sangre caliente"]
    },
    "Ave": {
        "subclases": ["Pájaro"],
        "propiedades": ["tiene plumas", "pone huevos"]
    },
    "Humano": {
        "subclases": [],
        "propiedades": ["piensa", "usa herramientas"]
    },
    "Perro": {
        "subclases": [],
        "propiedades": ["ladra", "es fiel"]
    },
    "Pájaro": {
        "subclases": [],
        "propiedades": ["canta", "vuela"]
    }
}

# Instancias (individuos) y su tipo
instancias = {
    "juan": "Humano",
    "firulais": "Perro",
    "piolin": "Pájaro"
}

# Relaciones entre instancias (tripletas tipo RDF)
relaciones = [
    ("juan", "tiene mascota", "firulais"),
    ("piolin", "vive en", "jaula"),
    ("firulais", "es amigo de", "juan")
]

# ---------- FUNCIONES PARA INTERACTUAR CON LA ONTOLOGÍA ----------

def imprimir_clase(clase):
    print(f"\n📘 Clase: {clase}")
    print(f" - Subclases: {clases[clase]['subclases']}")
    print(f" - Propiedades: {clases[clase]['propiedades']}")

def imprimir_jerarquia(clase, nivel=0):
    print("  " * nivel + f"📦 {clase}")
    for sub in clases[clase]["subclases"]:
        imprimir_jerarquia(sub, nivel + 1)

def imprimir_instancias():
    print("\n📙 Instancias (individuos):")
    for nombre, tipo in instancias.items():
        print(f" - {nombre} es un {tipo}")

def imprimir_relaciones():
    print("\n🔗 Relaciones:")
    for sujeto, predicado, objeto in relaciones:
        print(f" - {sujeto} {predicado} {objeto}")

# ---------- EJECUCIÓN DEL SISTEMA ----------

print("=" * 60)
print("🔎 Ontología: Dominio de Animales")
print("=" * 60)

print("\n📂 Jerarquía de clases:")
imprimir_jerarquia("Animal")

imprimir_clase("Mamífero")
imprimir_clase("Ave")

imprimir_instancias()
imprimir_relaciones()
