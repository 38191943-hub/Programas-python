#p074-suma-mutiplos.py
# imprime los multiplos m de 1 a n y su suma, usando un ciclo for 

while True:
    print('\033[H\033[J')

    print('Imprimiendo y sumando multiplos  ')
    n= int(input('Hasta donde  ?'))
    m= int(input('Multiplos   ?'))

    cm=0
    sm=0
    
    for i in range(1,n+1):
        if i % m==0:
            print(i, end=' ')
            cm +=1
            sm += i
    print(f'\nFueron {cm} multiplos, que suman {sm}  ')
    
    if input('\n\nDesear continuar (S/N) ?').upper()=='N': break

print('\nProceso terminado' )

