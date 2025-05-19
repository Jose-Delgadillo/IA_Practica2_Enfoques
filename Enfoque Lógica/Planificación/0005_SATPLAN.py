"""
Planificación Lógica Proposicional: SATPLAN (Simplificado)

Este programa ilustra el método SATPLAN para planificación:
- Se representa el problema de planificación como una fórmula lógica proposicional
- La fórmula es satisfacible si existe un plan que logre el objetivo desde el estado inicial
- El código genera proposiciones lógicas para estados y acciones en cada paso temporal
- Usa un solucionador SAT básico (backtracking) para encontrar una secuencia de acciones

NOTA: Para simplificar, aquí se muestra un ejemplo pequeño sin librerías externas.
"""

from itertools import product

# Dominio: mover caja y robot entre sala y pasillo

estados = ['robot_en_pasillo', 'robot_en_sala', 'caja_en_pasillo', 'caja_en_sala', 'puerta_abierta']
acciones = ['mover_robot_sala_a_pasillo', 'mover_robot_pasillo_a_sala', 'mover_caja_sala_a_pasillo']

# Estado inicial y objetivo
estado_inicial = {
    'robot_en_pasillo': True,
    'robot_en_sala': False,
    'caja_en_pasillo': False,
    'caja_en_sala': True,
    'puerta_abierta': True
}
objetivo = {
    'caja_en_pasillo': True
}

# Para cada paso temporal, crearemos variables proposicionales:
# Ejemplo: robot_en_pasillo@0, mover_robot_sala_a_pasillo@1, etc.

MAX_PASOS = 4  # Número máximo de pasos para encontrar plan

def var(name, step):
    """Genera nombre de variable proposicional"""
    return f"{name}@{step}"

def neg(literal):
    """Negación de literal proposicional"""
    if literal.startswith("¬"):
        return literal[1:]
    else:
        return "¬" + literal

def expr_and(*args):
    return ("AND", args)

def expr_or(*args):
    return ("OR", args)

def expr_implies(a, b):
    return ("IMPLIES", a, b)

def expr_equiv(a, b):
    return ("EQUIV", a, b)

def expr_not(a):
    return ("NOT", a)

# Funciones para traducir al lenguaje CNF simplificado para SAT
def to_cnf(expr):
    # Esta es una simplificación para propósitos didácticos
    # En un sistema real se implementaría conversión completa a CNF
    # Aquí solo vamos a manejar cláusulas simples
    # Para nuestro pequeño ejemplo, nos ahorramos esta parte
    return expr

# Restricciones del problema para SATPLAN

def generar_clausulas():
    clausulas = []

    # Inicialización: estado inicial en t=0
    for estado in estados:
        lit = var(estado, 0)
        if estado_inicial.get(estado, False):
            clausulas.append([lit])  # verdadero
        else:
            clausulas.append([neg(lit)])  # falso

    # El objetivo debe ser cierto en algún paso <= MAX_PASOS
    # Para simplificar, lo colocamos en el último paso MAX_PASOS
    for g in objetivo:
        clausulas.append([var(g, MAX_PASOS)])

    # Restricciones básicas: en cada paso, sólo puede estar el robot en un lugar
    for t in range(MAX_PASOS + 1):
        # robot_en_pasillo@t XOR robot_en_sala@t
        p1 = var('robot_en_pasillo', t)
        p2 = var('robot_en_sala', t)
        # XOR -> (p1 or p2) and not (p1 and p2)
        clausulas.append([p1, p2])  # al menos uno
        clausulas.append([neg(p1), neg(p2)])  # no ambos

        # caja_en_pasillo@t XOR caja_en_sala@t
        c1 = var('caja_en_pasillo', t)
        c2 = var('caja_en_sala', t)
        clausulas.append([c1, c2])
        clausulas.append([neg(c1), neg(c2)])

    # Acción-precondición y efectos (simplificados)
    for t in range(1, MAX_PASOS + 1):
        # Si mover_robot_sala_a_pasillo@t se realiza, entonces
        # precondiciones: robot_en_sala@t-1, puerta_abierta@t-1
        act = var('mover_robot_sala_a_pasillo', t)
        pre1 = var('robot_en_sala', t-1)
        pre2 = var('puerta_abierta', t-1)
        clausulas.append([neg(act), pre1])
        clausulas.append([neg(act), pre2])

        # Efectos: si act se realiza, robot_en_pasillo@t es verdadero, robot_en_sala@t es falso
        post1 = var('robot_en_pasillo', t)
        post2 = var('robot_en_sala', t)
        clausulas.append([neg(act), post1])
        clausulas.append([neg(act), neg(post2)])

        # Si no se realiza la acción, entonces estado no cambia (inercia)
        # Si no mover_robot_sala_a_pasillo@t, robot_en_pasillo@t == robot_en_pasillo@t-1
        # Esta parte se omite por simplicidad

    # Similar para mover_robot_pasillo_a_sala y mover_caja_sala_a_pasillo...

    # Se agregan otras restricciones de exclusión y efectos de acciones en un sistema real

    return clausulas

def satisfacible(clausulas, asignacion={}):
    """
    Algoritmo de backtracking para SAT simple.
    clausulas: lista de listas de literales (strings)
    asignacion: diccionario variable -> True/False
    """
    # Si no hay cláusulas, todo satisface
    if not clausulas:
        return asignacion

    # Si hay cláusulas vacías -> conflicto
    if any(len(c) == 0 for c in clausulas):
        return None

    # Seleccionar un literal para asignar (heurística simple: primer literal de la primera cláusula)
    for c in clausulas:
        for lit in c:
            var_name = lit[1:] if lit.startswith("¬") else lit
            if var_name not in asignacion:
                # Probar asignar True o False
                for valor in [True, False]:
                    asignacion_copia = asignacion.copy()
                    asignacion_copia[var_name] = valor

                    # Simplificar cláusulas con esta asignación
                    clausulas_simpl = []
                    for cl in clausulas:
                        if any((lit.startswith("¬") and asignacion_copia.get(lit[1:], None) == False) or
                               (not lit.startswith("¬") and asignacion_copia.get(lit, None) == True)
                               for lit in cl):
                            # La cláusula está satisfecha, no la agregamos
                            continue
                        # Eliminar literales falsos
                        nueva_cl = [l for l in cl if not
                                   ((l.startswith("¬") and asignacion_copia.get(l[1:], None) == True) or
                                    (not l.startswith("¬") and asignacion_copia.get(l, None) == False))]
                        clausulas_simpl.append(nueva_cl)

                    resultado = satisfacible(clausulas_simpl, asignacion_copia)
                    if resultado is not None:
                        return resultado
                return None

    return asignacion

def main():
    clausulas = generar_clausulas()
    print("Número de cláusulas generadas:", len(clausulas))

    solucion = satisfacible(clausulas)
    if solucion is None:
        print("No se encontró un plan SAT satisfacible.")
    else:
        print("Solución SAT encontrada:")
        pasos = []
        for t in range(1, MAX_PASOS + 1):
            for a in acciones:
                var_act = var(a, t)
                if solucion.get(var_act, False):
                    pasos.append(f"Paso {t}: {a}")

        if pasos:
            print("Plan encontrado:")
            for p in pasos:
                print(p)
        else:
            print("No se necesita realizar ninguna acción.")

if __name__ == "__main__":
    main()
