"""
Prácticas de Inteligencia Artificial
Reconocimiento del Habla (Simulado con entrada de texto)
"""

# Esta función simula el reconocimiento de voz pidiendo texto por consola.
def reconocimiento_de_voz_simulado():
    print("=== Reconocimiento de voz simulado ===")
    print("Escribe una frase (como si estuvieras hablando):")
    texto = input(">>")

    # Procesamiento simulado del texto "reconocido"
    print("\nTexto reconocido:")
    print(texto)

    # Ejemplo simple de análisis
    if "hola" in texto.lower():
        print("-> Saludo detectado.")
    elif "clima" in texto.lower():
        print("-> Pregunta sobre el clima detectada.")
    elif "adiós" in texto.lower():
        print("-> Despedida detectada.")
    else:
        print("-> Frase general detectada.")

# Ejecutar la función principal
if __name__ == "__main__":
    reconocimiento_de_voz_simulado()
