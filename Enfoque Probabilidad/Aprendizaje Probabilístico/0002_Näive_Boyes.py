"""
Prácticas de Inteligencia Artificial
Aprendizaje Probabilístico: Clasificador Naïve Bayes

Este programa implementa el algoritmo de clasificación Naïve Bayes, que asume que los atributos
son condicionalmente independientes dado la clase. Utiliza la Regla de Bayes para calcular
la probabilidad de cada clase basada en los atributos observados, y selecciona la clase
con mayor probabilidad posterior como resultado.

Es un método simple pero muy efectivo en tareas de clasificación.
"""

# Datos de entrenamiento: atributos y su clase asociada
# Formato: [(atributo1, atributo2, ..., clase)]
datos_entrenamiento = [
    ('soleado', 'calor', 'alta', 'débil', 'no'),
    ('soleado', 'calor', 'alta', 'fuerte', 'no'),
    ('nublado', 'calor', 'alta', 'débil', 'sí'),
    ('lluvia', 'templado', 'alta', 'débil', 'sí'),
    ('lluvia', 'frío', 'normal', 'débil', 'sí'),
    ('lluvia', 'frío', 'normal', 'fuerte', 'no'),
    ('nublado', 'frío', 'normal', 'fuerte', 'sí'),
    ('soleado', 'templado', 'alta', 'débil', 'no'),
    ('soleado', 'frío', 'normal', 'débil', 'sí'),
    ('lluvia', 'templado', 'normal', 'débil', 'sí'),
    ('soleado', 'templado', 'normal', 'fuerte', 'sí'),
    ('nublado', 'templado', 'alta', 'fuerte', 'sí'),
    ('nublado', 'calor', 'normal', 'débil', 'sí'),
    ('lluvia', 'templado', 'alta', 'fuerte', 'no')
]

# Lista de clases posibles
clases = ['sí', 'no']

# Lista de atributos por posición (separado por índice)
atributos = [
    ['soleado', 'nublado', 'lluvia'],        # Outlook
    ['calor', 'templado', 'frío'],           # Temperature
    ['alta', 'normal'],                      # Humidity
    ['débil', 'fuerte']                      # Wind
]

# Función para contar cuántas veces aparece cada clase
def contar_clases(datos):
    conteo = {'sí': 0, 'no': 0}
    for ejemplo in datos:
        clase = ejemplo[-1]
        conteo[clase] += 1
    return conteo

# Función que calcula las probabilidades condicionales P(attr_i | clase)
def contar_condicionales(datos):
    condicionales = {}  # (atributo_index, valor, clase) -> conteo
    for i in range(len(atributos)):
        for valor in atributos[i]:
            for clase in clases:
                condicionales[(i, valor, clase)] = 0

    for ejemplo in datos:
        for i in range(len(atributos)):
            valor = ejemplo[i]
            clase = ejemplo[-1]
            condicionales[(i, valor, clase)] += 1

    return condicionales

# Función para clasificar una nueva instancia usando Naïve Bayes
def clasificar(ejemplo, datos):
    total = len(datos)
    conteo_clases = contar_clases(datos)
    condicionales = contar_condicionales(datos)

    probabilidades = {}

    for clase in clases:
        # Probabilidad a priori: P(clase)
        prob = conteo_clases[clase] / total

        # Multiplicamos por las probabilidades condicionales: P(attr_i | clase)
        for i in range(len(ejemplo)):
            valor = ejemplo[i]
            # Conteo del valor dado la clase
            numerador = condicionales[(i, valor, clase)] + 1  # Suavizado de Laplace
            denominador = conteo_clases[clase] + len(atributos[i])  # Total posibles valores
            prob *= numerador / denominador

        probabilidades[clase] = prob

    # Elegir la clase con mayor probabilidad
    return max(probabilidades, key=probabilidades.get), probabilidades

# Ejemplo a clasificar (nuevo dato sin clase)
nuevo_ejemplo = ('soleado', 'templado', 'alta', 'débil')

# Clasificar
clase_predicha, probas = clasificar(nuevo_ejemplo, datos_entrenamiento)

# Mostrar resultados
print("===== Clasificador Naïve Bayes =====")
print("Ejemplo a clasificar:", nuevo_ejemplo)
print("\nProbabilidades por clase:")
for clase in probas:
    print(f"P({clase} | datos) = {probas[clase]:.4f}")

print(f"\nClase predicha: {clase_predicha}")
