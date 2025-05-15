"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Perceptrón, ADALINE y MADALINE

Este programa ilustra tres modelos de redes neuronales básicas:

1. **Perceptrón**: Clasificador binario que aprende ajustando pesos con base
   en el error de clasificación (funciona bien con datos linealmente separables).

2. **ADALINE (Adaptive Linear Neuron)**: Similar al perceptrón, pero usa
   una función de activación lineal durante el entrenamiento, permitiendo un
   ajuste más fino gracias al uso del error cuadrático.

3. **MADALINE (Multiple ADALINE)**: Red neuronal multicapa con múltiples
   neuronas ADALINE en la primera capa. Por simplicidad, aquí se describe
   teóricamente y no se implementa por completo sin librerías avanzadas.

Este código entrena los modelos Perceptrón y ADALINE en la compuerta lógica
OR, usando Python puro y salidas por consola.
"""

# ------------------------------------------------------------
# FUNCIONES AUXILIARES
# ------------------------------------------------------------

def step_function(x):
    """Función de activación escalón (usada en perceptrón)."""
    return 1 if x >= 0 else 0

def linear_activation(x):
    """Función de activación lineal (usada en ADALINE)."""
    return x  # No se aplica umbral hasta después del entrenamiento

def print_weights(epoch, weights, bias):
    """Imprime los pesos y sesgo en cada época."""
    print(f"Época {epoch + 1}: Pesos = {weights}, Bias = {bias:.2f}")

# ------------------------------------------------------------
# PERCEPTRÓN
# ------------------------------------------------------------

def entrenar_perceptron(entradas, salidas, tasa_aprendizaje=0.1, epocas=10):
    """
    Entrena un modelo Perceptrón sobre un conjunto de datos binarios.
    """
    print("\nENTRENAMIENTO PERCEPTRÓN\n" + "-" * 40)

    pesos = [0, 0]  # Inicialización de pesos
    bias = 0        # Inicialización del sesgo

    for epoca in range(epocas):
        for i in range(len(entradas)):
            suma = sum(p * x for p, x in zip(pesos, entradas[i])) + bias
            salida = step_function(suma)
            error = salidas[i] - salida

            # Ajuste de pesos y bias
            for j in range(len(pesos)):
                pesos[j] += tasa_aprendizaje * error * entradas[i][j]
            bias += tasa_aprendizaje * error

        print_weights(epoca, pesos, bias)

    return pesos, bias

# ------------------------------------------------------------
# ADALINE
# ------------------------------------------------------------

def entrenar_adaline(entradas, salidas, tasa_aprendizaje=0.01, epocas=10):
    """
    Entrena un modelo ADALINE sobre un conjunto de datos binarios.
    A diferencia del perceptrón, usa activación lineal para el cálculo del error.
    """
    print("\nENTRENAMIENTO ADALINE\n" + "-" * 40)

    pesos = [0.0, 0.0]
    bias = 0.0

    for epoca in range(epocas):
        for i in range(len(entradas)):
            suma = sum(p * x for p, x in zip(pesos, entradas[i])) + bias
            salida = linear_activation(suma)
            error = salidas[i] - salida

            # Actualización basada en el error lineal
            for j in range(len(pesos)):
                pesos[j] += tasa_aprendizaje * error * entradas[i][j]
            bias += tasa_aprendizaje * error

        print_weights(epoca, pesos, bias)

    return pesos, bias

# ------------------------------------------------------------
# PRUEBA DE LOS MODELOS CON LA COMPUERTA OR
# ------------------------------------------------------------

def prueba_modelo(pesos, bias, modelo_nombre):
    """
    Evalúa el modelo entrenado con la tabla OR.
    """
    print(f"\nPRUEBA DEL MODELO ({modelo_nombre})\n" + "-" * 40)
    for x1 in [0, 1]:
        for x2 in [0, 1]:
            suma = pesos[0]*x1 + pesos[1]*x2 + bias
            salida = step_function(suma)
            print(f"Entrada: ({x1}, {x2}) => Salida: {salida}")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

if __name__ == "__main__":
    # Datos de entrenamiento para la compuerta OR
    entradas = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    salidas = [0, 1, 1, 1]

    # Entrenamiento del Perceptrón
    pesos_perceptron, bias_perceptron = entrenar_perceptron(entradas, salidas)
    prueba_modelo(pesos_perceptron, bias_perceptron, "Perceptrón")

    # Entrenamiento de ADALINE
    pesos_adaline, bias_adaline = entrenar_adaline(entradas, salidas)
    prueba_modelo(pesos_adaline, bias_adaline, "ADALINE")

