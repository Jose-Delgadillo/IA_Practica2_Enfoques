"""
Prácticas de Inteligencia Artificial
Valor de la Información (VOI): ¿Vale la pena obtener más información?
"""

# Decisiones posibles
decisiones = ['Llevar Paraguas', 'No Llevar Paraguas']

# Probabilidad de que llueva
prob_lluvia = 0.3
prob_no_lluvia = 1 - prob_lluvia

# Utilidades según el caso
utilidades = {
    ('Llevar Paraguas', True): 5,
    ('Llevar Paraguas', False): -1,
    ('No Llevar Paraguas', True): -10,
    ('No Llevar Paraguas', False): 10
}

# Calcula utilidad esperada sin información adicional
def utilidad_esperada(decision):
    return (
        prob_lluvia * utilidades[(decision, True)] +
        prob_no_lluvia * utilidades[(decision, False)]
    )

# Encuentra la mejor decisión sin información
mejor_decision = max(decisiones, key=utilidad_esperada)
utilidad_sin_info = utilidad_esperada(mejor_decision)

# Utilidad con información perfecta (sabemos si lloverá o no antes de decidir)
# Si llueve, tomamos la mejor decisión en ese caso
mejor_lluvia = max(decisiones, key=lambda d: utilidades[(d, True)])
mejor_no_lluvia = max(decisiones, key=lambda d: utilidades[(d, False)])

utilidad_con_info = (
    prob_lluvia * utilidades[(mejor_lluvia, True)] +
    prob_no_lluvia * utilidades[(mejor_no_lluvia, False)]
)

# Valor de la información
valor_info = utilidad_con_info - utilidad_sin_info

# Mostrar resultados
print("===== Valor de la Información =====")
print(f"Utilidad esperada sin información: {utilidad_sin_info}")
print(f"Utilidad esperada con información perfecta: {utilidad_con_info}")
print(f"Valor de la Información: {valor_info:.2f}")
