# -p058-impares-ascendentes.py 
#  Se desea imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario

import os

while(True):
    os.system("cls")

    print("Imprime numeros impares del 1 a n y la suma de estos")

    n = int(input("\nHasta que numero desea imprimir ? "))
    ni = 1
    c = 0
    s = 0
    print("\nNumeros impares")
    while ni <= n:
        print(ni, end="  ")
        c += 1
        s = s + ni
        ni = 2*c+1

    if input(f"\nLa suma de los numeros impares es: {s}\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado")