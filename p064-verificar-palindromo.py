# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se
# lee igual de izquierda a derecha que de derecha a izquierda

continuar = "S"

while continuar == "S":
    num = input("Introduce un número para verificar si es palíndromo: ")

    # Un número es palíndromo si su representación en string es igual a su reverso
    if num == num[::-1]:
        print(f"El número {num} es un palíndromo.")
    else:
        print(f"El número {num} no es un palíndromo.")

    continuar = input("¿Desea continuar (S/N)? ").upper()

print("\nPrograma terminado...")
