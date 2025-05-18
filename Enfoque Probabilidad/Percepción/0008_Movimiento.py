"""
Prácticas de Inteligencia Artificial  
Percepción: Movimiento

Este programa simula la detección de movimiento entre dos imágenes binarias (frames).
El movimiento se detecta comparando píxel por píxel en dos cuadros consecutivos.
Donde haya una diferencia (1 → 0 o 0 → 1), se asume que ocurrió movimiento.

Este enfoque es útil para sistemas simples de vigilancia, detección de actividad,
y análisis de secuencias de imágenes en visión por computadora.
"""
# --- Función para detectar movimiento entre dos cuadros ---
def detectar_movimiento(frame1, frame2):
    alto = len(frame1)
    ancho = len(frame1[0])
    movimiento = [[0 for _ in range(ancho)] for _ in range(alto)]

    for i in range(alto):
        for j in range(ancho):
            if frame1[i][j] != frame2[i][j]:
                movimiento[i][j] = 1  # Detecta diferencia (movimiento)
    return movimiento

# --- Simulación de dos cuadros (frames) de una escena en binario ---
frame_anterior = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

frame_actual = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# --- Mostrar los cuadros originales ---
print("Frame anterior:")
for fila in frame_anterior:
    print(fila)

print("\nFrame actual:")
for fila in frame_actual:
    print(fila)

# --- Detectar movimiento ---
mov = detectar_movimiento(frame_anterior, frame_actual)

# --- Mostrar los píxeles donde se detectó movimiento ---
print("\nMapa de movimiento detectado (1 = cambio detectado):")
for fila in mov:
    print(fila)
