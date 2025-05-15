"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Retropropagación del Error

Este programa implementa una Red Neuronal Multicapa (MLP) básica que se entrena
mediante el algoritmo de Retropropagación del Error (Backpropagation). Esta técnica
permite ajustar los pesos de la red propagando hacia atrás el error cometido en la
salida, actualizando los pesos de todas las capas para mejorar el rendimiento.

Se utiliza como ejemplo el problema de la compuerta lógica XOR, que no puede
ser resuelto por un perceptrón simple, pero sí por una MLP con al menos una
capa oculta y una función de activación no lineal (sigmoide).
"""

import random
import math

# ------------------------------------------------------------
# Funciones de activación
# ------------------------------------------------------------

def sigmoide(x):
    """Función de activación sigmoide."""
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    """Derivada de la sigmoide (x ya debe ser sigmoide(x))."""
    return x * (1 - x)

# ------------------------------------------------------------
# Clase Red Neuronal Multicapa
# ------------------------------------------------------------

class RedNeuronal:
    def __init__(self, num_entradas, num_ocultas, num_salidas, tasa_aprendizaje=0.5):
        self.tasa_aprendizaje = tasa_aprendizaje

        # Pesos de la capa de entrada a la capa oculta (matriz: ocultas x entradas)
        self.pesos_entrada_oculta = [
            [random.uniform(-1, 1) for _ in range(num_entradas)] for _ in range(num_ocultas)
        ]
        self.sesgos_ocultos = [random.uniform(-1, 1) for _ in range(num_ocultas)]

        # Pesos de la capa oculta a la capa de salida
        self.pesos_oculta_salida = [random.uniform(-1, 1) for _ in range(num_ocultas)]
        self.sesgo_salida = random.uniform(-1, 1)

    def alimentar(self, entrada):
        """Propagación hacia adelante (feedforward)."""
        # Capa oculta
        self.salidas_ocultas = []
        for i in range(len(self.pesos_entrada_oculta)):
            suma = sum(entrada[j] * self.pesos_entrada_oculta[i][j] for j in range(len(entrada))) + self.sesgos_ocultos[i]
            self.salidas_ocultas.append(sigmoide(suma))

        # Capa de salida
        suma_salida = sum(self.salidas_ocultas[i] * self.pesos_oculta_salida[i] for i in range(len(self.salidas_ocultas))) + self.sesgo_salida
        self.salida_final = sigmoide(suma_salida)

        return self.salida_final

    def entrenar(self, datos_entrada, datos_salida, epocas=10000):
        """Entrenamiento con retropropagación del error."""
        for epoca in range(epocas):
            error_total = 0
            for entrada, salida_esperada in zip(datos_entrada, datos_salida):
                salida = self.alimentar(entrada)

                # Error en la salida
                error_salida = salida_esperada - salida
                delta_salida = error_salida * derivada_sigmoide(salida)
                error_total += error_salida ** 2

                # Error en la capa oculta
                deltas_ocultos = []
                for i in range(len(self.salidas_ocultas)):
                    error_oculto = delta_salida * self.pesos_oculta_salida[i]
                    delta_oculto = error_oculto * derivada_sigmoide(self.salidas_ocultas[i])
                    deltas_ocultos.append(delta_oculto)

                # Actualizar pesos capa oculta -> salida
                for i in range(len(self.pesos_oculta_salida)):
                    self.pesos_oculta_salida[i] += self.tasa_aprendizaje * delta_salida * self.salidas_ocultas[i]
                self.sesgo_salida += self.tasa_aprendizaje * delta_salida

                # Actualizar pesos entrada -> capa oculta
                for i in range(len(self.pesos_entrada_oculta)):
                    for j in range(len(entrada)):
                        self.pesos_entrada_oculta[i][j] += self.tasa_aprendizaje * deltas_ocultos[i] * entrada[j]
                    self.sesgos_ocultos[i] += self.tasa_aprendizaje * deltas_ocultos[i]

            # Mostrar progreso cada 1000 épocas
            if epoca % 1000 == 0:
                print(f"Época {epoca}: Error total = {error_total:.4f}")

    def predecir(self, entrada):
        return self.alimentar(entrada)

# ------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------

if __name__ == "__main__":
    # Entradas para la compuerta XOR
    entradas = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    salidas_esperadas = [0, 1, 1, 0]

    # Crear red neuronal: 2 entradas, 2 neuronas ocultas, 1 salida
    red = RedNeuronal(num_entradas=2, num_ocultas=2, num_salidas=1)
    red.entrenar(entradas, salidas_esperadas, epocas=10000)

    # Resultados finales
    print("\nResultados después del entrenamiento:")
    for entrada, esperado in zip(entradas, salidas_esperadas):
        pred = red.predecir(entrada)
        print(f"Entrada: {entrada} => Predicción: {round(pred, 4)} (Esperado: {esperado})")
