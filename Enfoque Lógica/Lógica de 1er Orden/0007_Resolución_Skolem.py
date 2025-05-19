"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Resolución - Skolemización

La Skolemización es una técnica que elimina los cuantificadores existenciales de las fórmulas 
lógicas de primer orden, reemplazándolos por funciones de Skolem. Es un paso importante para 
convertir una fórmula en forma normal conjuntiva (FNC), lo cual permite aplicar mecanismos de 
resolución automática.

Este programa implementa un ejemplo básico que toma una fórmula con cuantificadores, la transforma
eliminando los existenciales mediante funciones o constantes de Skolem, y muestra el resultado.
"""
# Representamos las fórmulas como árboles usando tuplas:
# ('∀', 'x', fórmula)       → Cuantificador universal
# ('∃', 'y', fórmula)       → Cuantificador existencial
# ('⇒', A, B)               → Implicación
# ('∧', A, B)               → Conjunción
# ('∨', A, B)               → Disyunción
# ('¬', A)                  → Negación
# ('pred', nombre, [args])  → Predicado

skolem_count = 0

# Genera un nuevo nombre de función/constante de Skolem
def nueva_funcion_skolem(libres):
    global skolem_count
    skolem_count += 1
    if libres:
        return ('f' + str(skolem_count), libres)
    else:
        return 'c' + str(skolem_count)  # constante

# Sustitución de variable por término
def sustituir(expr, var, valor):
    if isinstance(expr, tuple):
        if expr[0] == 'pred':
            return ('pred', expr[1], [valor if arg == var else arg for arg in expr[2]])
        else:
            return tuple([expr[0]] + [sustituir(e, var, valor) for e in expr[1:]])
    return expr

# Skolemización
def skolemizar(expr, libres=None):
    if libres is None:
        libres = []

    if isinstance(expr, tuple):
        if expr[0] == '∀':
            var = expr[1]
            return ('∀', var, skolemizar(expr[2], libres + [var]))
        elif expr[0] == '∃':
            var = expr[1]
            sk_term = nueva_funcion_skolem(libres)
            return skolemizar(sustituir(expr[2], var, sk_term), libres)
        else:
            return tuple([expr[0]] + [skolemizar(e, libres) for e in expr[1:]])
    return expr

# Mostrar expresiones de forma legible
def mostrar(expr):
    if isinstance(expr, tuple):
        if expr[0] == 'pred':
            args = ', '.join(map(str, expr[2]))
            return f"{expr[1]}({args})"
        elif expr[0] in {'∀', '∃'}:
            return f"{expr[0]}{expr[1]}.({mostrar(expr[2])})"
        elif expr[0] == '¬':
            return f"¬({mostrar(expr[1])})"
        else:
            return f"({mostrar(expr[1])} {expr[0]} {mostrar(expr[2])})"
    return str(expr)

# -----------------------------
# Ejemplo: ∀x ∃y ama(x, y)
# -----------------------------
f1 = ('∀', 'x', ('∃', 'y', ('pred', 'ama', ['x', 'y'])))
print("Fórmula original:")
print(mostrar(f1))

f1_sk = skolemizar(f1)
print("\nFórmula skolemizada:")
print(mostrar(f1_sk))

# -----------------------------
# Otro ejemplo: ∃x ∀y padre(x, y)
# -----------------------------
f2 = ('∃', 'x', ('∀', 'y', ('pred', 'padre', ['x', 'y'])))
print("\n\nFórmula original:")
print(mostrar(f2))

f2_sk = skolemizar(f2)
print("\nFórmula skolemizada:")
print(mostrar(f2_sk))
