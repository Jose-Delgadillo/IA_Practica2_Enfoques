"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Funciones de Activación

Las funciones de activación son esenciales en las redes neuronales artificiales,
ya que permiten introducir **no linealidad** al modelo. Sin ellas, una red neuronal
sería simplemente una combinación lineal, incapaz de aprender patrones complejos.

Este programa implementa algunas de las funciones de activación más comunes:
1. Escalón (Heaviside): activa o no activa una neurona con base en un umbral.
2. Sigmoide: función suave que aplana los extremos y transforma cualquier valor
   real a un rango entre 0 y 1.
3. Tangente hiperbólica: similar a la sigmoide pero con rango entre -1 y 1.
4. ReLU (Rectified Linear Unit): muy popular en redes profundas, pasa valores positivos tal cual y pone cero a los negativos.

Dado que no usamos librerías como matplotlib, las "gráficas" se muestran como
barras de texto para visualizar la forma de cada función.
"""

import math  # Importamos funciones matemáticas básicas

# ------------------------------------------------------
# DEFINICIÓN DE FUNCIONES DE ACTIVACIÓN
# ------------------------------------------------------

def escalon(x):
    """
    Función de activación tipo escalón.
    Devuelve 1 si x es mayor o igual a 0, de lo contrario devuelve 0.
    Representa una activación binaria (todo o nada).
    """
    return 1 if x >= 0 else 0

def sigmoide(x):
    """
    Función sigmoide logística.
    Utiliza la fórmula 1 / (1 + e^(-x)).
    Su rango está entre 0 y 1, útil para clasificación.
    """
    return 1 / (1 + math.exp(-x))

def tanh(x):
    """
    Tangente hiperbólica.
    Similar a la sigmoide, pero su rango es entre -1 y 1.
    La salida centrada en cero suele ayudar al aprendizaje.
    """
    return math.tanh(x)

def relu(x):
    """
    Función ReLU (Rectified Linear Unit).
    Devuelve x si x > 0, o 0 en caso contrario.
    Es eficiente y evita el problema del gradiente desvanecido.
    """
    return max(0, x)

# ------------------------------------------------------
# IMPRESIÓN VISUAL DE CADA FUNCIÓN EN CONSOLA (Gráfica textual)
# ------------------------------------------------------

def imprimir_funcion(nombre, funcion, rango=(-10, 10), paso=1):
    """
    Imprime en consola una representación visual de una función.

    Parámetros:
    - nombre: Nombre de la función (para mostrar en título).
    - funcion: función Python que acepta un número y devuelve un valor.
    - rango: tupla con el rango de valores de x a evaluar.
    - paso: paso entre valores de x (por defecto 1).
    """

    print(f"\n{name_format(nombre)}")  # Título centrado
    print("-" * 50)

    for x in range(rango[0], rango[1] + 1, paso):
        y = funcion(x)  # Calculamos el valor de salida de la función

        # Convertimos el valor de salida y en una barra de caracteres
        if y >= 0:
            cantidad = int(y * 20)  # Escalamos para que la barra sea visible
            barra = '#' * cantidad
            print(f"x={x:>3} | {barra}")
        else:
            # Para funciones como tanh que pueden ser negativas
            cantidad = int(-y * 20)
            barra = '#' * cantidad
            print(f"x={x:>3} | {' ' * 20}{barra}")  # Alineamos a la derecha

def name_format(text):
    """
    Da formato centrado a los nombres de las funciones para encabezados.
    """
    return f"{text.upper():^50}"  # Centrado en 50 caracteres

# ------------------------------------------------------
# EJECUCIÓN PRINCIPAL DEL PROGRAMA
# ------------------------------------------------------

if __name__ == "__main__":
    # Mostramos cada función en el mismo rango para comparar sus formas
    imprimir_funcion("Escalón", escalon, rango=(-5, 5), paso=1)
    imprimir_funcion("Sigmoide", sigmoide, rango=(-5, 5), paso=1)
    imprimir_funcion("Tangente Hiperbólica", tanh, rango=(-5, 5), paso=1)
    imprimir_funcion("ReLU", relu, rango=(-5, 5), paso=1)
