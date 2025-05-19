"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Tipos de Razonamiento y Aprendizaje

Este programa ejemplifica diferentes tipos de razonamiento utilizados en
el aprendizaje automático e inteligencia artificial, mostrando cómo 
se pueden representar y diferenciar los enfoques principales:

- Razonamiento Deductivo: Parte de reglas generales para llegar a conclusiones específicas.
- Razonamiento Inductivo: Generaliza a partir de ejemplos específicos para crear reglas generales.
- Razonamiento Abductivo: Busca la mejor explicación para un conjunto de observaciones.

Además, se ejemplifican tres tipos principales de aprendizaje:

- Aprendizaje Supervisado: Se aprende a partir de datos etiquetados.
- Aprendizaje No Supervisado: Se busca encontrar patrones sin etiquetas.
- Aprendizaje por Refuerzo: Se aprende a través de la interacción y retroalimentación.

Este código no usa librerías externas para facilitar su ejecución en cualquier entorno.
"""

# Definición simple de razonamiento deductivo
def razonamiento_deductivo(reglas, hechos):
    """
    Aplica reglas lógicas a hechos dados para derivar conclusiones específicas.
    reglas: lista de tuplas (condición, consecuencia)
    hechos: conjunto de hechos iniciales
    """
    conclusiones = set()
    for cond, concl in reglas:
        # Si la condición está en los hechos, añadimos la conclusión
        if cond in hechos:
            print(f"Regla aplicada: Si {cond}, entonces {concl}")
            conclusiones.add(concl)
    return conclusiones

# Definición simple de razonamiento inductivo
def razonamiento_inductivo(ejemplos):
    """
    Generaliza una regla simple a partir de ejemplos positivos.
    ejemplos: lista de ejemplos positivos (por simplicidad, solo booleanos)
    """
    # Regla inductiva: Si la mayoría de ejemplos es True, la regla general es True
    positivos = sum(ejemplos)
    total = len(ejemplos)
    regla_general = positivos > total / 2
    print(f"Ejemplos positivos: {positivos}/{total}. Regla general inducida: {regla_general}")
    return regla_general

# Definición simple de razonamiento abductivo
def razonamiento_abductivo(observacion, hipotesis_posibles):
    """
    Selecciona la hipótesis más plausible que explica la observación.
    observacion: hecho observado
    hipotesis_posibles: lista de hipótesis posibles (tuplas: (hipótesis, probabilidad))
    """
    # Se elige la hipótesis con mayor probabilidad que explique la observación
    mejor_hipotesis = None
    mejor_prob = -1
    for hip, prob in hipotesis_posibles:
        if prob > mejor_prob:
            mejor_prob = prob
            mejor_hipotesis = hip
    print(f"Observación: {observacion}")
    print(f"Hipótesis seleccionada: {mejor_hipotesis} con probabilidad {mejor_prob}")
    return mejor_hipotesis

# Ejemplo de aprendizaje supervisado
def aprendizaje_supervisado(datos):
    """
    Aprende a clasificar datos etiquetados mediante regla simple.
    datos: lista de tuplas (entrada, etiqueta)
    """
    print("\nAprendizaje Supervisado:")
    # Simple regla: si el promedio de entradas con etiqueta True es > 0.5, clase True
    suma = 0
    cuenta = 0
    for entrada, etiqueta in datos:
        if etiqueta:
            suma += entrada
            cuenta += 1
    regla = (suma / cuenta) if cuenta > 0 else 0
    print(f"Promedio de entradas con etiqueta True: {regla:.2f}")
    return regla

# Ejemplo de aprendizaje no supervisado
def aprendizaje_no_supervisado(datos):
    """
    Encuentra un patrón básico sin etiquetas, usando agrupamiento simple.
    datos: lista de números
    """
    print("\nAprendizaje No Supervisado:")
    # Cluster simple: separar datos por si son mayores o menores que la media
    media = sum(datos) / len(datos)
    grupo1 = [x for x in datos if x <= media]
    grupo2 = [x for x in datos if x > media]
    print(f"Media de datos: {media:.2f}")
    print(f"Grupo 1 (<= media): {grupo1}")
    print(f"Grupo 2 (> media): {grupo2}")
    return grupo1, grupo2

# Ejemplo de aprendizaje por refuerzo
def aprendizaje_por_refuerzo(acciones, recompensas):
    """
    Aprende a seleccionar la mejor acción basada en recompensas recibidas.
    acciones: lista de acciones posibles
    recompensas: lista de recompensas correspondientes a acciones
    """
    print("\nAprendizaje por Refuerzo:")
    mejor_accion = None
    mejor_recompensa = float('-inf')
    for accion, recompensa in zip(acciones, recompensas):
        print(f"Acción: {accion}, Recompensa recibida: {recompensa}")
        if recompensa > mejor_recompensa:
            mejor_recompensa = recompensa
            mejor_accion = accion
    print(f"Mejor acción seleccionada: {mejor_accion} con recompensa {mejor_recompensa}")
    return mejor_accion

# ------------------------
# Ejecución de ejemplos
# ------------------------

print("=== Razonamiento Deductivo ===")
reglas = [('llueve', 'suelo mojado'), ('hace_sol', 'cielo despejado')]
hechos = {'llueve'}
conclusiones = razonamiento_deductivo(reglas, hechos)
print(f"Conclusiones deducidas: {conclusiones}\n")

print("=== Razonamiento Inductivo ===")
ejemplos = [True, True, False, True, True]
regla_general = razonamiento_inductivo(ejemplos)

print("\n=== Razonamiento Abductivo ===")
observacion = 'suelo mojado'
hipotesis_posibles = [('lluvia', 0.7), ('riego', 0.2), ('limpieza', 0.1)]
hipotesis = razonamiento_abductivo(observacion, hipotesis_posibles)

print("\n=== Aprendizaje Supervisado ===")
datos_supervisados = [(0.8, True), (0.3, False), (0.6, True), (0.1, False)]
promedio = aprendizaje_supervisado(datos_supervisados)

print("\n=== Aprendizaje No Supervisado ===")
datos_no_supervisados = [0.1, 0.4, 0.35, 0.8, 0.9]
grupo1, grupo2 = aprendizaje_no_supervisado(datos_no_supervisados)

print("\n=== Aprendizaje por Refuerzo ===")
acciones = ['avanzar', 'girar izquierda', 'girar derecha']
recompensas = [10, 5, 7]
mejor_accion = aprendizaje_por_refuerzo(acciones, recompensas)
