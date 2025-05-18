"""
Prácticas de Inteligencia Artificial
Tratamiento Probabilístico del Lenguaje:
Extracción de Información

Este programa simula un sistema básico de extracción de información (IE) a partir de textos simples.
La extracción de información busca encontrar hechos, entidades o relaciones relevantes dentro de documentos.

En este caso, se implementa un sistema muy simple en Python puro que:
1. Detecta entidades como personas, lugares y fechas usando expresiones regulares.
2. Extrae relaciones básicas como "Persona trabaja en Organización" a partir de patrones conocidos.

Este tipo de enfoque es útil para tareas de análisis de texto, minería de datos o preprocesamiento de lenguaje natural.
"""
import re

# Base de ejemplos de texto
textos = [
    "Juan Pérez trabaja en Google desde 2018.",
    "María Gómez fue contratada por Microsoft en enero de 2021.",
    "Carlos López se incorporó a IBM el 5 de marzo de 2020.",
    "Ana Ruiz fundó una startup en Monterrey en 2019."
]

# Expresiones regulares para entidades
patron_persona = r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\b"
patron_organizacion = r"\b(Google|Microsoft|IBM|startup)\b"
patron_lugar = r"\b(Monterrey|CDMX|México)\b"
patron_fecha = r"\b(\d{4}|[0-9]{1,2}\s+de\s+[a-z]+|enero|febrero|marzo)\b"

# Patrones de relaciones: persona -> organización
patron_relacion = r"([A-Z][a-z]+\s[A-Z][a-z]+).+(trabaja en|contratada por|incorporó a|fundó).+(Google|Microsoft|IBM|startup)"

# Función para extraer entidades
def extraer_entidades(texto):
    personas = re.findall(patron_persona, texto)
    organizaciones = re.findall(patron_organizacion, texto)
    lugares = re.findall(patron_lugar, texto)
    fechas = re.findall(patron_fecha, texto)
    return personas, organizaciones, lugares, fechas

# Función para extraer relaciones
def extraer_relaciones(texto):
    relaciones = re.findall(patron_relacion, texto)
    return relaciones

# Proceso principal
for i, texto in enumerate(textos):
    print(f"\n--- Documento {i+1} ---")
    print(f"Texto: {texto}")
    
    # Extracción de entidades
    personas, organizaciones, lugares, fechas = extraer_entidades(texto)
    print("Personas encontradas:", set(personas))
    print("Organizaciones encontradas:", set(organizaciones))
    print("Lugares encontrados:", set(lugares))
    print("Fechas encontradas:", set(fechas))
    
    # Extracción de relaciones
    relaciones = extraer_relaciones(texto)
    for persona, verbo, organizacion in relaciones:
        print(f"Relación detectada: {persona} → {verbo} → {organizacion}")
