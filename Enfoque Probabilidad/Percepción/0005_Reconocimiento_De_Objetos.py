"""
Prácticas de Inteligencia Artificial  
Percepción: Reconocimiento de Objetos

Este programa simula un sistema básico de reconocimiento de objetos a partir de representaciones matriciales simples.  
Se trabaja con plantillas (templates) de formas y una imagen escaneada.  
El algoritmo compara regiones de la imagen con las plantillas y determina si algún objeto conocido está presente.

Este es un ejemplo sencillo basado en coincidencia directa, sin usar bibliotecas externas ni aprendizaje profundo.
"""
# --- Definir plantillas de objetos conocidos (formas) ---
plantillas = {
    "cuadro": [
        [1, 1],
        [1, 1]
    ],
    "línea_h": [
        [1, 1, 1]
    ],
    "línea_v": [
        [1],
        [1],
        [1]
    ]
}

# --- Imagen de entrada (escena) ---
imagen = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0],
]

# --- Función para comparar una subregión con una plantilla ---
def coincide(imagen, plantilla, fila, col):
    for i in range(len(plantilla)):
        for j in range(len(plantilla[0])):
            # Verifica bordes
            if fila + i >= len(imagen) or col + j >= len(imagen[0]):
                return False
            if imagen[fila + i][col + j] != plantilla[i][j]:
                return False
    return True

# --- Buscar objetos en la imagen ---
def reconocer_objetos(imagen, plantillas):
    hallazgos = []
    for nombre, plantilla in plantillas.items():
        for i in range(len(imagen)):
            for j in range(len(imagen[0])):
                if coincide(imagen, plantilla, i, j):
                    hallazgos.append((nombre, i, j))
    return hallazgos

# --- Ejecutar ---
resultados = reconocer_objetos(imagen, plantillas)

# --- Mostrar resultados ---
print("Imagen:")
for fila in imagen:
    print(fila)

print("\nObjetos reconocidos:")
for objeto, fila, col in resultados:
    print(f"- {objeto} en posición ({fila}, {col})")
