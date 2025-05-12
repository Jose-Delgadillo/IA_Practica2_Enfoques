"""
Prácticas de Inteligencia Artificial
Búsqueda Informada: Algoritmos Genéticos
"""

import random

# ============ Parámetros ============
TAM_CROMOSOMA = 8  # Tamaño del individuo (ej: 8 bits)
POBLACION_INICIAL = 6
GENERACIONES = 20
PROB_MUTACION = 0.1


# ============ Funciones clave ============

# Crear un cromosoma aleatorio (ej: [0,1,1,0,1,1,0,1])
def crear_cromosoma():
    return [random.randint(0, 1) for _ in range(TAM_CROMOSOMA)]

# Crear población inicial
def crear_poblacion():
    return [crear_cromosoma() for _ in range(POBLACION_INICIAL)]

# Evaluar el fitness (cuántos 1 tiene)
def evaluar(cromosoma):
    return sum(cromosoma)

# Selección por torneo (elige el mejor de dos aleatorios)
def seleccionar(poblacion):
    a = random.choice(poblacion)
    b = random.choice(poblacion)
    return a if evaluar(a) > evaluar(b) else b

# Cruce de un punto
def cruzar(padre1, padre2):
    punto = random.randint(1, TAM_CROMOSOMA - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

# Mutación (flip aleatorio de bits)
def mutar(cromosoma):
    return [gen if random.random() > PROB_MUTACION else 1 - gen for gen in cromosoma]


# ============ Algoritmo Genético Principal ============

def algoritmo_genetico():
    poblacion = crear_poblacion()

    for generacion in range(GENERACIONES):
        poblacion = sorted(poblacion, key=evaluar, reverse=True)
        print(f"Generación {generacion+1} - Mejor individuo: {poblacion[0]} Fitness: {evaluar(poblacion[0])}")

        nueva_poblacion = []

        while len(nueva_poblacion) < POBLACION_INICIAL:
            padre1 = seleccionar(poblacion)
            padre2 = seleccionar(poblacion)
            hijo1, hijo2 = cruzar(padre1, padre2)
            nueva_poblacion.extend([mutar(hijo1), mutar(hijo2)])

        # Mantener solo los mejores individuos
        poblacion = nueva_poblacion[:POBLACION_INICIAL]

    # Resultado final
    mejor = max(poblacion, key=evaluar)
    print("\n===== Resultado Final =====")
    print(f"Mejor cromosoma: {mejor}")
    print(f"Fitness: {evaluar(mejor)}")


# ============ Ejecutar ============
if __name__ == "__main__":
    algoritmo_genetico()
