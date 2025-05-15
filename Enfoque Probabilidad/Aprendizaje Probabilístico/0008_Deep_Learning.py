# Importamos las librerías necesarias
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

def deep_learning_mnist():
    """
    Ejemplo básico de red neuronal profunda para clasificar dígitos del dataset MNIST.
    """

    # Cargamos el dataset MNIST, que ya viene dividido en train y test
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Mostramos la forma de los datos
    print(f'Tamaño de conjunto de entrenamiento: {x_train.shape}')
    print(f'Tamaño de conjunto de prueba: {x_test.shape}')

    # Preprocesamiento:
    # Normalizamos los valores de píxeles (0-255) a un rango de 0 a 1 para mejor entrenamiento
    x_train = x_train.astype('float32') / 255
    x_test = x_test.astype('float32') / 255

    # Aplanamos las imágenes de 28x28 a vectores de 784 para la red densa
    x_train = x_train.reshape(-1, 28 * 28)
    x_test = x_test.reshape(-1, 28 * 28)

    # Definimos el modelo secuencial: varias capas densas (fully connected)
    model = models.Sequential([
        layers.Dense(512, activation='relu', input_shape=(784,)),  # Primera capa oculta con 512 neuronas y activación ReLU
        layers.Dense(256, activation='relu'),                      # Segunda capa oculta con 256 neuronas
        layers.Dense(10, activation='softmax')                     # Capa de salida con 10 neuronas (una por clase), activación softmax para probabilidad
    ])

    # Compilamos el modelo:
    # - Optimizador Adam: algoritmo para actualizar los pesos
    # - Función de pérdida: sparse_categorical_crossentropy, adecuada para clasificación múltiple con etiquetas enteras
    # - Métrica: accuracy para evaluar desempeño
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Entrenamos el modelo con los datos de entrenamiento
    history = model.fit(x_train, y_train,
                        epochs=10,        # Número de épocas (iteraciones completas sobre todo el dataset)
                        batch_size=128,   # Tamaño del lote para cada actualización
                        validation_split=0.2)  # 20% de los datos se usan para validación durante el entrenamiento

    # Evaluamos el modelo en el conjunto de prueba
    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
    print(f'\nPrecisión en conjunto de prueba: {test_acc:.4f}')

    # Graficamos la evolución de la precisión en entrenamiento y validación
    plt.plot(history.history['accuracy'], label='Precisión entrenamiento')
    plt.plot(history.history['val_accuracy'], label='Precisión validación')
    plt.xlabel('Épocas')
    plt.ylabel('Precisión')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    deep_learning_mnist()
