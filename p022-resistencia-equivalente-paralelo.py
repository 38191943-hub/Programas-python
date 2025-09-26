# Programa  calcular la resistencia total de 3 resistencias e paralelo

# Solicitar valores resistencias 
R1 = float(input("Ingresa el valor de la resistencia R1 (ohmios): "))
R2 = float(input("Ingresa el valor de la resistencia R2 (ohmios): "))
R3 = float(input("Ingresa el valor de la resistencia R3 (ohmios): "))


# Calcular resistencia paralelo
Rt = 1 / ((1/R1) + (1/R2) + (1/R3) )

# Resultado
print(f"La resistencia total equivalente es: {Rt:.2f} ohmios")
