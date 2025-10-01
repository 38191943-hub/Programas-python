# p053-conjetura-collatz.py
# Calcula la conjetura de Collatz
# collatz.py
# Programa que imprime la sucesión de Collatz para un número positivo
while True:
    # limpiar pantalla (funciona en muchas terminales)
    print('\033[H\033[J', end='')

    print('Imprime la conjetura de Collatz')
    # pedir número positivo con validación
    while True:
        try:
            num = int(input('Dame un número = '))
        except ValueError:
            print('Error: debes introducir un número entero.')
            continue
        if num > 0:
            break
        print('Error: el número debe ser mayor que 0.')

    # imprimir la sucesión
    print('\nLa conjetura de Collatz es:')
    print(num, end=' ')
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        print(num, end=' ')
    print()  # salto de línea al terminar la sucesión

    # preguntar si desea continuar
    res = input('\nDeseas Continuar (S/N)? ').strip().upper()
    if res == 'N':
        print('\nGracias por usar este programa. Vuelve pronto.')
        break
    # si responde otra cosa, el loop principal vuelve a iniciar
