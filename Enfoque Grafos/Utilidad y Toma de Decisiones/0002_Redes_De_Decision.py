"""
Prácticas de Inteligencia Artificial
Redes de Decisión: Selección de decisión basada en utilidad esperada
"""

# Posibles decisiones
decisiones = ['Llevar Paraguas', 'No Llevar Paraguas']

# Probabilidad de que llueva
prob_lluvia = 0.3  # 30% de probabilidad de lluvia

# Utilidades:
# (decisión, llueve): utilidad
utilidades = {
    ('Llevar Paraguas', True): 5,     # Comodidad con paraguas bajo la lluvia
    ('Llevar Paraguas', False): -1,   # Molestia innecesaria si no llueve
    ('No Llevar Paraguas', True): -10, # Te mojas si no llevas paraguas
    ('No Llevar Paraguas', False): 10  # Comodidad sin paraguas y sin lluvia
}

# Calculamos utilidad esperada de cada decisión
def utilidad_esperada(decision):
    u_lluvia = utilidades[(decision, True)] * prob_lluvia
    u_no_lluvia = utilidades[(decision, False)] * (1 - prob_lluvia)
    return u_lluvia + u_no_lluvia

# Mostrar utilidades esperadas
print("===== Utilidades Esperadas =====")
mejor_decision = None
mejor_utilidad = float('-inf')

for decision in decisiones:
    ue = utilidad_esperada(decision)
    print(f"Decisión: {decision} → Utilidad esperada: {ue}")
    
    if ue > mejor_utilidad:
        mejor_utilidad = ue
        mejor_decision = decision

# Mostrar la mejor decisión
print("\n===== Mejor Decisión =====")
print(f"Debes elegir: {mejor_decision} con utilidad esperada: {mejor_utilidad}")
