#--p027-calcular-paga-extra.py
# Calculo la paga de un trabajador considerando las horas extras (se paga doble)

print('\033[2J\033^[H')
print('Calculando la paga extra de un trabajador')

# Entrada 
print('Introduce los datos del trabajo')
nombre = input('Nombre ? ')
horas = int(input('Horas trabajadas ?'))
paga_hora = float(input('Paga por hora ? '))

# proceso 
horas_normales = 30
horas_extras = 0
paga_normal = 0
paga_extras = 0
total = 0

if horas <= horas_normales:
    paga_normal = horas * paga_hora
    total = paga_normal
else:
    paga_normal = horas_normales * paga_hora
    horas_extras = horas - horas_normales
    paga_extras = horas_extras * ( paga_hora * 2)
    total = paga_normal + paga_extras

print('\nCalculo completo')
print(f'{nombre} trabajo {horas} horas, a una paga de {paga_hora} pesos por hora, ')
print(f'Paga normal       : $ {paga_normal:13,.2f}')
print(f'Paga extra       : $ {paga_extras:13,.2f}')
print(f'Total       : $ {total:13,.2f}')
