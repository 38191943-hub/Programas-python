# -suma-200.py
# Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, 
# luego mostrar cuantos números fueron introducidos y la suma de estos. 

import os

while True:
    os.system("cls")
    print("Imprime la suma y la cantidad de numeros introducidos cuando la suma >= 200")

    numeros_introducidos = 0
    s = 0

    while s < 200:
        num = int(input("Introduce un número: "))
        numeros_introducidos += 1
        s += num

    print(f"\nLa suma es {s}")
    print(f"Se introdujeron un total de {numeros_introducidos} números")

    if input("\n¿Deseas continuar (S/N)? ").upper().startswith("N"):
        break

print("\nProceso terminado ...")
