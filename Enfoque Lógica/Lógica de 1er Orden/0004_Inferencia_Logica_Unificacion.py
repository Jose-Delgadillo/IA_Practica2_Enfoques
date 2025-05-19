"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Inferencia Lógica - Unificación

La unificación es un proceso fundamental en la lógica de primer orden.  
Permite determinar si dos expresiones pueden igualarse mediante sustitución  
de variables. Es una herramienta central en la resolución automática de problemas  
y los motores de inferencia lógicos.

Este programa implementa un algoritmo básico de unificación usando Python puro.
"""

def es_variable(x):
    return isinstance(x, str) and x[0].islower()

def es_constante(x):
    return isinstance(x, str) and x[0].isupper()

def es_funcion(x):
    return isinstance(x, tuple) and isinstance(x[1], list)

def aplicar_sustituciones(x, sustituciones):
    if es_variable(x) and x in sustituciones:
        return aplicar_sustituciones(sustituciones[x], sustituciones)
    elif es_funcion(x):
        return (x[0], [aplicar_sustituciones(arg, sustituciones) for arg in x[1]])
    else:
        return x

def ocurre(var, x):
    if var == x:
        return True
    elif es_funcion(x):
        return any(ocurre(var, arg) for arg in x[1])
    else:
        return False

def unificar_variable(var, x, sustituciones):
    if not es_variable(var):
        return None
    if var in sustituciones:
        return unificar(sustituciones[var], x, sustituciones)
    elif es_variable(x) and x in sustituciones:
        return unificar(var, sustituciones[x], sustituciones)
    elif ocurre(var, x):
        return None
    else:
        sustituciones[var] = x
        return sustituciones

def unificar(x, y, sustituciones=None):
    if sustituciones is None:
        sustituciones = {}

    x = aplicar_sustituciones(x, sustituciones)
    y = aplicar_sustituciones(y, sustituciones)

    if x == y:
        return sustituciones
    elif es_variable(x):
        return unificar_variable(x, y, sustituciones)
    elif es_variable(y):
        return unificar_variable(y, x, sustituciones)
    elif es_funcion(x) and es_funcion(y):
        if x[0] != y[0] or len(x[1]) != len(y[1]):
            return None
        for arg1, arg2 in zip(x[1], y[1]):
            sustituciones = unificar(arg1, arg2, sustituciones)
            if sustituciones is None:
                return None
        return sustituciones
    else:
        return None

def mostrar(term):
    if es_funcion(term):
        nombre, args = term
        return f"{nombre}({', '.join(map(mostrar, args))})"
    else:
        return str(term)

def ejemplo(t1, t2):
    print("\nIntentando unificar:")
    print("  ", mostrar(t1))
    print("  ", mostrar(t2))
    resultado = unificar(t1, t2)
    if resultado is None:
        print("  ❌ No se pueden unificar")
    else:
        print("  ✅ Unificación exitosa:")
        for var, val in resultado.items():
            print(f"   {var} → {mostrar(val)}")

# ----------------------------
# Casos de prueba
# ----------------------------

# padre(x) ≐ padre(Juan)
ejemplo(('padre', ['x']), ('padre', ['Juan']))

# ama(x, y) ≐ ama(Ana, Pedro)
ejemplo(('ama', ['x', 'y']), ('ama', ['Ana', 'Pedro']))

# f(x) ≐ f(a, b) → falla
ejemplo(('f', ['x']), ('f', ['a', 'b']))

# f(x, g(x)) ≐ f(g(a), y)
ejemplo(('f', ['x', ('g', ['x'])]), ('f', [('g', ['a']), 'y']))

# f(x, x) ≐ f(a, b) → debe fallar
ejemplo(('f', ['x', 'x']), ('f', ['a', 'b']))
