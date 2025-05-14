"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico en el Tiempo
Subtema: Filtros de Kalman

Este programa implementa un Filtro de Kalman unidimensional simple.
Se utiliza para estimar el estado de un sistema dinámico lineal con ruido gaussiano.
"""

# Parámetros del modelo (se pueden ajustar para experimentar)
import random

# Simulación del sistema real
def sistema_real(x, movimiento_real, ruido_mov):
    return x + movimiento_real + random.gauss(0, ruido_mov)

# Simulación de una medición del sistema con ruido
def medir(x_real, ruido_sensor):
    return x_real + random.gauss(0, ruido_sensor)

# Filtro de Kalman
def filtro_kalman(z, x_est, p_est, movimiento, var_mov, var_sensor):
    """
    z: medición actual
    x_est: estado estimado previo
    p_est: varianza (incertidumbre) previa
    movimiento: movimiento que se espera aplicar
    var_mov: varianza del modelo de movimiento
    var_sensor: varianza del sensor (ruido de la medición)
    """
    # Paso 1: Predicción
    x_pred = x_est + movimiento
    p_pred = p_est + var_mov

    # Paso 2: Actualización con la medición
    K = p_pred / (p_pred + var_sensor)  # Ganancia de Kalman
    x_new = x_pred + K * (z - x_pred)
    p_new = (1 - K) * p_pred

    return x_new, p_new

# ======================= EJECUCIÓN ==========================

print("===== Filtro de Kalman (1D) =====\n")

# Valores iniciales
x_real = 0               # Posición real
x_est = 0                # Estimación inicial
p_est = 1                # Incertidumbre inicial
movimiento = 1           # Movimiento por paso
var_mov = 0.2            # Varianza del movimiento
var_sensor = 1.0         # Varianza del sensor

# Ciclo de estimación
for paso in range(1, 11):
    # El sistema se mueve (con ruido)
    x_real = sistema_real(x_real, movimiento, var_mov)

    # Se obtiene una medición ruidosa
    z = medir(x_real, var_sensor)

    # Filtro de Kalman actualiza la estimación
    x_est, p_est = filtro_kalman(z, x_est, p_est, movimiento, var_mov, var_sensor)

    print(f"Paso {paso}")
    print(f"  Real:      {x_real:.2f}")
    print(f"  Medición:  {z:.2f}")
    print(f"  Estimado:  {x_est:.2f}")
    print(f"  Incertidumbre: {p_est:.2f}")
    print()
