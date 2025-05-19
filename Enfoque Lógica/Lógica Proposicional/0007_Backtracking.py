"""
Prácticas de Inteligencia Artificial  
Enfoque: Resolución de Problemas  
Técnica: Backtracking (Vuelta Atrás)

El backtracking (o retroceso) es una técnica general para resolver problemas 
combinatorios mediante búsqueda. Se utiliza para explorar todas las posibles 
configuraciones de una solución y retroceder cuando se detecta que no se puede 
llegar a una solución válida desde la configuración actual.

Este ejemplo resuelve el clásico problema de las N reinas: 
colocar N reinas en un tablero NxN de modo que ninguna se ataque mutuamente.
"""

# ----------------------------
# Función principal de resolución
# ----------------------------

def resolver_n_reinas(n):
    """
    Resuelve el problema de las N reinas usando backtracking.
    Retorna una lista con una solución donde el índice representa la fila
    y el valor en esa posición la columna donde va la reina.
    """
    soluciones = []
    tablero = [-1] * n  # tablero[i] = columna donde está la reina en la fila i

    def es_valido(fila, columna):
        """
        Verifica que no haya conflicto con las reinas ya colocadas.
        """
        for i in range(fila):
            if tablero[i] == columna or \
               abs(tablero[i] - columna) == abs(i - fila):  # misma diagonal
                return False
        return True

    def backtrack(fila):
        """
        Intenta colocar una reina en la fila dada y llama recursivamente
        para las siguientes filas.
        """
        if fila == n:
            soluciones.append(tablero[:])  # se encontró una solución completa
            return

        for col in range(n):
            if es_valido(fila, col):
                tablero[fila] = col
                backtrack(fila + 1)
                # No es necesario "deshacer" el movimiento porque
                # el valor se sobrescribe en la siguiente iteración

    backtrack(0)
    return soluciones

# ----------------------------
# Mostrar la solución
# ----------------------------

def imprimir_tablero(tablero):
    """
    Dibuja el tablero con las reinas colocadas.
    """
    n = len(tablero)
    for fila in range(n):
        linea = ""
        for col in range(n):
            if tablero[fila] == col:
                linea += "♛ "
            else:
                linea += ". "
        print(linea)
    print()

# ----------------------------
# Ejecución del programa
# ----------------------------

N = 8  # Puedes cambiar el valor a 4, 5, 6, ... dependiendo del tamaño del problema
soluciones = resolver_n_reinas(N)

print(f"Se encontraron {len(soluciones)} soluciones para {N} reinas:\n")

# Imprimir solo una solución de ejemplo
if soluciones:
    imprimir_tablero(soluciones[0])
