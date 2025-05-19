"""
Prácticas de Inteligencia Artificial
Enfoque: Representar el Conocimiento
Subtema: Eventos y Objetos Mentales – Creencias

Este programa implementa una representación simple de creencias como objetos mentales,
asociados a agentes que tienen una base de creencias.
También modela eventos que pueden afectar estas creencias, agregándolas o eliminándolas.

Las creencias se representan como hechos (strings), y cada agente tiene un conjunto
de creencias que puede consultar y modificar.
"""

class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.creencias = set()  # Usamos un conjunto para evitar creencias duplicadas

    def agregar_creencia(self, creencia):
        """Agrega una creencia a la base del agente"""
        self.creencias.add(creencia)
        print(f"[{self.nombre}] Nueva creencia agregada: '{creencia}'")

    def eliminar_creencia(self, creencia):
        """Elimina una creencia si existe"""
        if creencia in self.creencias:
            self.creencias.remove(creencia)
            print(f"[{self.nombre}] Creencia eliminada: '{creencia}'")
        else:
            print(f"[{self.nombre}] Creencia '{creencia}' no encontrada.")

    def tiene_creencia(self, creencia):
        """Verifica si el agente tiene una creencia"""
        return creencia in self.creencias

    def mostrar_creencias(self):
        """Imprime todas las creencias del agente"""
        print(f"\nCreencias actuales de {self.nombre}:")
        if not self.creencias:
            print("  (sin creencias)")
        else:
            for c in self.creencias:
                print(f"  - {c}")

class EventoCreencia:
    def __init__(self, descripcion, agente, accion, creencia):
        """
        Evento que modifica las creencias de un agente.
        accion: 'agregar' o 'eliminar'
        """
        self.descripcion = descripcion
        self.agente = agente
        self.accion = accion
        self.creencia = creencia

    def ejecutar(self):
        print(f"\nEvento: {self.descripcion}")
        if self.accion == "agregar":
            self.agente.agregar_creencia(self.creencia)
        elif self.accion == "eliminar":
            self.agente.eliminar_creencia(self.creencia)
        else:
            print("Acción desconocida.")

# --- Ejemplo de uso ---

# Crear un agente con creencias iniciales
agente_ana = Agente("Ana")
agente_ana.agregar_creencia("El cielo es azul")
agente_ana.agregar_creencia("La tierra es redonda")

# Mostrar creencias iniciales
agente_ana.mostrar_creencias()

# Evento: Ana recibe nueva información
evento1 = EventoCreencia(
    descripcion="Ana aprende que va a llover mañana",
    agente=agente_ana,
    accion="agregar",
    creencia="Va a llover mañana"
)
evento1.ejecutar()

# Evento: Ana olvida una creencia equivocada
evento2 = EventoCreencia(
    descripcion="Ana corrige su creencia sobre el color del cielo",
    agente=agente_ana,
    accion="eliminar",
    creencia="El cielo es azul"
)
evento2.ejecutar()

# Mostrar creencias finales
agente_ana.mostrar_creencias()
