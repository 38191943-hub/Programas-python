# Conteo-descente-for-v2.py 
# Imprime los numeros de n a 1, en decrements de m, usando un ciclo for

print('\033[H\033[J')
print('Inicializando secuencia descendente ')

n = int(input(' Desde donde ? '))
m = int(input('De cuanto en cuanto ?'))

for f in range (n,0,-m):
    print(f,end=' ')