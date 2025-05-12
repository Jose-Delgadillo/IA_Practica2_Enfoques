"""
Prácticas de Inteligencia Artificial
Teoría de Juegos: Equilibrio de Nash en el Juego de la Prisión
"""

# Resultados del juego de la prisión
# Las recompensas son las siguientes:
# (Cooperar, Cooperar) -> (3, 3) -> Ambos ganan 3 puntos
# (Cooperar, Traicionar) -> (0, 5) -> El que coopera pierde, el que traiciona gana 5 puntos
# (Traicionar, Cooperar) -> (5, 0) -> El que traiciona gana 5 puntos, el que coopera pierde
# (Traicionar, Traicionar) -> (1, 1) -> Ambos pierden 1 punto

# Definimos las estrategias de los jugadores
jugador_1 = ['Cooperar', 'Traicionar']
jugador_2 = ['Cooperar', 'Traicionar']

# Matriz de recompensas
recompensas = {
    ('Cooperar', 'Cooperar'): (3, 3),
    ('Cooperar', 'Traicionar'): (0, 5),
    ('Traicionar', 'Cooperar'): (5, 0),
    ('Traicionar', 'Traicionar'): (1, 1)
}

# Función para obtener el resultado del juego
def jugar(jugador_1_elegido, jugador_2_elegido):
    return recompensas[(jugador_1_elegido, jugador_2_elegido)]

# Buscar el equilibrio de Nash: ninguno de los jugadores quiere cambiar su estrategia si el otro no cambia la suya
def equilibrio_nash():
    # Comprobamos todas las combinaciones de jugadas
    for jugada_1 in jugador_1:
        for jugada_2 in jugador_2:
            resultado_1, resultado_2 = jugar(jugada_1, jugada_2)
            # Si jugador 1 no puede mejorar su resultado cambiando su jugada
            if (jugada_1 == 'Cooperar' and resultado_1 >= jugar('Traicionar', jugada_2)[0]) or \
               (jugada_1 == 'Traicionar' and resultado_1 >= jugar('Cooperar', jugada_2)[0]):
                # Si jugador 2 no puede mejorar su resultado cambiando su jugada
                if (jugada_2 == 'Cooperar' and resultado_2 >= jugar(jugada_1, 'Traicionar')[1]) or \
                   (jugada_2 == 'Traicionar' and resultado_2 >= jugar(jugada_1, 'Cooperar')[1]):
                    print(f"Equilibrio de Nash encontrado: \nJugador 1 elige {jugada_1} \nJugador 2 elige {jugada_2}")
                    return

# Ejecutar la búsqueda del equilibrio de Nash
equilibrio_nash()
