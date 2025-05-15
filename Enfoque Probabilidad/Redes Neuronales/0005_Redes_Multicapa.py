"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Redes Neuronales Multicapa (MLP)

Este programa implementa una Red Neuronal Multicapa (MLP, por sus siglas en inglés)
con una capa oculta, diseñada para resolver problemas no linealmente separables
como la compuerta lógica XOR.

Las redes MLP permiten modelar funciones complejas gracias a sus múltiples capas
y a la retropropagación del error, que ajusta los pesos para minimizar el error.

Este ejemplo se entrena completamente en Python puro, sin librerías externas.
"""

import random
import math

# ------------------------------------------------------------
# FUNCIONES DE ACTIVACIÓN
# ------------------------------------------------------------

def sigmoide(x):
    """Función de activación sigmoide."""
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    """Derivada de la función sigmoide (para backpropagation)."""
    return x * (1 - x)  # x ya debe ser sigmoide(x)

# ------------------------------------------------------------
# CLASE PARA LA RED NEURONAL MULTICAPA
# ------------------------------------------------------------

class RedNeuronalMLP:
    def __init__(self, num_entradas, num_ocultas, num_salidas, tasa_aprendizaje=0.5):
        # Inicializar pesos y sesgos con valores aleatorios pequeños
        self.tasa_aprendizaje = tasa_aprendizaje

        # Pesos de entrada a capa oculta
        self.pesos_entrada_oculta = [[random.uniform(-1, 1) for _ in range(num_entradas)] for _ in range(num_ocultas)]
        self.sesgos_ocultos = [random.uniform(-1, 1) for _ in range(num_ocultas)]

        # Pesos de capa oculta a salida
        self.pesos_oculta_salida = [random.uniform(-1, 1) for _ in range(num_ocultas)]
        self.sesgo_salida = random.uniform(-1, 1)

    def alimentar(self, entrada):
        """Propagación hacia adelante (feedforward)."""
        # Capa oculta
        self.salida_oculta = []
        for i in range(len(self.pesos_entrada_oculta)):
            suma = sum(x*w for x, w in zip(entrada, self.pesos_entrada_oculta[i])) + self.sesgos_ocultos[i]
            self.salida_oculta.append(sigmoide(suma))

        # Capa de salida
        suma_salida = sum(h*w for h, w in zip(self.salida_oculta, self.pesos_oculta_salida)) + self.sesgo_salida
        self.salida_final = sigmoide(suma_salida)

        return self.salida_final

    def entrenar(self, datos_entrenamiento, salidas_esperadas, epocas=10000):
        for epoca in range(epocas):
            error_total = 0
            for entrada, esperado in zip(datos_entrenamiento, salidas_esperadas):
                # 1. Propagación hacia adelante
                salida = self.alimentar(entrada)

                # 2. Cálculo del error de salida
                error_salida = esperado - salida
                delta_salida = error_salida * derivada_sigmoide(salida)
                error_total += error_salida ** 2

                # 3. Cálculo del error para cada neurona oculta
                deltas_ocultos = []
                for i in range(len(self.salida_oculta)):
                    error = delta_salida * self.pesos_oculta_salida[i]
                    deltas_ocultos.append(error * derivada_sigmoide(self.salida_oculta[i]))

                # 4. Actualización de pesos de la capa oculta a salida
                for i in range(len(self.pesos_oculta_salida)):
                    self.pesos_oculta_salida[i] += self.tasa_aprendizaje * delta_salida * self.salida_oculta[i]
                self.sesgo_salida += self.tasa_aprendizaje * delta_salida

                # 5. Actualización de pesos de entrada a capa oculta
                for i in range(len(self.pesos_entrada_oculta)):
                    for j in range(len(self.pesos_entrada_oculta[i])):
                        self.pesos_entrada_oculta[i][j] += self.tasa_aprendizaje * deltas_ocultos[i] * entrada[j]
                    self.sesgos_ocultos[i] += self.tasa_aprendizaje * deltas_ocultos[i]

            # Mostrar progreso cada 1000 épocas
            if epoca % 1000 == 0:
                print(f"Época {epoca}: Error total = {error_total:.4f}")

    def predecir(self, entrada):
        return self.alimentar(entrada)

# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

if __name__ == "__main__":
    # Datos de entrenamiento para la compuerta XOR
    entradas = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    salidas_esperadas = [0, 1, 1, 0]

    # Crear y entrenar red neuronal
    red = RedNeuronalMLP(num_entradas=2, num_ocultas=2, num_salidas=1)
    red.entrenar(entradas, salidas_esperadas, epocas=10000)

    # Mostrar resultados finales
    print("\nResultados finales:")
    for entrada, esperado in zip(entradas, salidas_esperadas):
        salida = red.predecir(entrada)
        print(f"Entrada: {entrada} => Salida: {round(salida, 4)} (Esperado: {esperado})")
