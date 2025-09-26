# Programa para convertir horas a días, minutos y segundos

# Pedir la cantidad de horas al usuario
horas = int(input("Ingresa la cantidad de horas: "))

# Cálculos
dias = horas // 24
minutos = horas * 60
segundos = horas * 60 * 60

# Salida
print(f"{horas} horas equivalen a:")
print(f"- {dias} día(s)")
print(f"- {minutos} minutos")
print(f"- {segundos} segundos")
