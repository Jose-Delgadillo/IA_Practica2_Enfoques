"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Programación Lógica (Prolog y CLIPS)

Este programa simula conceptos básicos de programación lógica inspirados en Prolog y CLIPS.
Se representa una base de conocimiento con hechos y reglas, y se implementa un motor simple
de inferencia lógica similar a lo que haría un sistema Prolog o CLIPS.

Se puede hacer consultas sobre relaciones como "padre", "abuelo", etc., y el sistema
responderá si pueden deducirse lógicamente a partir de las reglas definidas.
"""
# Base de conocimientos: hechos y reglas
hechos = {
    'padre(Juan, Pedro)',
    'padre(Juan, Ana)',
    'padre(Pedro, Luis)',
    'madre(Maria, Pedro)',
    'madre(Maria, Ana)'
}

reglas = [
    # Si X es padre o madre de Y, entonces X es progenitor de Y
    ('progenitor(X, Y)', ['padre(X, Y)']),
    ('progenitor(X, Y)', ['madre(X, Y)']),

    # Si X es progenitor de Y y Y es progenitor de Z, entonces X es abuelo de Z
    ('abuelo(X, Z)', ['padre(X, Y)', 'progenitor(Y, Z)']),

    # Si X es progenitor de Y, y Y es progenitor de Z, entonces X es antecesor de Z
    ('antecesor(X, Z)', ['progenitor(X, Z)']),
    ('antecesor(X, Z)', ['progenitor(X, Y)', 'antecesor(Y, Z)'])
]

# Función para hacer matching de predicados
def unificar(pred1, pred2, bindings=None):
    if bindings is None:
        bindings = {}

    def parse(t):
        nombre, args = t.split('(')
        args = args[:-1].split(',')
        return nombre.strip(), [a.strip() for a in args]

    nombre1, args1 = parse(pred1)
    nombre2, args2 = parse(pred2)

    if nombre1 != nombre2 or len(args1) != len(args2):
        return None

    b = bindings.copy()
    for a1, a2 in zip(args1, args2):
        if a1[0].isupper():  # Variable
            if a1 in b:
                if b[a1] != a2:
                    return None
            else:
                b[a1] = a2
        elif a1 != a2:
            return None
    return b

# Función de resolución: intenta probar un objetivo con los hechos y reglas
def resolver(objetivo, hechos, reglas, nivel=0):
    indent = "  " * nivel
    print(f"{indent}¿Se puede probar: {objetivo}?")

    # Buscar en los hechos
    for hecho in hechos:
        b = unificar(objetivo, hecho)
        if b is not None:
            print(f"{indent}✅ Se cumple directamente: {hecho}")
            return True

    # Buscar en las reglas
    for cabeza, cuerpo in reglas:
        b = unificar(objetivo, cabeza)
        if b is not None:
            print(f"{indent}🔁 Intentando aplicar regla: {cabeza} :- {cuerpo}")
            # Aplicar la sustitución a los predicados del cuerpo
            cuerpo_sust = []
            for pred in cuerpo:
                for var, val in b.items():
                    pred = pred.replace(var, val)
                cuerpo_sust.append(pred)
            # Resolver cada parte del cuerpo recursivamente
            if all(resolver(p, hechos, reglas, nivel+1) for p in cuerpo_sust):
                print(f"{indent}✅ Se puede deducir: {objetivo}")
                return True

    print(f"{indent}❌ No se puede probar: {objetivo}")
    return False

# -----------------------------
# Pruebas
# -----------------------------
consultas = [
    'progenitor(Juan, Pedro)',
    'progenitor(Maria, Ana)',
    'abuelo(Juan, Luis)',
    'abuelo(Maria, Luis)',
    'antecesor(Juan, Luis)',
    'antecesor(Juan, Ana)',
    'antecesor(Pedro, Luis)'
]

print("\n--- Consultas ---")
for c in consultas:
    print("\nConsulta:", c)
    resolver(c, hechos, reglas)
