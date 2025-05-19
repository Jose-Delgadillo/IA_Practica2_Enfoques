"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Lógica Proposicional: Encadenamiento Hacia Adelante y Hacia Atrás

Este programa implementa dos métodos clásicos de inferencia lógica:

1. Encadenamiento Hacia Adelante (Forward Chaining):
   - Parte de los hechos conocidos y aplica reglas para deducir nuevos hechos.
   - Se usa comúnmente en sistemas expertos para construir conclusiones.

2. Encadenamiento Hacia Atrás (Backward Chaining):
   - Parte de una meta y trabaja hacia atrás buscando si se puede justificar con los hechos y reglas.
   - Es útil para diagnóstico, verificación de hipótesis o planeación.

Ambos algoritmos están implementados en Python puro, sin uso de librerías externas.
"""

# ----------------------------
# Representación de reglas y hechos
# ----------------------------

# Reglas de inferencia, cada una como una tupla: (antecedentes, consecuente)
# Ejemplo: si A y B son verdaderos, entonces C es verdadero
reglas = [
    (["A"], "B"),
    (["B", "C"], "D"),
    (["D"], "E"),
    (["F"], "C")
]

# Hechos conocidos inicialmente
hechos_iniciales = ["A", "F"]

# Meta que queremos demostrar con encadenamiento hacia atrás
meta_objetivo = "E"

# ----------------------------
# Encadenamiento hacia adelante
# ----------------------------

def encadenamiento_adelante(hechos, reglas):
    """
    Aplica encadenamiento hacia adelante:
    Usa hechos conocidos y aplica reglas para deducir nuevos hechos.
    """
    nuevos = list(hechos)         # Copiamos los hechos iniciales
    inferidos = set(nuevos)       # Usamos un conjunto para acceso rápido
    cambio = True                 # Flag para seguir aplicando reglas

    print("\nEncadenamiento hacia adelante:")

    while cambio:
        cambio = False
        for antecedentes, consecuente in reglas:
            # Si todos los antecedentes están en los hechos y aún no se ha inferido el consecuente
            if all(p in inferidos for p in antecedentes) and consecuente not in inferidos:
                print(f"De {antecedentes} se infiere {consecuente}")
                inferidos.add(consecuente)
                nuevos.append(consecuente)
                cambio = True

    print("\nHechos inferidos:", nuevos)
    return nuevos

# ----------------------------
# Encadenamiento hacia atrás
# ----------------------------

def encadenamiento_atras(meta, hechos, reglas, trazado=None):
    """
    Aplica encadenamiento hacia atrás:
    Intenta demostrar una meta utilizando hechos y reglas.
    """
    if trazado is None:
        trazado = set()  # conjunto para evitar ciclos

    if meta in hechos:
        print(f"Meta {meta} ya está en los hechos.")
        return True

    if meta in trazado:
        return False  # evitar bucles infinitos
    trazado.add(meta)

    print(f"\nTratando de demostrar {meta}...")

    # Buscar reglas cuyo consecuente sea la meta
    for antecedentes, consecuente in reglas:
        if consecuente == meta:
            print(f"Regla encontrada: {antecedentes} → {consecuente}")
            # Intentamos demostrar todos los antecedentes recursivamente
            if all(encadenamiento_atras(p, hechos, reglas, trazado) for p in antecedentes):
                print(f"✓ Meta {meta} demostrada por {antecedentes}")
                return True

    print(f"✗ No se pudo demostrar {meta}")
    return False

# ----------------------------
# Ejecución del programa
# ----------------------------

# Encadenamiento hacia adelante
hechos_deducidos = encadenamiento_adelante(hechos_iniciales, reglas)

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás para demostrar la meta:", meta_objetivo)
resultado = encadenamiento_atras(meta_objetivo, hechos_iniciales, reglas)

print("\n¿Meta lograda? =>", resultado)
