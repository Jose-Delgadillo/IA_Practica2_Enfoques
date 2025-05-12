import random
import matplotlib.pyplot as plt

# Probabilidad condicional para la lluvia
# P(Lluvia en t | Lluvia en t-1)
P_lluvia_dado_lluvia = 0.7
P_lluvia_dado_no_lluvia = 0.3
P_no_lluvia_dado_lluvia = 0.3
P_no_lluvia_dado_no_lluvia = 0.7

# Probabilidad condicional para la temperatura
# Temperatura alta y baja dependiendo de si hay lluvia o no
P_temperatura_alta_dado_lluvia = 0.3
P_temperatura_baja_dado_lluvia = 0.7
P_temperatura_alta_dado_no_lluvia = 0.8
P_temperatura_baja_dado_no_lluvia = 0.2

# Inicialización: probabilidad inicial de lluvia y temperatura
P_lluvia_inicial = 0.5
P_temperatura_alta_inicial = 0.6

# Inicializamos las listas para almacenar los resultados
dias = 20
temperaturas = []
lluvias = []

# Simulamos la evolución del clima durante varios días
lluvia = random.random() < P_lluvia_inicial  # Día 1: lluvia o no
temperatura = random.random() < P_temperatura_alta_inicial  # Día 1: temperatura alta o baja

# Inicializamos los primeros valores
lluvias.append(lluvia)
temperaturas.append(temperatura)

# Simulamos los siguientes días basados en la probabilidad de transición
for dia in range(1, dias):
    # Actualizamos la probabilidad de lluvia para el siguiente día
    if lluvias[dia - 1]:
        prob_lluvia = P_lluvia_dado_lluvia
    else:
        prob_lluvia = P_lluvia_dado_no_lluvia

    lluvia = random.random() < prob_lluvia
    lluvias.append(lluvia)

    # Actualizamos la probabilidad de temperatura para el siguiente día
    if lluvias[dia]:
        prob_temperatura_alta = P_temperatura_alta_dado_lluvia
    else:
        prob_temperatura_alta = P_temperatura_alta_dado_no_lluvia

    temperatura = random.random() < prob_temperatura_alta
    temperaturas.append(temperatura)

# Convertimos las temperaturas a un formato legible (Alta: 1, Baja: 0)
temperaturas = ['Alta' if t else 'Baja' for t in temperaturas]
lluvias = ['Lluvia' if l else 'No Lluvia' for l in lluvias]

# Imprimir los resultados
for dia in range(dias):
    print(f"Día {dia + 1}: Lluvia: {lluvias[dia]}, Temperatura: {temperaturas[dia]}")

# Graficamos los resultados
plt.figure(figsize=(10, 5))
plt.plot(range(1, dias + 1), [1 if t == 'Alta' else 0 for t in temperaturas], label='Temperatura Alta (1) / Baja (0)', color='b')
plt.ylabel('Temperatura (1 = Alta, 0 = Baja)')
plt.xlabel('Días')
plt.title('Evolución de la Temperatura en los Días')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()
