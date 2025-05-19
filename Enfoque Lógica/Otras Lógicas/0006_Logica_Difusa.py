"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógica Difusa

Este programa integra y muestra por separado los tres subtemas:
1. Conjuntos Difusos
2. Inferencia Difusa
3. Fuzzy CLIPS (simulado en Python puro)
"""

# ---------- 1. CONJUNTOS DIFUSOS ----------

def frio(x):
    if x <= 10:
        return 1.0
    elif 10 < x < 20:
        return (20 - x) / 10.0
    else:
        return 0.0

def caliente(x):
    if x <= 20:
        return 0.0
    elif 20 < x < 30:
        return (x - 20) / 10.0
    else:
        return 1.0

def calef_alta(x):
    if x <= 5:
        return 1.0
    elif 5 < x < 10:
        return (10 - x) / 5.0
    else:
        return 0.0

def calef_baja(x):
    if x <= 0:
        return 0.0
    elif 0 < x < 5:
        return x / 5.0
    else:
        return 1.0

# ---------- 2. INFERENCIA DIFUSA ----------

def inferir_calefaccion(temp):
    grado_frio = frio(temp)
    grado_caliente = caliente(temp)

    calef_alta_salida = grado_frio
    calef_baja_salida = grado_caliente

    salida_total = (
        calef_alta_salida * 8 +
        calef_baja_salida * 2
    )
    suma_grados = calef_alta_salida + calef_baja_salida

    if suma_grados == 0:
        return 0
    return salida_total / suma_grados

# ---------- 3. "Fuzzy CLIPS" SIMULADO ----------

def fuzzy_clips_simulado(temp):
    reglas = []

    if frio(temp) > 0.0:
        reglas.append("SI temperatura ES fría ENTONCES calefacción ES alta")
    if caliente(temp) > 0.0:
        reglas.append("SI temperatura ES caliente ENTONCES calefacción ES baja")

    return reglas

# ---------- FUNCIÓN GENERAL ----------

def mostrar_todo(temp):
    print(f"\n🌡️  Temperatura actual: {temp}°C")
    
    # 1. Conjuntos Difusos
    print("\n📘 1. Conjuntos Difusos:")
    print(f" - Pertenencia a 'frío': {frio(temp):.2f}")
    print(f" - Pertenencia a 'caliente': {caliente(temp):.2f}")

    # 2. Inferencia Difusa
    print("\n📗 2. Inferencia Difusa:")
    salida = inferir_calefaccion(temp)
    print(f" - Nivel de calefacción inferido: {salida:.2f} (rango 0 a 10)")

    # 3. Fuzzy CLIPS simulado
    print("\n📙 3. Reglas Fuzzy CLIPS activadas:")
    reglas = fuzzy_clips_simulado(temp)
    if reglas:
        for r in reglas:
            print(f"   ✅ {r}")
    else:
        print("   ❌ No se activó ninguna regla.")

# ---------- PRUEBAS ----------

print("Sistema de Control Difuso: Temperatura → Calefacción")
print("=" * 60)
for t in [5, 15, 25, 35]:
    mostrar_todo(t)
    print("-" * 60)
