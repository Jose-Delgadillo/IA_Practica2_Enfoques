"""
Prácticas de Inteligencia Artificial
Tema: Razonamiento Probabilístico - Manto de Markov

El Manto de Markov de un nodo en una Red Bayesiana es el conjunto mínimo de nodos que, 
al conocerse, hacen que el nodo sea condicionalmente independiente del resto de la red.

Este conjunto está compuesto por:
- Los padres del nodo
- Sus hijos
- Los otros padres de sus hijos
"""

# Representamos una red bayesiana simple como un diccionario de relaciones
# Nodo: [Padres]
red_bayesiana = {
    'Robo': [],
    'Terremoto': [],
    'Alarma': ['Robo', 'Terremoto'],
    'JuanLlama': ['Alarma'],
    'MariaLlama': ['Alarma']
}

def encontrar_hijos(red, nodo):
    """Devuelve los hijos directos del nodo en la red"""
    hijos = []
    for n, padres in red.items():
        if nodo in padres:
            hijos.append(n)
    return hijos

def manto_de_markov(red, nodo):
    """Calcula el manto de Markov del nodo dado"""
    padres = set(red[nodo])  # Padres del nodo
    hijos = set(encontrar_hijos(red, nodo))  # Hijos del nodo
    otros_padres = set()

    for hijo in hijos:
        otros_padres.update(red[hijo])  # Padres de los hijos

    # El manto de Markov es la unión de padres, hijos, y otros padres de los hijos
    return padres.union(hijos).union(otros_padres - {nodo})

# Ejemplo: obtener el manto de Markov del nodo 'Alarma'
nodo_objetivo = 'Alarma'
manto = manto_de_markov(red_bayesiana, nodo_objetivo)

# Mostrar resultados
print("======= Manto de Markov =======")
print(f"Nodo objetivo: {nodo_objetivo}")
print(f"Manto de Markov: {sorted(manto)}")
