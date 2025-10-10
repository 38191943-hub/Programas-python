# - suma de potencias .py 
# suma las potencias de un numero x desde x^1 hasta x ^n

print("\033[H\033[J")

print ("-- suma de potencias --\n")
x=float(input(" introduce el valor de x :  "))
n= int(input("Introduce el numero de terminos (n): "))
s_t = 0
print(f"\nCalculando serie S =x^1+...+x^{n}")

# bucle ext pra cada termino de la serie 
for i in range(1,n+1):
    t_a=1

    #bucle inter pra cada termino de la serie 
    for j in range(i):
        t_a += x
        print(f"termino {i}:{x}^{i} ={t_a}")
    s_t += t_a
        
print(f"\nEl resultado de la serie es:{s_t}")

