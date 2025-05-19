"""
Prácticas de Inteligencia Artificial  
Enfoque: Lógica  
Subtema: Encadenamiento hacia adelante y hacia atrás

Este programa implementa dos métodos clásicos de inferencia lógica:
- Encadenamiento hacia adelante (Forward Chaining): aplica reglas para derivar nuevos hechos desde los conocidos.
- Encadenamiento hacia atrás (Backward Chaining): trata de probar una meta trabajando hacia atrás desde ella, usando reglas disponibles.

Ambos enfoques se usan en sistemas expertos y motores de inferencia para deducir conclusiones a partir de una base de conocimiento.
"""
# Representamos hechos como strings y reglas como tuplas: (antecedentes, consecuente)
# Donde 'antecedentes' es una lista de hechos requeridos para deducir 'consecuente'.

# Base de conocimiento
hechos_iniciales = ['llueve', 'tengo_paraguas']
reglas = [
    (['llueve', 'tengo_paraguas'], 'no_me_mojo'),
    (['no_me_mojo'], 'llego_seco'),
    (['llego_seco', 'puntual'], 'feliz'),
    (['me_dormi'], 'no_puntual'),
    (['no_puntual'], 'no_feliz')
]

# -----------------------------
# Encadenamiento hacia adelante
# -----------------------------
def encadenamiento_adelante(hechos, reglas):
    hechos = set(hechos)  # Para búsqueda eficiente
    nuevos = True
    while nuevos:
        nuevos = False
        for antecedentes, consecuente in reglas:
            if all(a in hechos for a in antecedentes) and consecuente not in hechos:
                hechos.add(consecuente)
                print(f"✅ Se deduce: {consecuente} a partir de {antecedentes}")
                nuevos = True
    return hechos

# -----------------------------
# Encadenamiento hacia atrás
# -----------------------------
def encadenamiento_atras(meta, hechos, reglas, nivel=0):
    indent = "  " * nivel
    print(f"{indent}¿Se puede probar: {meta}?")

    if meta in hechos:
        print(f"{indent}✅ {meta} está en los hechos iniciales.")
        return True

    for antecedentes, consecuente in reglas:
        if consecuente == meta:
            print(f"{indent}🔁 Intentando con regla: {antecedentes} → {consecuente}")
            if all(encadenamiento_atras(submeta, hechos, reglas, nivel + 1) for submeta in antecedentes):
                print(f"{indent}✅ Regla satisfecha para {meta}")
                return True

    print(f"{indent}❌ No se puede probar {meta}")
    return False

# -----------------------------
# Ejecución
# -----------------------------
print("----- Encadenamiento hacia adelante -----")
hechos_finales = encadenamiento_adelante(hechos_iniciales, reglas)
print("\nHechos deducidos:", hechos_finales)

print("\n----- Encadenamiento hacia atrás -----")
# Intentamos probar una meta final
meta = 'feliz'
resultado = encadenamiento_atras(meta, hechos_iniciales, reglas)
print(f"\n¿Se puede deducir '{meta}'?: {'✅ Sí' if resultado else '❌ No'}")
