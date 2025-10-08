# p073-suma-promedio-numeros.py
# suma y promedia n numero introducidos por el usuarios 

while True:
    print('\033[H\033[J')
    print('sumando y promediando numeros ')
    
    n= int(input('Cuantas calificaciones ?'))
    
    s=0
    numeros=""
    for i in range(1,n+1):
        c = int(input(f'Calificacion {i} : '))
        s+= c
        numeros = numeros + str(c) + ' '

    print (f'Las calificaciones fueron : {numeros}') 
    print (f'la suma es : {s}')  
    print(f'El promedio es: {s/n}')  





    if input('\n\nDesear continuar (S/N) ?').upper()=='N': break

print('\nProceso terminado' )
