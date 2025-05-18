"""
Prácticas de Inteligencia Artificial  
Percepción: Reconocimiento de Escritura

Este programa implementa un sistema simple de reconocimiento de caracteres escritos a mano,
utilizando representaciones binarias (matrices de 0s y 1s) para las letras.
El reconocimiento se hace comparando la entrada con un conjunto de plantillas predefinidas
usando una métrica de similitud básica (conteo de coincidencias de bits).

Este enfoque es útil para ilustrar los conceptos de plantillas y reconocimiento visual sin librerías externas.
"""
# --- Plantillas binarias de letras ---
# Cada letra es una matriz 5x3 (alto x ancho)
plantillas = {
    "A": [
        [0, 1, 0],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1]
    ],
    "B": [
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 0]
    ],
    "C": [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
        [0, 1, 1]
    ]
}

# --- Función de similitud entre dos matrices ---
def similitud(matriz1, matriz2):
    total = 0
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if matriz1[i][j] == matriz2[i][j]:
                total += 1
    return total

# --- Función para reconocer una letra dada una matriz de entrada ---
def reconocer_letra(entrada, plantillas):
    mejor_letra = None
    mejor_puntaje = -1
    for letra, plantilla in plantillas.items():
        puntaje = similitud(entrada, plantilla)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_letra = letra
    return mejor_letra, mejor_puntaje

# --- Ejemplo de entrada simulando una letra "A" escrita a mano con pequeñas diferencias ---
entrada_usuario = [
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 1]
]

# --- Mostrar entrada ---
print("Letra ingresada:")
for fila in entrada_usuario:
    print(fila)

# --- Reconocer la letra ---
letra, puntaje = reconocer_letra(entrada_usuario, plantillas)
print(f"\nLetra reconocida: {letra} (similitud: {puntaje}/15)")
