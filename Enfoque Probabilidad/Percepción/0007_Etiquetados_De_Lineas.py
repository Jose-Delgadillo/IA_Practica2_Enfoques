"""
Prácticas de Inteligencia Artificial  
Percepción: Etiquetado de Líneas

Este programa implementa un algoritmo simple de etiquetado de regiones conectadas en una imagen binaria.
Dada una matriz de 0s y 1s que representa una imagen (1 = píxel blanco / parte de un objeto, 0 = fondo),
el objetivo es asignar una etiqueta numérica distinta a cada conjunto de píxeles conectados.

Este procedimiento es útil para identificar contornos, objetos, líneas y otras regiones
en tareas de segmentación y análisis de imágenes.
"""
# --- Función de etiquetado por conexión en 4 direcciones ---
def etiquetar_lineas(imagen):
    # Clonamos la imagen para no modificar el original
    alto = len(imagen)
    ancho = len(imagen[0])
    etiquetas = [[0 for _ in range(ancho)] for _ in range(alto)]

    etiqueta_actual = 1

    # Función recursiva para expandir la etiqueta
    def expandir(i, j, etiqueta):
        if i < 0 or j < 0 or i >= alto or j >= ancho:
            return
        if imagen[i][j] == 1 and etiquetas[i][j] == 0:
            etiquetas[i][j] = etiqueta
            # Revisamos arriba, abajo, izquierda, derecha (conexión 4)
            expandir(i-1, j, etiqueta)
            expandir(i+1, j, etiqueta)
            expandir(i, j-1, etiqueta)
            expandir(i, j+1, etiqueta)

    # Recorremos la imagen para encontrar regiones conectadas
    for i in range(alto):
        for j in range(ancho):
            if imagen[i][j] == 1 and etiquetas[i][j] == 0:
                expandir(i, j, etiqueta_actual)
                etiqueta_actual += 1

    return etiquetas, etiqueta_actual - 1

# --- Imagen binaria de ejemplo: líneas verticales ---
imagen_binaria = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

# --- Mostrar la imagen original ---
print("Imagen binaria original:")
for fila in imagen_binaria:
    print(fila)

# --- Etiquetar líneas conectadas ---
etiquetas, total = etiquetar_lineas(imagen_binaria)

# --- Mostrar el resultado ---
print("\nImagen etiquetada (cada número representa una región diferente):")
for fila in etiquetas:
    print(fila)

print(f"\nTotal de regiones etiquetadas: {total}")
