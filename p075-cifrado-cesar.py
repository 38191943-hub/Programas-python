# p075-cifrado-cesar.py
# cifra un mensaje utilizando el cifrado de cesar

# p075-cifrado-cesar.py
# Cifra un mensaje utilizando el cifrado de César

while True:
    print('\033[H\033[J')  # Limpia pantalla en terminal compatible ANSI

    print('Cifrado de un mensaje utilizando el cifrado de César')
    m_or = input('Ingresa el mensaje a cifrar: ')

    # Validar desplazamiento
    while True:
        try:
            des = int(input('Desplazamiento (número): '))
            break
        except ValueError:
            print("⚠ Debes ingresar un número entero.")

    men_ci = ""

    for caracter in m_or:
        if caracter.isalpha() and ('a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'):
            codigo_ascii = ord(caracter)
            base = ord('a') if caracter.islower() else ord('A')
            codigo_nuevo = base + (codigo_ascii - base + des) % 26
            men_ci += chr(codigo_nuevo)
        else:
            men_ci += caracter  # Deja espacios, signos, ñ, acentos y números sin cambios

    print(f'\nMensaje original : {m_or}')
    print(f'Mensaje cifrado  : {men_ci}')

    if input('\n¿Deseas continuar (S/N)? ').upper().startswith("N"):
        break

print('\nProceso terminado...')



