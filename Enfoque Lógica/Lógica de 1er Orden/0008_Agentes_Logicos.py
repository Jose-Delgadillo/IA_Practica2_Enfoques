"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Agentes Lógicos

Un agente lógico es un sistema que actúa y toma decisiones basándose en un conocimiento
representado formalmente mediante lógica proposicional o de primer orden, y utiliza
mecanismos de inferencia lógica para derivar nuevas conclusiones y actuar en consecuencia.

Este código muestra un agente simple basado en lógica proposicional que, dado un conocimiento
base (base de conocimiento) y una consulta, determina si la consulta es consecuencia lógica
de la base usando inferencia por resolución.
"""

# Representación simple de cláusulas como conjuntos de literales (para la lógica proposicional)
# Ejemplo de literal: 'P', '~Q' (donde ~ indica negación)

def resolver(base_conocimiento, consulta):
    """
    Implementa la resolución para determinar si consulta es consecuencia lógica
    de la base de conocimiento (ambas listas de cláusulas).
    
    base_conocimiento: lista de cláusulas (cada cláusula es un conjunto de literales)
    consulta: fórmula proposicional (en forma de cláusulas) que queremos probar

    Retorna True si la consulta se deduce, False si no.
    """
    # Negamos la consulta y la añadimos a la base para demostrar por contradicción
    clausulas = base_conocimiento.copy()
    for c in consulta:
        clausulas.append(set(neg(lit) for lit in c))

    nueva = set()
    
    while True:
        n = len(clausulas)
        pares = [(clausulas[i], clausulas[j]) for i in range(n) for j in range(i+1, n)]
        
        for (ci, cj) in pares:
            resolventes = resolver_clausulas(ci, cj)
            if set() in resolventes:
                return True  # Clausula vacía => contradicción encontrada
            
            nueva.update(resolventes)
        
        if nueva.issubset(set(map(frozenset, clausulas))):
            return False  # No se generaron clausulas nuevas, no se puede derivar consulta
        
        for c in nueva:
            if c not in clausulas:
                clausulas.append(c)

def neg(literal):
    """Negación simple para literales en forma de string"""
    return literal[1:] if literal.startswith('~') else '~' + literal

def resolver_clausulas(ci, cj):
    """
    Dada dos cláusulas (conjuntos de literales), genera todos los resolventes
    eliminando un par de literales complementarios.
    """
    resolventes = set()
    for lit in ci:
        if neg(lit) in cj:
            res = (ci - {lit}) | (cj - {neg(lit)})
            resolventes.add(frozenset(res))
    return resolventes

# -------------------------
# Ejemplo de uso del agente
# -------------------------

# Base de conocimiento: 
# (P ∨ Q), (~P ∨ R), (~Q ∨ R), (~R)
KB = [
    {'P', 'Q'},
    {'~P', 'R'},
    {'~Q', 'R'},
    {'~R'}
]

# Consulta a probar: {Q}
consulta = [{'Q'}]

print("¿Se puede deducir Q de la base de conocimiento?")
resultado = resolver(KB, consulta)
print("Respuesta:", resultado)
