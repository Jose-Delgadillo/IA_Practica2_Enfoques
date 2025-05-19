"""
Prácticas de Inteligencia Artificial
Enfoque: Representar el Conocimiento
Subtema: Reglas, Redes Semánticas y Lógica Descriptiva

Este programa ilustra la representación del conocimiento utilizando:
- Reglas de producción para razonamiento basado en condiciones
- Redes semánticas para representar relaciones entre conceptos
- Lógica descriptiva para definir clases y sus propiedades

Se incluye un motor simple de inferencia basado en reglas, una estructura para redes semánticas,
y una simulación básica de lógica descriptiva con clases y restricciones.
"""

# ---------------------------
# Definición de la Red Semántica
# ---------------------------
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.relaciones = {}  # Diccionario: relación -> lista de nodos relacionados

    def agregar_relacion(self, tipo_relacion, nodo_objetivo):
        """Agrega una relación desde este nodo hacia otro"""
        if tipo_relacion not in self.relaciones:
            self.relaciones[tipo_relacion] = []
        self.relaciones[tipo_relacion].append(nodo_objetivo)

    def mostrar(self):
        print(f"Nodo: {self.nombre}")
        for rel, nodos in self.relaciones.items():
            nombres = [n.nombre for n in nodos]
            print(f"  {rel} -> {nombres}")

# ---------------------------
# Motor simple de reglas
# ---------------------------
class MotorReglas:
    def __init__(self):
        self.hechos = set()  # hechos conocidos (strings)
        self.reglas = []     # lista de reglas (funciones)

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)
        print(f"Hecho agregado: {hecho}")

    def agregar_regla(self, regla_func):
        self.reglas.append(regla_func)

    def inferir(self):
        """Aplica reglas hasta que no se generen nuevos hechos"""
        cambios = True
        while cambios:
            cambios = False
            for regla in self.reglas:
                nuevos_hechos = regla(self.hechos)
                for hecho in nuevos_hechos:
                    if hecho not in self.hechos:
                        print(f"Inferencia: {hecho}")
                        self.hechos.add(hecho)
                        cambios = True

# ---------------------------
# Representación sencilla de Lógica Descriptiva
# ---------------------------
class Clase:
    def __init__(self, nombre, propiedades=None):
        self.nombre = nombre
        self.propiedades = propiedades if propiedades else {}  # {propiedad: tipo}

    def describir(self):
        print(f"Clase {self.nombre} con propiedades:")
        for prop, tipo in self.propiedades.items():
            print(f" - {prop}: {tipo}")

# ---------------------------
# Ejemplo de uso
# ---------------------------

# 1. Crear nodos y relaciones para la red semántica
nodo_animal = Nodo("Animal")
nodo_perro = Nodo("Perro")
nodo_gato = Nodo("Gato")
nodo_animal.agregar_relacion("tipo", nodo_perro)
nodo_animal.agregar_relacion("tipo", nodo_gato)
nodo_perro.agregar_relacion("sonido", Nodo("Ladrido"))
nodo_gato.agregar_relacion("sonido", Nodo("Maullido"))

print("=== Red Semántica ===")
nodo_animal.mostrar()
nodo_perro.mostrar()
nodo_gato.mostrar()

# 2. Crear motor de reglas e insertar hechos y reglas
motor = MotorReglas()
motor.agregar_hecho("es_perro(Fido)")
motor.agregar_hecho("es_gato(Misu)")

# Regla: Si es perro, entonces es animal
def regla_perro_a_animal(hechos):
    nuevos = set()
    for hecho in hechos:
        if hecho.startswith("es_perro("):
            nuevo_hecho = "es_animal(" + hecho[8:]
            nuevos.add(nuevo_hecho)
    return nuevos

# Regla: Si es gato, entonces es animal
def regla_gato_a_animal(hechos):
    nuevos = set()
    for hecho in hechos:
        if hecho.startswith("es_gato("):
            nuevo_hecho = "es_animal(" + hecho[7:]
            nuevos.add(nuevo_hecho)
    return nuevos

motor.agregar_regla(regla_perro_a_animal)
motor.agregar_regla(regla_gato_a_animal)

print("\n=== Motor de Reglas: Inferencia ===")
motor.inferir()
print("\nHechos finales:")
for h in motor.hechos:
    print(" -", h)

# 3. Lógica descriptiva: definición de clases
clase_animal = Clase("Animal", {"tiene_patas": "int", "es_mamifero": "bool"})
clase_perro = Clase("Perro", {"raza": "str", "es_fiel": "bool"})

print("\n=== Lógica Descriptiva ===")
clase_animal.describir()
clase_perro.describir()
