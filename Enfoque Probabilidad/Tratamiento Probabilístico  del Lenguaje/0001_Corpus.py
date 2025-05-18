"""
Prácticas de Inteligencia Artificial
Tratamiento Probabilístico del Lenguaje: Modelo Probabilístico del Lenguaje a partir de un Corpus

Este programa implementa un modelo probabilístico simple del lenguaje usando un corpus textual.
A partir de un texto dado, el programa calcula las frecuencias de aparición de palabras
(unigrama) y pares de palabras consecutivas (bigrama), y estima sus probabilidades.
Este enfoque permite modelar cómo se distribuyen las palabras en un idioma, útil en
tareas como predicción de palabras, corrección automática o generación de texto.
"""

# Corpus de ejemplo
texto = """
el gato duerme en la alfombra
el perro duerme en la alfombra
la gata duerme en el sofá
el perro ladra fuerte
"""

# Preprocesamiento: convertir el texto a minúsculas y separar las palabras
palabras = texto.lower().replace('\n', ' ').split()

# Diccionarios para contar unigrama y bigrama
conteo_unigrama = {}
conteo_bigrama = {}

# Contar unigrama (frecuencia de cada palabra)
for palabra in palabras:
    if palabra in conteo_unigrama:
        conteo_unigrama[palabra] += 1
    else:
        conteo_unigrama[palabra] = 1

# Contar bigrama (frecuencia de cada par de palabras consecutivas)
for i in range(len(palabras) - 1):
    par = (palabras[i], palabras[i+1])
    if par in conteo_bigrama:
        conteo_bigrama[par] += 1
    else:
        conteo_bigrama[par] = 1

# Cálculo de probabilidades unigramas
total_palabras = sum(conteo_unigrama.values())
prob_unigrama = {}
for palabra in conteo_unigrama:
    prob_unigrama[palabra] = conteo_unigrama[palabra] / total_palabras

# Cálculo de probabilidades bigramas
prob_bigrama = {}
for (w1, w2) in conteo_bigrama:
    prob_bigrama[(w1, w2)] = conteo_bigrama[(w1, w2)] / conteo_unigrama[w1]

# Mostrar resultados
print("Frecuencias Unigrama:")
for palabra in conteo_unigrama:
    print(f"{palabra}: {conteo_unigrama[palabra]} (P={prob_unigrama[palabra]:.3f})")

print("\nFrecuencias Bigrama:")
for par in conteo_bigrama:
    print(f"{par[0]} {par[1]}: {conteo_bigrama[par]} (P={prob_bigrama[par]:.3f})")

# Ejemplo de predicción: ¿qué palabra es más probable que siga a "el"?
print("\nPredicciones para la palabra 'el':")
for (w1, w2) in prob_bigrama:
    if w1 == "el":
        print(f"el {w2}: {prob_bigrama[(w1, w2)]:.3f}")
