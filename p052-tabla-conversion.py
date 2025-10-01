# p052-tabla-conversion.py
# Muestra una tabla de conversión de Pesos a Dollar
tc = 20.71

while True:
    print('\033[H\033[J', end='')

    print("Tabla de Conversión Peso a Dollar")
    print(f'Tipo de Cambio: {tc} Pesos por Dollar')
    print("-" * 30)

    while True:
        try:
            pi = float(input("Valor inicial: "))
            pf = float(input("Valor final  : "))
        except ValueError:
            print("Por favor ingresa números válidos.")
            continue

        if (pi > 0 and pf > 0) and (pi < pf):
            break
        print("Error en los valores: asegúrate que 0 < Valor inicial < Valor final.")

 
    c = pi
    print("\nPesos\tDollar")
    print("-" * 30)
  
    while c <= pf:
        print(f'{c:.2f}\t{c / tc:.2f}')
        c += 1  
    print("-" * 30)

    res = input('Deseas Continuar (S/N)? ').strip().upper()
    if res == 'N':
        print("Saliendo...")
        break
   
