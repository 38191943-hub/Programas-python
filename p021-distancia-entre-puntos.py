# DISTANCIA ENTRE 2 PUNTOS 

import math

# Programa que calcula la distancia entre dos puntos

# Coordenadas punto A
x1 = float(input("Ingresa la coordenada x del punto A: "))
y1 = float(input("Ingresa la coordenada y del punto A: "))

#  Coordenadas punto B
x2 = float(input("Ingresa la coordenada x del punto B: "))
y2 = float(input("Ingresa la coordenada y del punto B: "))

# Calcular la distancia usando la fórmula
distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Mostrar resultado
print(f"La distancia entre A({x1}, {y1}) y B({x2}, {y2}) es: {distancia:.2f}")
