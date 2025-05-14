"""
Prácticas de Inteligencia Artificial  
Red Bayesiana Dinámica: Filtrado de Partículas
"""

import random
from collections import Counter

# =============================================
# MODELO DEL MUNDO (RED BAYESIANA DINÁMICA SIMPLIFICADA)
# ---------------------------------------------
# - Estado oculto: posición discreta del agente (0 a 4).
# - Observaciones: sensor que detecta si está "cerca" de la posición objetivo (posición 2).
# - Objetivo: estimar la posición real del agente usando partículas (filtro de partículas).
# =============================================

# Inicializa una lista de partículas aleatorias distribuidas uniformemente
def inicializar_particulas(n_particulas, estados):
    # Cada partícula representa una hipótesis sobre la ubicación del agente
    return [random.choice(estados) for _ in range(n_particulas)]

# Modelo de transición: simula cómo se mueve el agente
def mover_estado(estado):
    # El agente puede moverse a la izquierda, quedarse, o moverse a la derecha
    if estado == 0:
        return random.choice([0, 1])  # Solo puede ir hacia la derecha o quedarse
    elif estado == 4:
        return random.choice([3, 4])  # Solo puede ir hacia la izquierda o quedarse
    else:
        return random.choice([estado - 1, estado, estado + 1])  # Tiene tres opciones

# Modelo de sensor: genera una observación basada en el estado real
def generar_observacion(estado_real):
    # Observa "Cerca" si está a 1 de distancia del objetivo (posición 2)
    if abs(estado_real - 2) <= 1:
        return True if random.random() < 0.8 else False  # Alta probabilidad si está cerca
    else:
        return True if random.random() < 0.2 else False  # Baja probabilidad si está lejos

# Calcula la probabilidad de una observación dada una partícula (estado)
def probabilidad_sensor(observacion, estado):
    if abs(estado - 2) <= 1:
        return 0.8 if observacion else 0.2
    else:
        return 0.2 if observacion else 0.8

# Re-muestreo: elige nuevas partículas según su peso (importancia)
def remuestrear(particulas, pesos):
    total = sum(pesos)
    if total == 0:
        # Si todos los pesos son cero, no hay buena información: elegir aleatoriamente
        return random.choices(particulas, k=len(particulas))
    
    # Normalizar los pesos para que sumen 1
    normalizados = [w / total for w in pesos]
    
    # Elegir nuevas partículas con probabilidad proporcional al peso
    return random.choices(particulas, weights=normalizados, k=len(particulas))

# =============================
# FILTRADO DE PARTÍCULAS PRINCIPAL
# =============================
def filtrado_particulas(num_pasos=10, n_particulas=100):
    estados_posibles = [0, 1, 2, 3, 4]  # Espacio de estados (posiciones posibles)
    particulas = inicializar_particulas(n_particulas, estados_posibles)  # Inicializar partículas

    estado_real = random.choice(estados_posibles)  # Escoger un estado real inicial aleatorio

    # Iniciar el ciclo de filtrado por cada paso de tiempo
    for paso in range(1, num_pasos + 1):
        # 1. Transición del estado real del agente
        estado_real = mover_estado(estado_real)

        # 2. Generar una observación basada en el estado real
        observacion = generar_observacion(estado_real)

        # 3. Transición de todas las partículas (predicción)
        particulas = [mover_estado(p) for p in particulas]

        # 4. Calcular el peso (importancia) de cada partícula según la observación
        pesos = [probabilidad_sensor(observacion, p) for p in particulas]

        # 5. Re-muestreo: seleccionar nuevas partículas con base en los pesos
        particulas = remuestrear(particulas, pesos)

        # 6. Estimar el estado actual como la moda (valor más frecuente) entre las partículas
        estimado = Counter(particulas).most_common(1)[0][0]

        # ====================
        # Imprimir resultados
        # ====================
        print(f"Paso {paso}")
        print(f"  Estado real:      {estado_real}")
        print(f"  Observación:      {'Cerca del objetivo' if observacion else 'Lejos'}")
        print(f"  Estimado (moda):  {estimado}")
        print(f"  Distribución de partículas: {Counter(particulas)}\n")

# Ejecutar el filtrado de partículas
filtrado_particulas()
