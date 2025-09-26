# --p029-calculodora-descuento.py
# Simula una calculadora de descuentos en base al monto de compra 

compra= descuento = porcentaje = toal = 0.0

print('\033[2J\033^[H')
print('Calculadora de descuentos')

compra = float(input('Ingresar el total de la compra: $  '))

if compra>2000:
    procentaje = 0.20
else:
    if compra > 1000:
        procentaje = 0.10
    else:
        if  compra> 500:
            procentaje = 0.5
        else:
            procentaje = 0

descuento = compra * procentaje
total= compra - descuento

print('Resumen Final')
print(f'Total de la compra.          : {compra} ')
print(f'Porcentaje de descuento      : {procentaje:.5f} ')
print(f'Descuento                    : {descuento} ')
print(f'Total a pagar                : {total} ')

print('\nProceso terminado ')