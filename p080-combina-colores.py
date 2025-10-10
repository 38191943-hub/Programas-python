# - combina-colores.py 
# genera combinacion de dos colores a partir de una lista 

print(" --- Generador de combinacion de colores--\n")

# usuario que ingrese los colores y crear una lista 
colores = input("Ingresa los colores separados por comas ").strip().split(',')

print (f"\n Colore base: {colores}")
print("--- Combinacion Posibles---")

# bucle exterior: tome el timer color 
for color1 in colores:

    # toma de el segundo color 
    for color2 in colores:

        # Condiciones para evitar combinar un color consigo mismo 
        if color1 != color2:
            print(f"- {color1} y {color2} ")


