"""
Prácticas de Inteligencia Artificial
Enfoque: Lógica
Subtema: Otras Lógicas – Lógica Difusa

Este programa integra tres conceptos clave de la lógica difusa:

1. Conjuntos Difusos:
   Se definen funciones de pertenencia que devuelven un grado entre 0 y 1.
   Por ejemplo, la temperatura 15°C puede pertenecer en 0.5 al conjunto "frío".

2. Inferencia Difusa:
   Se aplican reglas lógicas difusas del tipo:
   - SI temperatura ES fría ENTONCES calefacción ES alta
   - SI temperatura ES caliente ENTONCES calefacción ES baja

   Se usa un método tipo Mamdani con reglas simples para inferir la salida.

3. Fuzzy CLIPS (simulado):
   No se usa el motor real de CLIPS, pero se simula un sistema de reglas
   con conjuntos difusos y salidas aproximadas.

Todo implementado en Python puro, sin módulos externos.
"""

# ---------- 1. CONJUNTOS DIFUSOS ----------

# Función de pertenencia difusa para "frío"
def frio(x):
    if x <= 10:
        return 1.0
    elif 10 < x < 20:
        return (20 - x) / 10.0
    else:
        return 0.0

# Función de pertenencia difusa para "caliente"
def caliente(x):
    if x <= 20:
        return 0.0
    elif 20 < x < 30:
        return (x - 20) / 10.0
    else:
        return 1.0

# Función de pertenencia para "calefacción alta"
def calef_alta(x):
    if x <= 5:
        return 1.0
    elif 5 < x < 10:
        return (10 - x) / 5.0
    else:
        return 0.0

# Función de pertenencia para "calefacción baja"
def calef_baja(x):
    if x <= 0:
        return 0.0
    elif 0 < x < 5:
        return x / 5.0
    else:
        return 1.0

# ---------- 2. INFERENCIA DIFUSA ----------

# Sistema difuso tipo Mamdani simplificado
def inferir_calefaccion(temp):
    # Grado de pertenencia a los conjuntos
    grado_frio = frio(temp)
    grado_caliente = caliente(temp)

    # Reglas difusas:
    # 1) SI temperatura ES fría → calefacción alta
    # 2) SI temperatura ES caliente → calefacción baja

    # Inferencia: combinar mínimos
    calef_alta_salida = grado_frio  # activación de la regla 1
    calef_baja_salida = grado_caliente  # activación de la regla 2

    # Agregación: promedio ponderado (método del centroide simplificado)
    salida_total = (
        calef_alta_salida * 8 +  # centro de "alta" es 8
        calef_baja_salida * 2    # centro de "baja" es 2
    )
    suma_grados = calef_alta_salida + calef_baja_salida

    if suma_grados == 0:
        return 0  # no se activa ninguna regla
    return salida_total / suma_grados

# ---------- 3. "Fuzzy CLIPS" SIMULADO ----------

def fuzzy_motor(temp):
    print(f"\n💡 Temperatura actual: {temp}°C")
    print(f"- Grado de 'frío': {frio(temp):.2f}")
    print(f"- Grado de 'caliente': {caliente(temp):.2f}")

    resultado = inferir_calefaccion(temp)
    print(f"🔥 Nivel de calefacción recomendado (0-10): {resultado:.2f}")

# ---------- PRUEBAS ----------

print("Simulación de lógica difusa para control de calefacción")
print("=" * 60)
for temperatura in [5, 10, 15, 20, 25, 30, 35]:
    fuzzy_motor(temperatura)
