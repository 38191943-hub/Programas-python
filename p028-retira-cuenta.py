#-- p028-retira-cuenta.py
# simula el retiro de dinero de una cuenta de ahorros revisa el saldo 

saldo_actual = 15000.00
print('Simulacion de retiro ')
print('\033[2J\033^[H')
print(f'Tu saldo inicial es de {saldo_actual:.2f} ')

cantidad_retiro = float(input('Cantidad a retirar :  $ '))

if cantidad_retiro > 0:
    if cantidad_retiro <= saldo_actual:
        print('Iniciando retiro..')
        saldo_actual -= cantidad_retiro
        print('\nRetiro exitoso')
        print(f' Tu saldo nuevo es : {saldo_actual:-2f}')
    else:
        print('\n Fondos insuficientes para completar la transaccion')
else:
    print('\nLa cantidad a retirar debe ser un numero positivo ')

print('\nProceso termindo...')