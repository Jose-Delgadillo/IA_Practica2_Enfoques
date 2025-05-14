"""
Prácticas de Inteligencia Artificial  
Tema: Razonamiento Probabilístico en el Tiempo  
Subtema: Filtrado, Predicción, Suavizado y Explicación

Este programa simula las tareas más comunes en el razonamiento probabilístico en el tiempo usando una cadena de Markov Oculta (HMM).  
Se ilustra cómo calcular:

1. Filtrado (creencias actuales dado observaciones hasta el presente),
2. Predicción (creencias futuras),
3. Suavizado (creencias pasadas dado información futura),
4. Explicación (estado más probable actual).

Usamos un HMM básico con 2 estados (Saludable, Resfriado) y observaciones (Normal, Fiebre).
"""

# Estados ocultos
estados = ['Saludable', 'Resfriado']

# Posibles observaciones
observaciones = ['Normal', 'Fiebre']

# Distribución inicial
P_inicial = {
    'Saludable': 0.6,
    'Resfriado': 0.4
}

# Matriz de transición de estados: P(estado_t | estado_t-1)
P_transicion = {
    'Saludable': {'Saludable': 0.7, 'Resfriado': 0.3},
    'Resfriado': {'Saludable': 0.4, 'Resfriado': 0.6}
}

# Modelo de sensor: P(observacion | estado)
P_sensor = {
    'Saludable': {'Normal': 0.9, 'Fiebre': 0.1},
    'Resfriado': {'Normal': 0.2, 'Fiebre': 0.8}
}

# Secuencia de observaciones (por ejemplo del tiempo)
evidencias = ['Normal', 'Fiebre', 'Fiebre', 'Normal']

def normalizar(distribucion):
    total = sum(distribucion.values())
    return {k: v / total for k, v in distribucion.items()}

def filtrar(evidencias):
    """Filtrado hacia adelante: creencias actuales dado observaciones pasadas"""
    bel = P_inicial.copy()
    for e in evidencias:
        # Predicción
        bel_pronostico = {s: sum(P_transicion[s_prev][s] * bel[s_prev] for s_prev in estados) for s in estados}
        # Corrección
        bel = {s: P_sensor[s][e] * bel_pronostico[s] for s in estados}
        bel = normalizar(bel)
    return bel

def predecir(bel_actual, pasos):
    """Predicción hacia el futuro sin observaciones adicionales"""
    bel = bel_actual.copy()
    for _ in range(pasos):
        bel = {s: sum(P_transicion[s_prev][s] * bel[s_prev] for s_prev in estados) for s in estados}
    return normalizar(bel)

def suavizar(evidencias, tiempo):
    """Suavizado: estima creencias en un tiempo anterior usando toda la evidencia"""
    # Paso 1: hacia adelante (filtrado hasta tiempo t)
    bel_adelante = [P_inicial.copy()]
    for e in evidencias:
        bel = bel_adelante[-1]
        bel_pronostico = {s: sum(P_transicion[s_prev][s] * bel[s_prev] for s_prev in estados) for s in estados}
        bel_corr = {s: P_sensor[s][e] * bel_pronostico[s] for s in estados}
        bel_adelante.append(normalizar(bel_corr))

    # Paso 2: hacia atrás (del futuro al pasado)
    bel_atras = {s: 1.0 for s in estados}
    for e in reversed(evidencias[tiempo+1:]):
        bel_atras = {s: sum(P_transicion[s][s2] * P_sensor[s2][e] * bel_atras[s2] for s2 in estados) for s in estados}
        bel_atras = normalizar(bel_atras)

    # Combinación: hacia adelante (filtrado) * hacia atrás (posterior)
    bel_final = {s: bel_adelante[tiempo+1][s] * bel_atras[s] for s in estados}
    return normalizar(bel_final)

def explicacion(bel):
    """Estado más probable actualmente"""
    return max(bel, key=bel.get)

# === Ejecutar los distintos tipos de razonamiento ===
print("===== Razonamiento Probabilístico en el Tiempo =====")
print(f"Secuencia de observaciones: {evidencias}\n")

# Filtrado
bel_filtrado = filtrar(evidencias)
print(">>> Filtrado (estado actual):")
print(bel_filtrado)

# Predicción
prediccion_futura = predecir(bel_filtrado, pasos=2)
print("\n>>> Predicción (2 pasos al futuro):")
print(prediccion_futura)

# Suavizado
tiempo_pasado = 1
bel_suavizado = suavizar(evidencias, tiempo_pasado)
print(f"\n>>> Suavizado (estado en t={tiempo_pasado}):")
print(bel_suavizado)

# Explicación
estado_mas_probable = explicacion(bel_filtrado)
print("\n>>> Explicación (estado más probable ahora):")
print(f"{estado_mas_probable}")
