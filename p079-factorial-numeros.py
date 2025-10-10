# p079-facotrial-numero.py 
# calcular el factorial de n numeros 

# Imprim el factorial de los numeros desde 1 hasta n 
print ("Calculo sucesivos Factoriales--\n")

try:
        n = int(input(" Hasta que numero desas calcular Factorial ? "))
        #bucle ext :iera cada numero (1,2,3..,n)
        for i in range(1,n +1 ):
            
                factorial = 1 # Reiniciamos el factorial para cada numero nuevo 

                #Bucle interior : cal el fact de i 
                for j in range (1 , i +1):
                        factorial += j
                print(f"El factorial de {i}! es {factorial}")
except ValueError: 
        print("Error : xfavor, introduce un numero entero valido. ")