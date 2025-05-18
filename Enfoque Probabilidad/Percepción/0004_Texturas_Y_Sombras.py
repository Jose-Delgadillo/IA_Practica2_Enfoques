"""
Prácticas de Inteligencia Artificial  
Gráficos por Computador: Texturas y Sombras

Este programa simula un sistema muy básico de texturizado y sombreado sobre una cuadrícula.  
- La **textura** se representa como un patrón de valores repetidos (por ejemplo, franjas).  
- La **sombra** se calcula con base en una fuente de luz y la orientación simulada de una superficie.

Ambos elementos son esenciales para dar realismo visual en gráficos 3D o entornos de simulación 2D.  
Este código está simplificado y usa solo Python puro, sin bibliotecas externas.
"""
# --- Generar una "superficie" simple como una matriz 2D ---
# Cada número representa la altura (z) de un punto en la superficie
superficie = [
    [1, 2, 3, 2, 1],
    [2, 3, 4, 3, 2],
    [3, 4, 5, 4, 3],
    [2, 3, 4, 3, 2],
    [1, 2, 3, 2, 1]
]

# --- Crear una textura: franjas horizontales ---
def aplicar_textura(superficie):
    """
    Crea una textura con franjas alternas sobre la superficie.
    Las filas pares se marcan con un patrón más oscuro (simulado).
    """
    filas = len(superficie)
    columnas = len(superficie[0])
    textura = [[0]*columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            # Alternar patrones según la fila
            if i % 2 == 0:
                textura[i][j] = 1  # Textura clara
            else:
                textura[i][j] = 0.6  # Textura oscura
    return textura

# --- Sombra basada en gradiente de altura (simula dirección de luz) ---
def calcular_sombra(superficie, direccion_luz=(1, 1)):
    """
    Calcula un sombreado simple basado en el cambio de altura.
    El sombreado es más oscuro donde hay más pendiente.
    """
    filas = len(superficie)
    columnas = len(superficie[0])
    sombra = [[0]*columnas for _ in range(filas)]
    dx, dy = direccion_luz

    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            # Derivadas aproximadas en X e Y
            grad_x = superficie[i][j+1] - superficie[i][j-1]
            grad_y = superficie[i+1][j] - superficie[i-1][j]

            # Producto escalar con la dirección de la luz
            intensidad = grad_x * dx + grad_y * dy

            # Normalizar a un rango entre 0 y 1
            intensidad = max(0, min(1, 1 - abs(intensidad) * 0.1))

            sombra[i][j] = intensidad
    return sombra

# --- Combinar textura y sombra ---
def renderizar(superficie, textura, sombra):
    """
    Aplica textura y sombra para simular iluminación sobre una superficie.
    """
    filas = len(superficie)
    columnas = len(superficie[0])
    render = [[0]*columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            # Producto de textura y sombra
            valor = textura[i][j] * sombra[i][j] if 0 <= i < len(sombra) and 0 <= j < len(sombra[0]) else 0
            render[i][j] = round(valor, 2)
    return render

# --- Ejecutar ---
textura = aplicar_textura(superficie)
sombra = calcular_sombra(superficie)
resultado = renderizar(superficie, textura, sombra)

# --- Imprimir resultados ---
print("\nSuperficie:")
for fila in superficie:
    print(fila)

print("\nTextura aplicada:")
for fila in textura:
    print(fila)

print("\nSombra calculada:")
for fila in sombra:
    print(fila)

print("\nRender final (textura + sombra):")
for fila in resultado:
    print(fila)
