"""
Prácticas de Inteligencia Artificial
Enfoque: Representar el Conocimiento
Subtema: Taxonomías – Categorías y Objetos

Este programa implementa una taxonomía básica usando estructuras de Python.
Una taxonomía es una jerarquía de categorías o clases que organizan objetos
por niveles de generalidad. Este modelo permite razonar sobre los objetos en función
de su posición en la jerarquía (herencia de propiedades, pertenencia, etc.).
"""

# ---------- DEFINICIÓN DE LA TAXONOMÍA ----------

# Diccionario de categorías: cada categoría tiene un nombre, un padre (supercategoría)
# y una lista de propiedades.
categorias = {
    "Entidad": {
        "padre": None,
        "propiedades": ["existe"]
    },
    "Objeto Físico": {
        "padre": "Entidad",
        "propiedades": ["ocupa espacio", "tiene masa"]
    },
    "Animal": {
        "padre": "Objeto Físico",
        "propiedades": ["vive", "se mueve"]
    },
    "Planta": {
        "padre": "Objeto Físico",
        "propiedades": ["vive", "fotosintetiza"]
    },
    "Mamífero": {
        "padre": "Animal",
        "propiedades": ["es de sangre caliente", "tiene pelo"]
    },
    "Ave": {
        "padre": "Animal",
        "propiedades": ["tiene plumas", "pone huevos"]
    },
    "Perro": {
        "padre": "Mamífero",
        "propiedades": ["ladra"]
    },
    "Gato": {
        "padre": "Mamífero",
        "propiedades": ["maúlla"]
    },
    "Pájaro": {
        "padre": "Ave",
        "propiedades": ["canta"]
    }
}

# Instancias (objetos) con su categoría asociada
objetos = {
    "firulais": "Perro",
    "garfield": "Gato",
    "piolin": "Pájaro",
    "roble": "Planta"
}

# ---------- FUNCIONES PARA CONSULTAR Y MOSTRAR ----------

def obtener_propiedades_heredadas(categoria):
    """Devuelve todas las propiedades de una categoría, incluyendo las heredadas"""
    propiedades = []
    actual = categoria
    while actual is not None:
        propiedades = categorias[actual]["propiedades"] + propiedades
        actual = categorias[actual]["padre"]
    return propiedades

def imprimir_taxonomia():
    """Imprime la jerarquía de la taxonomía"""
    print("\n📂 Jerarquía de Categorías:")
    def imprimir_subcategorias(cat, nivel=0):
        print("  " * nivel + f"📦 {cat}")
        for subcat in categorias:
            if categorias[subcat]["padre"] == cat:
                imprimir_subcategorias(subcat, nivel + 1)
    imprimir_subcategorias("Entidad")

def imprimir_objetos():
    """Imprime los objetos y sus propiedades heredadas"""
    print("\n📦 Objetos y sus propiedades:")
    for nombre, tipo in objetos.items():
        props = obtener_propiedades_heredadas(tipo)
        print(f" - {nombre} ({tipo}): {', '.join(props)}")

# ---------- EJECUCIÓN DEL SISTEMA ----------

print("=" * 60)
print("🔎 Taxonomía: Categorías y Objetos")
print("=" * 60)

imprimir_taxonomia()
imprimir_objetos()
