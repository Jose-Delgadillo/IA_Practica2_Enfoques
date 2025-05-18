"""
Prácticas de Inteligencia Artificial  
Gráficos por Computador: Detección de Aristas y Segmentación

Este programa implementa técnicas básicas de procesamiento de imágenes:  
1. **Detección de Aristas** usando el operador Sobel (simplificado)  
2. **Segmentación** por umbral, que separa regiones de una imagen en función de la intensidad.

La detección de aristas identifica bordes o contornos de objetos.  
La segmentación divide la imagen en partes significativas.  
Ambos procesos son pasos comunes en visión artificial y análisis de imágenes.

Este código usa matrices 2D simuladas como imágenes en escala de grises. No requiere librerías externas.
"""
# Imagen simulada como matriz 2D (imagen en escala de grises de 5x5)
imagen = [
    [10, 10, 10, 10, 10],
    [10, 50, 50, 50, 10],
    [10, 50, 90, 50, 10],
    [10, 50, 50, 50, 10],
    [10, 10, 10, 10, 10]
]

# --- Filtro Sobel simplificado (horizontal y vertical) ---
# Estos detectan cambios en intensidad, resaltando bordes
sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

sobel_y = [
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
]

def aplicar_sobel(imagen, kernel):
    """
    Aplica un filtro tipo Sobel (3x3) a una imagen 2D.
    Retorna una nueva imagen con las intensidades de borde detectadas.
    """
    filas = len(imagen)
    columnas = len(imagen[0])
    resultado = [[0]*columnas for _ in range(filas)]

    # Recorrer solo las posiciones válidas (sin bordes)
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            valor = 0
            for ki in range(-1, 2):
                for kj in range(-1, 2):
                    pixel = imagen[i + ki][j + kj]
                    peso = kernel[ki + 1][kj + 1]
                    valor += pixel * peso
            resultado[i][j] = abs(valor)  # Guardamos el valor absoluto del gradiente
    return resultado

# --- Magnitud del gradiente (combinación de X e Y) ---
def combinar_gradientes(grad_x, grad_y):
    """
    Combina dos gradientes (horizontal y vertical) para obtener la magnitud total.
    """
    filas = len(grad_x)
    columnas = len(grad_x[0])
    magnitud = [[0]*columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            # Magnitud de gradiente: raíz cuadrada de la suma de cuadrados (simplificada)
            magnitud[i][j] = min(255, int((grad_x[i][j]**2 + grad_y[i][j]**2)**0.5))
    return magnitud

# --- Segmentación binaria por umbral ---
def segmentar(imagen, umbral):
    """
    Segmenta una imagen en blanco (255) y negro (0) según un umbral de intensidad.
    """
    filas = len(imagen)
    columnas = len(imagen[0])
    salida = [[0]*columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            salida[i][j] = 255 if imagen[i][j] >= umbral else 0
    return salida

# --- Ejecución de la detección de bordes y segmentación ---
gradiente_x = aplicar_sobel(imagen, sobel_x)
gradiente_y = aplicar_sobel(imagen, sobel_y)
bordes = combinar_gradientes(gradiente_x, gradiente_y)
segmentada = segmentar(bordes, umbral=100)

# --- Imprimir resultados ---
print("\nImagen Original:")
for fila in imagen:
    print(fila)

print("\nBordes detectados (Sobel combinado):")
for fila in bordes:
    print(fila)

print("\nSegmentación por umbral (bordes resaltados):")
for fila in segmentada:
    print(fila)
