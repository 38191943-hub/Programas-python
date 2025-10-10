# -p078-piramide-caracter.py
# Imprime una piramide de caracter 

print('\033[H\033[J')
print('Imprime una piramide caracteres')

a = int(input("Ingresa la altura de la piramide:  "))
c = input("Ingresa el caracter para la piramide ")

print("\n-- Piramide Genereada --- ")

# bucle exterior pra nivel de la piramide
for i in range(1,a + 1):

    #Cal espacio y caracteres pra el nivel actual
    e = a - i
    car = 2 * i - 1

    # Prime bucle inter :impri los espacios en blanco a izquierda
    for j in  range (e):
        print(" ",end="")

    # Sgundo bucle interior :imprim los caracter
    for k in range(car):
        print(c, end="")

    # salto de linea siguiente nivel
    print()     