# --p024-verificar-numero
# Verificar si un numero es positivo, negativo o es cero

import os; os.system("cls")

print("Verificar si un numero es positivo, negativo o es cero\n")
# ENTRADA 
numero = int(input("Dame un numero entero ? "))

# proceso o la toma de decisiones 
if numero ==0:
    print('El numero es CERO')
else : 
    if numero<0:
        print('El numero es NEGATIVO')
    else:
        print('El numero es POSITIVO')
        
print('\n Proceso terminado')