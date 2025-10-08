# p072-suma-pares-impares.py
# imprimir numero pares e inpares, y su suma , el usuario elige 
while True:
    print('\033[H\033[J')

    print('Imprimir numeros pares o impares ascendente y su suma  ')
    print('[ 1 ] Pares ')
    print('[ 2 ] Impares ')
    op= int(input('Elige ? '))

    s=0

    if op==1:
        print('\nImprimiendo numeros pares y su suma ')
        n = int(input('\nLimite ? '))
        for i in range (2,n+1,2):
           print(i, end=' ' )
           s += i
        print('\nSuma de pares: ' +str(s))
    elif  op==2:
        print('\nImprimiendo inpares')
        n = int(input('\nLimite ? '))
        for i in range (1,n+1,2):
           print(i, end=' ' )
        print('\nSuma de impares: ' + str(s))
    else:
        print('\n\nOpcion Invalida') 


    if input('\n\nDesear continuar (S/N) ?').upper()=='N': break

print('\nProceso terminado' )