"""
Prácticas de Inteligencia Artificial
Computación Neuronal: Separabilidad Lineal

Este programa demuestra el concepto de **separabilidad lineal**, que es la
capacidad de dividir correctamente un conjunto de datos en clases distintas
usando una línea (en 2D), un plano (en 3D) o un hiperplano (en más dimensiones).

Para ello se entrena un modelo **Perceptrón** básico en dos conjuntos de datos:
- La compuerta lógica **OR**, que *sí* es linealmente separable.
- La compuerta lógica **XOR**, que *NO* es linealmente separable.

El perceptrón intentará encontrar una línea de separación. Si el modelo logra
clasificar correctamente todos los ejemplos después de varias épocas, se
considera que el conjunto es linealmente separable.
"""

# ------------------------------------------------------------
# FUNCIONES AUXILIARES
# ------------------------------------------------------------

def step(x):
    """Función de activación escalón."""
    return 1 if x >= 0 else 0

def entrenar_perceptron(datos, salidas_esperadas, tasa_aprendizaje=0.1, max_epocas=20):
    """
    Entrena un perceptrón para clasificar los datos.

    Retorna: pesos, sesgo, éxito (True si convergió, False si no).
    """
    pesos = [0.0 for _ in datos[0]]
    sesgo = 0.0
    convergencia = False

    for epoca in range(max_epocas):
        errores = 0
        for i in range(len(datos)):
            entrada = datos[i]
            esperado = salidas_esperadas[i]
            salida = step(sum(x*w for x, w in zip(entrada, pesos)) + sesgo)
            error = esperado - salida

            # Actualizar pesos y sesgo si hay error
            if error != 0:
                errores += 1
                for j in range(len(pesos)):
                    pesos[j] += tasa_aprendizaje * error * entrada[j]
                sesgo += tasa_aprendizaje * error

        print(f"Época {epoca+1}: Pesos = {pesos}, Sesgo = {sesgo:.2f}, Errores = {errores}")
        if errores == 0:
            convergencia = True
            break

    return pesos, sesgo, convergencia

def probar_modelo(pesos, sesgo, datos):
    """
    Evalúa el modelo sobre los datos y retorna las salidas.
    """
    resultados = []
    for entrada in datos:
        salida = step(sum(x*w for x, w in zip(entrada, pesos)) + sesgo)
        resultados.append(salida)
    return resultados

# ------------------------------------------------------------
# PRUEBA DE SEPARABILIDAD LINEAL
# ------------------------------------------------------------

def prueba_separabilidad(nombre, entradas, salidas_esperadas):
    """
    Ejecuta el entrenamiento y evalúa si el conjunto es linealmente separable.
    """
    print(f"\nPRUEBA: {nombre}\n" + "-"*40)
    pesos, sesgo, es_separable = entrenar_perceptron(entradas, salidas_esperadas)
    if es_separable:
        print(f"✅ El conjunto '{nombre}' ES linealmente separable.\n")
    else:
        print(f"❌ El conjunto '{nombre}' NO es linealmente separable.\n")

    # Mostrar resultados finales
    for i, entrada in enumerate(entradas):
        salida = step(sum(x*w for x, w in zip(entrada, pesos)) + sesgo)
        print(f"Entrada: {entrada} => Salida: {salida}, Esperado: {salidas_esperadas[i]}")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

if __name__ == "__main__":
    # Compuerta OR (linealmente separable)
    entradas_or = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    salidas_or = [0, 1, 1, 1]

    # Compuerta XOR (no linealmente separable)
    entradas_xor = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    salidas_xor = [0, 1, 1, 0]

    # Pruebas
    prueba_separabilidad("Compuerta OR", entradas_or, salidas_or)
    prueba_separabilidad("Compuerta XOR", entradas_xor, salidas_xor)
