import random
import math

# --------- FUNCIONES KERNEL ---------

def kernel_lineal(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))

def kernel_rbf(x, y, gamma=0.5):
    return math.exp(-gamma * sum((xi - yi) ** 2 for xi, yi in zip(x, y)))

# --------- GENERAR DATOS SINTÉTICOS ---------

def generar_datos(n):
    clase_1 = [(random.gauss(2, 0.5), random.gauss(2, 0.5), 1) for _ in range(n)]
    clase_2 = [(random.gauss(-2, 0.5), random.gauss(-2, 0.5), -1) for _ in range(n)]
    return clase_1 + clase_2

# --------- ENTRENAMIENTO SVM SIMPLE (DUAL) ---------

def entrenar_svm(datos, kernel_func, C=1.0, pasos=100):
    n = len(datos)
    alfas = [0.0 for _ in range(n)]
    b = 0.0

    # Matriz de kernel
    K = [[kernel_func((x1, y1), (x2, y2)) for x2, y2, _ in datos] for x1, y1, _ in datos]

    for _ in range(pasos):
        for i in range(n):
            suma = sum(alfas[j] * datos[j][2] * K[i][j] for j in range(n))
            error_i = suma + b - datos[i][2]
            alfas[i] = min(max(alfas[i] - 0.01 * error_i, 0), C)

        b = sum(datos[i][2] - sum(alfas[j] * datos[j][2] * K[i][j] for j in range(n)) for i in range(n)) / n

    return alfas, b

# --------- CLASIFICACIÓN ---------

def predecir(punto, datos, alfas, b, kernel_func):
    resultado = sum(
        alfas[i] * datos[i][2] * kernel_func((datos[i][0], datos[i][1]), punto)
        for i in range(len(datos))
    ) + b
    return 1 if resultado >= 0 else -1

# --------- MAIN ---------

# Generar datos y entrenar
datos = generar_datos(20)
kernel = kernel_rbf  # Cambia a kernel_lineal si quieres

alfas, b = entrenar_svm(datos, kernel_func=kernel)

# Probar clasificación
pruebas = [(0, 0), (2, 2), (-2, -2), (1, -1)]

print("\n--- Clasificación con SVM (núcleo RBF) ---")
for p in pruebas:
    etiqueta = predecir(p, datos, alfas, b, kernel)
    print(f"Punto {p} => Clase predicha: {etiqueta}")
