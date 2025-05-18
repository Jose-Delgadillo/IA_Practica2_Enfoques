"""
Prácticas de Inteligencia Artificial
Tratamiento Probabilístico del Lenguaje:
Recuperación de Información

Este programa implementa un sistema básico de Recuperación de Información (IR),
usando un enfoque probabilístico de coincidencia basado en el modelo de bolsa de palabras (bag-of-words).
El sistema indexa un pequeño conjunto de documentos y responde consultas con una lista
ordenada de documentos más relevantes, calculando una puntuación basada en la presencia
y frecuencia de las palabras clave (TF: frecuencia de término).

Se utiliza Python puro sin librerías externas.
"""
# Base de documentos simples para pruebas
documentos = {
    1: "el gato duerme en la alfombra",
    2: "el perro ladra al gato",
    3: "el perro duerme en su cama",
    4: "la alfombra es grande y roja"
}

def limpiar(texto):
    """Elimina signos de puntuación y pasa a minúsculas"""
    caracteres_invalidos = ",.;:¿?!¡"
    for c in caracteres_invalidos:
        texto = texto.replace(c, "")
    return texto.lower().split()

# Crear índice invertido: palabra -> lista de IDs de documentos donde aparece
def construir_indice(documentos):
    indice = {}
    for doc_id, texto in documentos.items():
        palabras = limpiar(texto)
        for palabra in palabras:
            if palabra not in indice:
                indice[palabra] = set()
            indice[palabra].add(doc_id)
    return indice

# Calcular puntuación TF (frecuencia de término) simple para una consulta
def puntuar_documentos(consulta, documentos):
    consulta_palabras = limpiar(consulta)
    puntuaciones = {}

    for doc_id, texto in documentos.items():
        palabras = limpiar(texto)
        puntuacion = 0
        for palabra in consulta_palabras:
            puntuacion += palabras.count(palabra)  # frecuencia simple
        puntuaciones[doc_id] = puntuacion
    return puntuaciones

# Mostrar resultados ordenados por relevancia
def mostrar_resultados(puntuaciones, documentos):
    resultados = sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)
    print("\nDocumentos más relevantes:")
    for doc_id, score in resultados:
        if score > 0:
            print(f"[{score}] Documento {doc_id}: {documentos[doc_id]}")

# Ejecución principal
indice = construir_indice(documentos)

print("Bienvenido al sistema de recuperación de información.")
while True:
    consulta = input("\nEscriba su consulta (o 'salir'): ")
    if consulta.lower() == "salir":
        break
    puntuaciones = puntuar_documentos(consulta, documentos)
    mostrar_resultados(puntuaciones, documentos)
