# -p077-triangulo-caracter.py
# Imprime un triangulo rectangulo de caracteres 

print ('\033[H\033[J')

n = int(input(" Cuantos renglones deseas tener en el Triangulo ? - -  "))
c = input(" Caracter deseas utilizar ? - - ")

print("\n--- Triangulo Generado --- ")

# Bucle ext : controla filas 
for i in range(1, n+1):
    # Bucle inter: control columnas 

    for j in range(i):
        print(c,end="")

    print()  
       
print("\nProceso terminado...")   