"""
Prácticas de Inteligencia Artificial
Preprocesado: Filtros

Este programa implementa un filtro simple para preprocesar datos.
Un filtro es una operación que modifica una señal para mejorarla o extraer información útil,
por ejemplo, suavizando ruido o destacando bordes en imágenes.

Aquí implementamos un filtro de media móvil (promedio) que suaviza una señal unidimensional.
"""

def filtro_media_movil(signal, window_size=3):
    """
    Aplica un filtro de media móvil a una señal.

    Parámetros:
    - signal: lista de números (la señal original)
    - window_size: tamaño de la ventana para el promedio (debe ser impar)

    Retorna:
    - lista con la señal filtrada (suavizada)
    """
    # Comprobar que window_size es impar para simetría
    if window_size % 2 == 0:
        raise ValueError("window_size debe ser impar")

    half_window = window_size // 2
    filtered_signal = []

    # Recorrer cada punto de la señal
    for i in range(len(signal)):
        # Definir los índices para ventana de promedio
        start = max(0, i - half_window)
        end = min(len(signal), i + half_window + 1)

        # Extraer la ventana de valores
        window = signal[start:end]

        # Calcular promedio de la ventana
        promedio = sum(window) / len(window)

        # Añadir valor filtrado a la lista
        filtered_signal.append(promedio)

    return filtered_signal

# --- Programa principal ---

# Señal original con ruido
senal_original = [2, 5, 8, 12, 7, 6, 10, 15, 14, 13, 10, 8, 6]

print("Señal original:")
print(senal_original)

# Aplicar filtro de media móvil con ventana de tamaño 3
senal_filtrada = filtro_media_movil(senal_original, window_size=3)

print("\nSeñal filtrada (media móvil, ventana=3):")
print(senal_filtrada)
