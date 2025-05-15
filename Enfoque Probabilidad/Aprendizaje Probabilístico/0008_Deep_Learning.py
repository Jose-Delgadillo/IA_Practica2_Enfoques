"""
Prácticas de Inteligencia Artificial
Aprendizaje Profundo (Deep Learning)

Este programa implementa una red neuronal simple con una capa oculta para clasificación binaria.
El aprendizaje profundo utiliza redes neuronales con múltiples capas para modelar relaciones
complejas en los datos. En este ejemplo, construimos y entrenamos la red desde cero usando NumPy,
sin utilizar librerías especializadas, para entender el proceso fundamental del entrenamiento
y la predicción en redes neuronales.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. Generación de datos
# ---------------------------

np.random.seed(42)
n_samples = 200

# Generamos datos para la clase 0 centrados en (-1, -1)
X0 = np.random.randn(n_samples // 2, 2) - 1
y0 = np.zeros(n_samples // 2)

# Generamos datos para la clase 1 centrados en (1, 1)
X1 = np.random.randn(n_samples // 2, 2) + 1
y1 = np.ones(n_samples // 2)

# Unimos los datos
X = np.vstack([X0, X1])
y = np.hstack([y0, y1])

# Visualizamos los datos
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
plt.title("Datos de entrenamiento (clases 0 y 1)")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# ---------------------------
# 2. Inicialización de la red neuronal
# ---------------------------

input_dim = 2
hidden_dim = 4
output_dim = 1

# Inicializamos los pesos y sesgos
W1 = np.random.randn(input_dim, hidden_dim) * 0.01
b1 = np.zeros((1, hidden_dim))
W2 = np.random.randn(hidden_dim, output_dim) * 0.01
b2 = np.zeros((1, output_dim))

# ---------------------------
# 3. Funciones auxiliares
# ---------------------------

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def forward(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    return Z1, A1, Z2, A2

def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

def backward(X, y, Z1, A1, Z2, A2, W1, b1, W2, b2, learning_rate=0.1):
    m = y.shape[0]
    dZ2 = A2 - y.reshape(-1, 1)
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * sigmoid_derivative(Z1)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    # Actualizamos pesos y sesgos
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    return W1, b1, W2, b2

# ---------------------------
# 4. Entrenamiento de la red
# ---------------------------

epochs = 1000

for epoch in range(epochs):
    Z1, A1, Z2, A2 = forward(X, W1, b1, W2, b2)
    loss = compute_loss(y, A2)
    W1, b1, W2, b2 = backward(X, y, Z1, A1, Z2, A2, W1, b1, W2, b2)
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, pérdida: {loss:.4f}")

# ---------------------------
# 5. Visualización de la frontera de decisión
# ---------------------------

def plot_decision_boundary(X, y, W1, b1, W2, b2):
    x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
    y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    _, _, _, probs = forward(grid, W1, b1, W2, b2)
    probs = probs.reshape(xx.shape)
    plt.contourf(xx, yy, probs, levels=[0, 0.5, 1], alpha=0.2, colors=['blue', 'red'])
    plt.scatter(X[:,0], X[:,1], c=y, cmap='bwr', edgecolors='k')
    plt.title("Frontera de decisión aprendida")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.show()

plot_decision_boundary(X, y, W1, b1, W2, b2)
