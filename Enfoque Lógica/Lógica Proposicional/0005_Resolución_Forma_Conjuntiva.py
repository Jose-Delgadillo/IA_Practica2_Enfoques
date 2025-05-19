"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Lógica Proposicional: Resolución y Forma Normal Conjuntiva (FNC)

Este programa muestra cómo aplicar la técnica de resolución lógica sobre un conjunto de proposiciones
ya transformadas a su Forma Normal Conjuntiva (FNC).

- La Forma Normal Conjuntiva consiste en una conjunción de disyunciones de literales (A ∨ B) ∧ (¬A ∨ C)
- La resolución es una regla de inferencia que permite deducir una nueva cláusula al eliminar literales
  complementarios (por ejemplo, A y ¬A).

Este ejemplo se implementa usando Python puro (sin librerías externas), y resuelve si un conjunto
de cláusulas lleva a una contradicción (cláusula vacía).
"""
# --- Funciones de utilidad ---

def negacion(literal):
    """
    Devuelve la negación de un literal:
    Si es A, devuelve ¬A
    Si es ¬A, devuelve A
    """
    return literal[1:] if literal.startswith('¬') else '¬' + literal

def resolver(clausula1, clausula2):
    """
    Intenta aplicar la resolución entre dos cláusulas.
    Si encuentra un literal en una y su negación en otra, genera una nueva cláusula sin ellos.
    Si no se puede resolver, devuelve None.
    """
    for l1 in clausula1:
        for l2 in clausula2:
            if l1 == negacion(l2):
                nueva = set(clausula1 + clausula2)
                nueva.discard(l1)
                nueva.discard(l2)
                return list(nueva)
    return None

def aplicar_resolucion(clausulas):
    """
    Aplica el algoritmo de resolución proposicional:
    - Repite hasta que ya no se generen nuevas cláusulas o se derive una contradicción (cláusula vacía)
    """
    nuevas = []

    while True:
        n = len(clausulas)
        pares = [(clausulas[i], clausulas[j]) for i in range(n) for j in range(i+1, n)]

        for (c1, c2) in pares:
            resolvente = resolver(c1, c2)
            if resolvente is not None:
                if resolvente == []:
                    print(f"\n¡Contradicción encontrada entre {c1} y {c2}!")
                    return True
                if resolvente not in nuevas:
                    nuevas.append(resolvente)

        if all(nueva in clausulas for nueva in nuevas):
            return False  # No se pudo deducir nada nuevo

        for nueva in nuevas:
            if nueva not in clausulas:
                clausulas.append(nueva)

# --- Definimos un conjunto de cláusulas en FNC ---

"""
Ejemplo:
(p ∨ q)
(¬p ∨ r)
(¬q ∨ r)
(¬r)

Estas cláusulas se representan como listas de literales.
"""

clausulas = [
    ['p', 'q'],
    ['¬p', 'r'],
    ['¬q', 'r'],
    ['¬r']
]

# Mostramos las cláusulas iniciales
print("Cláusulas en Forma Normal Conjuntiva:")
for c in clausulas:
    print(" ∨ ".join(c))

# Aplicamos resolución
resultado = aplicar_resolucion(clausulas)

print("\n¿Se dedujo una contradicción? =>", resultado)
