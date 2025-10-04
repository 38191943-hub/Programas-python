# -p059-pares-descentes.py 
# Se desea imprimir los numeros pares desde 1000 hasta el numero que el usuarios decida (n), ademas se imprime la suman de esos numeros pares


import os

while(True):
    os.system("cls")

    print("Imprime numeros impares del 100 a n de forma descendente y la suma de estos")

    n = int(input("\nHasta que numero par desea imprimir ? "))
    np = 100
    c = 0
    s = 0

    while np >= n:
        print(np, end=" ")
        s = s + np
        np -= 2 
        
        

    if input(f"\nLa suma de los numeros pares es: {s}\nDeseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado")