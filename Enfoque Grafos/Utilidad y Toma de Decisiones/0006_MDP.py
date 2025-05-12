"""
Prácticas de Inteligencia Artificial
Simulación de un Proceso de Decisión de Markov (MDP)

Un MDP se define por:
- Un conjunto de estados.
- Un conjunto de acciones disponibles por estado.
- Transiciones entre estados dadas por probabilidades.
- Recompensas asociadas a cada transición.
- Un factor de descuento gamma (γ).
Este código muestra cómo funciona un MDP paso a paso.
"""

import random

# ======================== DEFINICIÓN DEL MDP ==========================

# Conjunto de estados del entorno
estados = ['S1', 'S2', 'S3']

# Conjunto de acciones posibles por estado
acciones = {
    'S1': ['a1', 'a2'],
    'S2': ['a1', 'a2'],
    'S3': []  # S3 es un estado terminal
}

# Transiciones: estado -> acción -> lista de (probabilidad, siguiente_estado, recompensa)
transiciones = {
    'S1': {
        'a1': [(0.8, 'S1', -1), (0.2, 'S2', 0)],
        'a2': [(1.0, 'S2', 0)]
    },
    'S2': {
        'a1': [(1.0, 'S3', 10)],
        'a2': [(1.0, 'S1', -1)]
    },
    'S3': {}  # Sin transiciones desde el estado terminal
}

# Factor de descuento (gamma): valora más las recompensas cercanas que las futuras
gamma = 0.9


# ======================== EJECUCIÓN DE SIMULACIÓN ==========================

def ejecutar_mdp(estado_inicial, politica, pasos_max=10):
    """
    Simula una trayectoria en el MDP desde un estado inicial usando una política fija.
    """
    estado = estado_inicial
    total_recompensa = 0
    camino = [estado]

    print("\n--- Simulación de trayectoria MDP ---")
    for paso in range(pasos_max):
        if estado not in politica or not acciones[estado]:
            print(f"Estado {estado} es terminal.")
            break

        accion = politica[estado]
        posibles = transiciones[estado][accion]

        # Elegir transición basada en probabilidad
        transicion = random.choices(posibles, weights=[p for p, _, _ in posibles])[0]
        prob, nuevo_estado, recompensa = transicion

        total_recompensa += recompensa * (gamma ** paso)
        estado = nuevo_estado
        camino.append(estado)

        print(f"Paso {paso+1}: acción '{accion}', recompensa {recompensa}, nuevo estado -> {estado}")

        if not acciones[estado]:  # Estado terminal
            break

    print(f"\nTrayectoria seguida: {camino}")
    print(f"Recompensa total descontada: {total_recompensa:.2f}")
    return camino, total_recompensa


# ======================== DEFINICIÓN DE POLÍTICA ==========================

# Política fija: indica qué acción tomar en cada estado
politica = {
    'S1': 'a1',
    'S2': 'a1'
    # S3 no tiene acción porque es terminal
}

# ======================== PRUEBA ==========================

estado_inicial = 'S1'
camino, recompensa = ejecutar_mdp(estado_inicial, politica)
