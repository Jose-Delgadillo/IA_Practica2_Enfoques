"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Lógica Proposicional: Base de Conocimiento

Este programa simula una Base de Conocimiento (KB) usando lógica proposicional.
Una KB es un conjunto de fórmulas lógicas que representan hechos y reglas del mundo.
En este caso, se permite agregar hechos y consultar inferencias básicas usando 
evaluación directa de expresiones. Es un ejemplo introductorio de cómo se puede representar
y razonar con conocimiento simbólico en Inteligencia Artificial.
"""
# --- Base de Conocimiento como diccionario de hechos y reglas ---
base_conocimiento = {
    "llueve": True,
    "tengo_paraguas": False,
    "mojado_si_llueve_y_sin_paraguas": "(llueve and not tengo_paraguas)"
}

# --- Evaluador lógico simple ---
def evaluar_regla(nombre, kb):
    """
    Evalúa la regla cuyo valor es una expresión lógica con variables de la KB.
    """
    expr = kb.get(nombre, None)
    if expr is None:
        return f"'{nombre}' no existe en la base de conocimiento."
    
    # Sustituye las variables en la expresión
    for var in kb:
        if isinstance(kb[var], bool):
            expr = expr.replace(var, str(kb[var]))
    try:
        resultado = eval(expr)
        return f"{nombre} → {resultado}"
    except:
        return f"Error al evaluar la regla '{nombre}'"

# --- Mostrar todos los hechos y reglas evaluadas ---
print("Estado actual de la Base de Conocimiento:")
for clave in base_conocimiento:
    if isinstance(base_conocimiento[clave], bool):
        print(f"Hecho: {clave} = {base_conocimiento[clave]}")
    else:
        print(evaluar_regla(clave, base_conocimiento))

# --- Ejemplo de inferencia manual ---
print("\nConsulta: ¿Estoy mojado si llueve y no tengo paraguas?")
print(evaluar_regla("mojado_si_llueve_y_sin_paraguas", base_conocimiento))
