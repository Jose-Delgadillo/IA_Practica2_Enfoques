"""
Prácticas de Inteligencia Artificial
Enfoque: Representar el Conocimiento
Subtema: Acciones, Situaciones y Eventos – Marcos

Este programa implementa un sistema básico de Marcos (Frames).
Los marcos son estructuras para representar conocimiento organizado sobre
situaciones, eventos y acciones en un contexto determinado.
Un marco puede contener atributos (slots) con valores, y relaciones con otros marcos.

Ejemplo:
Un marco "Situación de compra" puede tener slots para comprador, vendedor, objeto,
precio y estado de la compra.
"""

# ---------- DEFINICIÓN DE LA CLASE MARCO ----------

class Marco:
    def __init__(self, nombre):
        self.nombre = nombre         # Nombre del marco
        self.slots = {}              # Diccionario de slots (atributos)
        self.relaciones = {}         # Relaciones con otros marcos (opcional)

    def set_slot(self, slot, valor):
        """Asignar valor a un slot"""
        self.slots[slot] = valor

    def get_slot(self, slot):
        """Obtener valor de un slot, devuelve None si no existe"""
        return self.slots.get(slot, None)

    def add_relacion(self, nombre_relacion, marco_objeto):
        """Agregar relación con otro marco"""
        self.relaciones[nombre_relacion] = marco_objeto

    def mostrar(self, nivel=0):
        """Imprimir el marco y sus slots, con indentación para claridad"""
        indent = "  " * nivel
        print(f"{indent}Marco: {self.nombre}")
        for slot, valor in self.slots.items():
            if isinstance(valor, Marco):
                print(f"{indent}  {slot}:")
                valor.mostrar(nivel + 2)
            else:
                print(f"{indent}  {slot}: {valor}")
        for relacion, marco_rel in self.relaciones.items():
            print(f"{indent}  Relación {relacion}:")
            marco_rel.mostrar(nivel + 2)

# ---------- CREACIÓN DE MARCOS EJEMPLO ----------

# Marco para una acción: Comprar
accion_comprar = Marco("Acción Comprar")
accion_comprar.set_slot("actor", "Cliente")
accion_comprar.set_slot("objeto", "Libro")
accion_comprar.set_slot("precio", 25)
accion_comprar.set_slot("estado", "Pendiente")

# Marco para una situación: Tienda
situacion_tienda = Marco("Situación Tienda")
situacion_tienda.set_slot("nombre", "Librería Central")
situacion_tienda.set_slot("ubicación", "Av. Principal 123")

# Marco para un evento: Transacción de Compra
evento_transaccion = Marco("Evento Transacción")
evento_transaccion.add_relacion("acción", accion_comprar)
evento_transaccion.add_relacion("lugar", situacion_tienda)
evento_transaccion.set_slot("fecha", "2025-05-19")
evento_transaccion.set_slot("resultado", "Éxito")

# ---------- MOSTRAR LOS MARCOS Y SUS RELACIONES ----------

print("=" * 60)
print("🔎 Marcos: Acciones, Situaciones y Eventos")
print("=" * 60)
evento_transaccion.mostrar()
