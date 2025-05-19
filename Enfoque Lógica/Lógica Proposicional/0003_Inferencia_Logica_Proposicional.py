"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Lógica Proposicional: Inferencia

Este programa ilustra un proceso básico de inferencia lógica proposicional.
La inferencia permite derivar nuevas conclusiones a partir de una base de conocimiento (KB),
usando reglas como el modus ponens:  
    Si A → B y A es verdadero, entonces B también lo es.  

Aquí implementamos una forma muy simple de inferencia basada en reglas explícitas, sin usar librerías externas.
"""
# --- Base de conocimiento como reglas (implicaciones) y hechos ---
reglas = [
    ("llueve", "suelo_mojado"),              # si llueve entonces el suelo está mojado
    ("suelo_mojado", "resbaloso"),           # si el suelo está mojado entonces es resbaloso
    ("tengo_paraguas", "no_mojado"),         # si tengo paraguas entonces no estoy mojado
    ("no_mojado", "feliz"),                  # si no estoy mojado, entonces soy feliz
]

hechos = {"llueve"}  # Hechos iniciales conocidos como verdaderos

# --- Función para aplicar inferencia usando Modus Ponens ---
def inferir(reglas, hechos):
    nuevos = True
    inferidos = set(hechos)  # Copia de los hechos para no modificarlos directamente
    
    while nuevos:
        nuevos = False
        for antecedente, consecuente in reglas:
            if antecedente in inferidos and consecuente not in inferidos:
                inferidos.add(consecuente)
                nuevos = True
                print(f"Inferido: si '{antecedente}' entonces '{consecuente}' → '{consecuente}' es verdadero")
    return inferidos

# --- Aplicar inferencia y mostrar resultados ---
resultado = inferir(reglas, hechos)

print("\nHechos finales conocidos después de la inferencia:")
for hecho in resultado:
    print(f"- {hecho}")
