"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Explicaciones e Información Relevante

Este código implementa métodos para generar explicaciones simples a partir de datos 
y modelos inductivos, así como para extraer información relevante que permita 
entender las decisiones o clasificaciones realizadas por un sistema de aprendizaje.

Se enfoca en interpretar el conocimiento aprendido y presentar reglas o patrones 
que faciliten la comprensión humana.

El código está escrito en Python puro, sin dependencias externas, para facilitar 
su ejecución y análisis didáctico.
"""

# Ejemplo sencillo de generación de explicaciones para un clasificador de reglas

# Datos de ejemplo: cada entrada es (atributos, clase)
datos = [
    ({"color": "rojo", "forma": "redondo", "tamaño": "grande"}, "manzana"),
    ({"color": "amarillo", "forma": "alargado", "tamaño": "grande"}, "banana"),
    ({"color": "verde", "forma": "redondo", "tamaño": "pequeño"}, "limón"),
    ({"color": "rojo", "forma": "alargado", "tamaño": "pequeño"}, "chile"),
    ({"color": "amarillo", "forma": "redondo", "tamaño": "pequeño"}, "limón"),
]

# Paso 1: Extraer reglas simples que relacionen atributos con clases
# Contar ocurrencias para cada atributo-valor asociado a una clase
def contar_atributos_clase(datos):
    conteos = {}
    for entrada, clase in datos:
        for atributo, valor in entrada.items():
            key = (atributo, valor, clase)
            conteos[key] = conteos.get(key, 0) + 1
    return conteos

# Paso 2: Generar reglas simples: "Si atributo=valor entonces clase=clase"
def generar_reglas(conteos, umbral=1):
    reglas = []
    for (atributo, valor, clase), cuenta in conteos.items():
        if cuenta >= umbral:
            reglas.append((atributo, valor, clase, cuenta))
    return reglas

# Paso 3: Explicar clasificación para un nuevo ejemplo mostrando reglas aplicadas
def explicar_clasificacion(ejemplo, reglas):
    explicacion = []
    for atributo, valor in ejemplo.items():
        for regla in reglas:
            ra, rv, clase, cuenta = regla
            if atributo == ra and valor == rv:
                explicacion.append(f"Si {atributo} = {valor} entonces clase = {clase} (soporte: {cuenta})")
    return explicacion

# Ejecutar el ejemplo
conteos = contar_atributos_clase(datos)
reglas = generar_reglas(conteos, umbral=1)

# Nuevo ejemplo a clasificar
nuevo_ejemplo = {"color": "rojo", "forma": "redondo", "tamaño": "grande"}

# Obtener explicación
explicacion = explicar_clasificacion(nuevo_ejemplo, reglas)

print("Explicación para la clasificación del nuevo ejemplo:")
for linea in explicacion:
    print(" -", linea)

"""
Salida esperada:

Explicación para la clasificación del nuevo ejemplo:
 - Si color = rojo entonces clase = manzana (soporte: 1)
 - Si forma = redondo entonces clase = manzana (soporte: 1)
 - Si tamaño = grande entonces clase = manzana (soporte: 1)

Esto indica que el ejemplo comparte características típicas de la clase 'manzana'.
"""
