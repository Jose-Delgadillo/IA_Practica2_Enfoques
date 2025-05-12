"""
Prácticas de Inteligencia Artificial
Iteración de Políticas en MDP

Este algoritmo encuentra una política óptima para un entorno donde:
- Los estados tienen transiciones probabilísticas.
- Cada acción puede llevar a diferentes estados con distintas recompensas.
"""

# ======================== DEFINICIÓN DEL MDP ==========================

estados = ['A', 'B', 'C']
acciones = ['izquierda', 'derecha']

# Transiciones: estado -> acción -> lista de (probabilidad, siguiente_estado, recompensa)
transiciones = {
    'A': {
        'derecha': [(1.0, 'B', 5)],
        'izquierda': [(1.0, 'A', 0)]
    },
    'B': {
        'derecha': [(1.0, 'C', 10)],
        'izquierda': [(1.0, 'A', 0)]
    },
    'C': {
        'derecha': [(1.0, 'C', 0)],  # Estado terminal
        'izquierda': [(1.0, 'B', 0)]
    }
}

# Factor de descuento
gamma = 0.9

# Valor inicial de todos los estados
valores = {s: 0 for s in estados}

# Política inicial: arbitraria
politica = {s: 'izquierda' for s in estados}


# ======================== EVALUACIÓN DE POLÍTICA ==========================

def evaluar_politica(politica, valores, max_iter=100, umbral=0.01):
    for _ in range(max_iter):
        delta = 0
        nuevos_valores = valores.copy()
        for estado in estados:
            accion = politica[estado]
            suma = 0
            for prob, siguiente_estado, recompensa in transiciones[estado][accion]:
                suma += prob * (recompensa + gamma * valores[siguiente_estado])
            nuevos_valores[estado] = suma
            delta = max(delta, abs(valores[estado] - suma))
        valores.update(nuevos_valores)
        if delta < umbral:
            break
    return valores


# ======================== MEJORA DE POLÍTICA ==========================

def mejorar_politica(valores, politica):
    estable = True
    for estado in estados:
        mejor_valor = float('-inf')
        mejor_accion = politica[estado]
        for accion in acciones:
            if accion in transiciones[estado]:
                suma = 0
                for prob, siguiente_estado, recompensa in transiciones[estado][accion]:
                    suma += prob * (recompensa + gamma * valores[siguiente_estado])
                if suma > mejor_valor:
                    mejor_valor = suma
                    mejor_accion = accion
        if mejor_accion != politica[estado]:
            politica[estado] = mejor_accion
            estable = False
    return politica, estable


# ======================== ITERACIÓN DE POLÍTICAS ==========================

def iteracion_politicas():
    global valores
    while True:
        valores = evaluar_politica(politica, valores)
        politica_mejorada, estable = mejorar_politica(valores, politica)
        if estable:
            break
    return politica_mejorada, valores


# ======================== EJECUCIÓN ==========================

politica_optima, valores_optimos = iteracion_politicas()

# ======================== RESULTADOS ==========================

print("===== Iteración de Políticas Finalizada =====")
print("\nPolítica óptima encontrada:")
for estado in estados:
    print(f" - En estado {estado}: tomar acción -> {politica_optima[estado]}")

print("\nValores óptimos de los estados:")
for estado in estados:
    print(f" - Estado {estado}: Valor = {valores_optimos[estado]:.2f}")
