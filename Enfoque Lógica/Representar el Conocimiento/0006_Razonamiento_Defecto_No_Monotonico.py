"""
Prácticas de Inteligencia Artificial
Enfoque: Razonamiento
Subtema: Razonamiento por Defecto y No Monotónico

Este programa muestra un ejemplo simple de razonamiento por defecto,
donde ciertas conclusiones se asumen en ausencia de evidencia en contra,
y cómo el razonamiento es no monotónico, es decir, nuevas evidencias pueden
hacer retractar conclusiones previas.

Simulamos hechos, reglas por defecto, y actualización del conocimiento.
"""

# Representación sencilla del conocimiento
hechos = set()
conclusiones = set()

# Reglas por defecto definidas como funciones
def regla_default_pajaro_puede_volar(hechos, conclusiones):
    """
    Regla por defecto: Los pájaros pueden volar, 
    salvo que haya evidencia de que no pueden (ej. pingüino)
    """
    nuevos = set()
    for hecho in hechos:
        if hecho.startswith("es_pajaro("):
            animal = hecho[10:-1]
            # Solo añadimos si no hay evidencia contraria
            if f"no_puede_volar({animal})" not in hechos:
                nuevo = f"puede_volar({animal})"
                if nuevo not in conclusiones:
                    print(f"[Por defecto] Se asume que {animal} puede volar")
                    nuevos.add(nuevo)
    return nuevos

def razonamiento_no_monotonico():
    """
    Ejemplo de razonamiento no monotónico:
    1) Inicialmente asumimos que Tweety (un pájaro) puede volar.
    2) Luego aparece evidencia que Tweety es un pingüino (no puede volar).
    3) Se retracta la conclusión previa.
    """
    global hechos, conclusiones

    # Paso 1: conocemos que Tweety es un pájaro
    hechos.add("es_pajaro(Tweety)")
    conclusiones |= regla_default_pajaro_puede_volar(hechos, conclusiones)

    print("\nConclusiones tras aplicar regla por defecto:")
    for c in conclusiones:
        print(" -", c)

    # Paso 2: aparece nueva evidencia, Tweety es un pingüino
    hechos.add("es_pinguino(Tweety)")
    hechos.add("no_puede_volar(Tweety)")

    # Se debe retractar la conclusión anterior, pues no puede volar
    if "puede_volar(Tweety)" in conclusiones:
        print("\n[Actualización] Nueva evidencia contra puede_volar(Tweety)")
        conclusiones.remove("puede_volar(Tweety)")

    print("\nConclusiones tras nueva evidencia (razonamiento no monotónico):")
    for c in conclusiones:
        print(" -", c)

if __name__ == "__main__":
    razonamiento_no_monotonico()
