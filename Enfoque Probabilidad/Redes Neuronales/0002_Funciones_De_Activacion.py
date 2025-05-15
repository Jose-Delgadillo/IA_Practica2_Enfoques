"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Funciones de Activación

Las funciones de activación son componentes fundamentales en las redes neuronales artificiales,
ya que determinan cómo se transforman las señales que llegan a una neurona. Su propósito principal
es introducir **no linealidad** en la red, permitiendo que esta aprenda patrones complejos.

Este programa implementa varias funciones de activación clásicas:
- Función escalón (Heaviside)
- Función sigmoide logística
- Función tangente hiperbólica (tanh)
- Función ReLU (Rectified Linear Unit)

Como estamos trabajando sin librerías externas, las gráficas se muestran de forma textual simple.
"""

import math

# ----------------------------
# Funciones de activación
# ----------------------------

def escalon(x):
    """Función escalón (Heaviside)"""
    return 1 if x >= 0 else 0

def sigmoide(x):
    """Función sigmoide logística"""
    return 1 / (1 + math.exp(-x))

def tanh(x):
    """Función tangente hiperbólica"""
    return math.tanh(x)

def relu(x):
    """Función ReLU"""
    return max(0, x)

# ----------------------------
# Simulación de gráfico textual
# ----------------------------

def imprimir_funcion(nombre, funcion, rango=(-10, 10), paso=1):
    print(f"\n{name_format(nombre)}")
    print("-" * 40)
    for x in range(rango[0], rango[1] + 1, paso):
        y = funcion(x)
        n = int(y * 20) if y >= 0 else int(-y * 20)
        barra = '#' * n
        if y >= 0:
            print(f"x={x:>3} | {barra}")
        else:
            print(f"x={x:>3} | {' ' * 20}{barra}")

def name_format(text):
    """Formatea los nombres en mayúsculas centrados"""
    return f"{text.upper():^40}"

# ----------------------------
# Ejecución del programa
# ----------------------------

if __name__ == "__main__":
    # Mostramos las funciones una por una
    imprimir_funcion("Escalón", escalon, rango=(-5, 5), paso=1)
    imprimir_funcion("Sigmoide", sigmoide, rango=(-5, 5), paso=1)
    imprimir_funcion("Tangente Hiperbólica", tanh, rango=(-5, 5), paso=1)
    imprimir_funcion("ReLU", relu, rango=(-5, 5), paso=1)
