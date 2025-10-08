# - p071-arriba-abajo.py
# imprime numeros de 1 a n o de 1 a n , segun eliga el usuario, usando el ciclo for 

while True:
    print('\033[H\033[J')

    print('imprimir numeros usando un ciclo for - Arriba o Abajo ')
    print('[ 1 ] Arriba de 1 a n')
    print('[ 2 ] Abajo de n a 1 ')
    op= int(input('Elige ? '))

    

    if op==1:
        print('\nImprime numeros de 1 a n')
        n = int(input('\nLimite ? '))
        for i in range (1,n):
           print(i, end=' ' )
        print('\n\n')
    elif  op==2:
        print('\nImprime numeros de n a 1')
        n = int(input('\nLimite ? '))
        for i in range (n,0,-1):
           print(i, end=' ' )
        print('\n\n')
    else:
        print('\n\nOpcion Invalida') 


    if input('\n\nDesear continuar (S/N)').upper()=='N': break

print('\nProceso terminado' )