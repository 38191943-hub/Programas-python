while True:
    print('\033[H\033[J', end='')
    print('Imprime la tabla de multiplicar deseada t, hasta el multiplo n')
    while True:
        try:
            t = int(input('Que tabla quieres? '))
            n = int(input('Hasta donde la quieres? '))
        except ValueError:
            print('Error, los números deben ser enteros mayores que 0')
            continue
        if t > 0 and n > 0:
            break
        print('Error, los números deben ser mayores que 0')
    c = 1
    while c <= n:
        print(f'{t} x {c} = {t*c}')
        c += 1
    if input('Deseas Continuar (S/N)? ').strip().upper() == 'N':
        break

print("\n\nGracias por utilizar este programa...")
