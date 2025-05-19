"""
Prácticas de Inteligencia Artificial
Aprendizaje Inductivo: Espacio de Versiones y Algoritmo AQ

Este código implementa una versión simplificada del algoritmo AQ,
un método de aprendizaje inductivo que explora el espacio de versiones
de hipótesis para encontrar descripciones conceptuales consistentes con
los datos de entrenamiento.

El espacio de versiones está formado por todas las hipótesis que pueden
ser generalizaciones o especificaciones basadas en los atributos de los datos.

Este ejemplo utiliza Python puro, sin librerías externas, y trabaja con
atributos categóricos para facilitar su comprensión y ejecución.
"""

def es_compatible(hipotesis, ejemplo):
    """
    Verifica si una hipótesis es compatible con un ejemplo dado.
    Una hipótesis es una lista de condiciones por atributo, donde
    un valor puede ser un valor específico o '?' que significa "cualquier valor".
    """
    for h_attr, e_attr in zip(hipotesis, ejemplo):
        if h_attr != '?' and h_attr != e_attr:
            return False
    return True

def generalizar_hipotesis(hipotesis, ejemplo):
    """
    Generaliza la hipótesis para incluir el ejemplo dado.
    Cambia cada atributo que no coincide por '?' para permitir más casos.
    """
    nueva_hipotesis = []
    for h_attr, e_attr in zip(hipotesis, ejemplo):
        if h_attr == e_attr or h_attr == '?':
            nueva_hipotesis.append(h_attr)
        else:
            nueva_hipotesis.append('?')
    return nueva_hipotesis

def especificar_hipotesis(hipotesis, ejemplo, atributo_index, dominio):
    """
    Especifica la hipótesis en el índice del atributo dado,
    excluyendo el valor que no coincide con el ejemplo.
    Esto se usa para eliminar ejemplos negativos.
    """
    hipotesis_especificadas = []
    for valor in dominio:
        if valor != ejemplo[atributo_index]:
            nueva = hipotesis[:]
            nueva[atributo_index] = valor
            hipotesis_especificadas.append(nueva)
    return hipotesis_especificadas

def algoritmo_aq(datos, etiquetas, dominios):
    """
    Implementación simple del algoritmo AQ.
    datos: lista de ejemplos (listas de atributos)
    etiquetas: lista con la clase positiva o negativa ('+' o '-')
    dominios: lista con los posibles valores para cada atributo
    """
    # Inicializamos el conjunto de hipótesis con la hipótesis más específica posible
    S = [['?' for _ in range(len(datos[0]))]]  # conjunto de hipótesis generales (version space)
    G = [ ['?' for _ in range(len(datos[0]))] ]  # conjunto de hipótesis específicas (en este ejemplo simplificado solo usamos S)
    
    for i, ejemplo in enumerate(datos):
        if etiquetas[i] == '+':
            # Para ejemplos positivos: generalizar hipótesis que no cubren el ejemplo
            nuevas_S = []
            for h in S:
                if es_compatible(h, ejemplo):
                    nuevas_S.append(h)
                else:
                    nueva = generalizar_hipotesis(h, ejemplo)
                    nuevas_S.append(nueva)
            S = nuevas_S
        else:
            # Para ejemplos negativos: especificar hipótesis para excluir el ejemplo
            nuevas_S = []
            for h in S:
                if es_compatible(h, ejemplo):
                    # especificar hipótesis para excluir ejemplo negativo
                    for attr_idx in range(len(h)):
                        if h[attr_idx] == '?':
                            nuevas_S.extend(especificar_hipotesis(h, ejemplo, attr_idx, dominios[attr_idx]))
                else:
                    # hipótesis ya excluye el ejemplo negativo
                    nuevas_S.append(h)
            # Actualizamos S eliminando duplicados
            # Para evitar explosión, aquí hacemos set de tuplas
            S = []
            seen = set()
            for hip in nuevas_S:
                t = tuple(hip)
                if t not in seen:
                    seen.add(t)
                    S.append(hip)
    
    return S

# Datos de ejemplo
datos = [
    ['soleado', 'calor', 'alta', 'fuerte'],
    ['soleado', 'calor', 'alta', 'débil'],
    ['nublado', 'calor', 'alta', 'fuerte'],
    ['lluvioso', 'templado', 'alta', 'fuerte'],
    ['lluvioso', 'frío', 'normal', 'fuerte'],
    ['lluvioso', 'frío', 'normal', 'débil'],
    ['nublado', 'frío', 'normal', 'débil'],
    ['soleado', 'templado', 'alta', 'fuerte'],
    ['soleado', 'frío', 'normal', 'fuerte'],
    ['lluvioso', 'templado', 'normal', 'fuerte'],
    ['soleado', 'templado', 'normal', 'débil'],
    ['nublado', 'templado', 'alta', 'débil'],
    ['nublado', 'calor', 'normal', 'fuerte'],
    ['lluvioso', 'templado', 'alta', 'débil'],
]

etiquetas = ['+', '+', '+', '+', '-', '-', '-', '+', '-', '+', '+', '+', '+', '-']

# Dominio de cada atributo para especificación
dominios = [
    ['soleado', 'nublado', 'lluvioso'],  # tiempo
    ['calor', 'templado', 'frío'],       # temperatura
    ['alta', 'normal'],                  # humedad
    ['fuerte', 'débil']                  # viento
]

# Ejecutar algoritmo AQ
hipotesis_finales = algoritmo_aq(datos, etiquetas, dominios)

# Imprimir hipótesis resultantes
print("Hipótesis compatibles con los datos positivos y excluyen negativos:")
for i, h in enumerate(hipotesis_finales):
    print(f"Hipótesis {i+1}: {h}")
