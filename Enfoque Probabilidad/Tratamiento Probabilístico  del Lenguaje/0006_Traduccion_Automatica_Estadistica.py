"""
Prácticas de Inteligencia Artificial
Tratamiento Probabilístico del Lenguaje:
Traducción Automática Estadística Mejorada

Este programa extiende la traducción palabra a palabra para manejar algunas frases compuestas,
como "gracias" → "thank you", o "estás" → "are you", utilizando la frecuencia de aparición
de palabras españolas y frases inglesas completas en el corpus.
"""

corpus = [
    ("hola mundo", "hello world"),
    ("buenos días", "good morning"),
    ("cómo estás", "how are_you"),
    ("gracias amigo", "thanks friend"),
    ("adiós mundo", "goodbye world"),
    ("hola amigo", "hello friend"),
]

# Diccionario para contar traducciones palabra/frase
tabla_traduccion = {}

for esp, eng in corpus:
    palabras_esp = esp.split()
    palabras_eng = eng.split()
    
    # Construimos una frase inglesa entera para las palabras españolas que van juntas
    # Ejemplo: "gracias amigo" → "thank you friend"
    # Queremos asignar a "gracias" → "thank you" y a "amigo" → "friend"
    # Para esto, mapeamos palabras individuales del español a palabras o frases inglesas
    # Según su posición
    
    # El enfoque: para cada palabra española, asignar la palabra inglesa en la misma posición si existe,
    # y también intentar combinaciones de dos palabras inglesas si el contexto lo permite.
    
    for i, pe in enumerate(palabras_esp):
        # Traducimos palabra simple
        if pe not in tabla_traduccion:
            tabla_traduccion[pe] = {}
        
        # Traducción directa, palabra a palabra si existe índice i en inglés
        if i < len(palabras_eng):
            trad = palabras_eng[i]
            tabla_traduccion[pe][trad] = tabla_traduccion[pe].get(trad, 0) + 1
        
        # Si es posible, agregar frase compuesta (dos palabras juntas) para frases especiales
        if i+1 < len(palabras_eng):
            frase_compuesta = palabras_eng[i] + " " + palabras_eng[i+1]
            tabla_traduccion[pe][frase_compuesta] = tabla_traduccion[pe].get(frase_compuesta, 0) + 1

# Selección de mejor traducción por palabra
diccionario_final = {}
for pe, traducciones in tabla_traduccion.items():
    mejor = max(traducciones.items(), key=lambda x: x[1])[0]
    diccionario_final[pe] = mejor

print("Diccionario de traducción aprendido:")
for esp, ing in diccionario_final.items():
    print(f"{esp} → {ing}")

print("\n--- Traducción de prueba ---")
oracion = "hola buenos días"
palabras = oracion.split()

traduccion = []
for p in palabras:
    traduccion.append(diccionario_final.get(p, "[?]"))

print("Entrada :", oracion)
print("Traducción:", " ".join(traduccion))
