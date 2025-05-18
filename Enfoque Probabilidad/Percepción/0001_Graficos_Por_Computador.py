"""
Prácticas de Inteligencia Artificial
Gráficos por Computador

Este programa muestra cómo representar gráficos simples en la consola usando caracteres ASCII.
El objetivo es entender conceptos fundamentales como puntos, líneas y coordenadas
sin usar librerías gráficas externas.

Ejemplo incluye:
- Dibujar un punto
- Dibujar una línea usando el algoritmo de Bresenham simplificado
"""

# Tamaño del "canvas" o área de dibujo (ancho x alto)
ancho = 40
alto = 20

# Creamos una matriz 2D (lista de listas) para representar los pixeles
# Inicialmente todos vacíos (espacios)
canvas = [[' ' for _ in range(ancho)] for _ in range(alto)]

def dibujar_punto(x, y, char='*'):
    """
    Dibuja un punto en la posición (x, y) del canvas usando el carácter especificado.
    Coordenadas (0,0) están en la esquina superior izquierda.
    """
    if 0 <= x < ancho and 0 <= y < alto:
        canvas[y][x] = char  # Nota: y es fila, x es columna

def dibujar_linea(x0, y0, x1, y1, char='*'):
    """
    Dibuja una línea entre los puntos (x0, y0) y (x1, y1) usando el algoritmo de Bresenham.
    Esto asegura que la línea sea lo más recta posible en una cuadrícula discreta.
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            dibujar_punto(x, y, char)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            dibujar_punto(x, y, char)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    dibujar_punto(x, y, char)  # Dibuja el último punto

def mostrar_canvas():
    """
    Imprime el contenido del canvas en consola.
    """
    for fila in canvas:
        print("".join(fila))

# --- Programa principal ---

# Dibujar algunos puntos sueltos
dibujar_punto(5, 5)
dibujar_punto(10, 2)
dibujar_punto(15, 10)

# Dibujar líneas
dibujar_linea(0, 0, 39, 19)  # Diagonal principal
dibujar_linea(0, 19, 39, 0)  # Diagonal secundaria
dibujar_linea(20, 0, 20, 19) # Línea vertical central
dibujar_linea(0, 10, 39, 10) # Línea horizontal central

# Mostrar resultado
mostrar_canvas()
