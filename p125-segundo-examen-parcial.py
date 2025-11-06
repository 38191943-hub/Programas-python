# p125-segundo-sxamen-parcial.py
# Segundo Examen Parcial - Computación Aplicada
# Inventario TecnoTienda
# Hecho por Braulio Ruelas 

inventario = []   # aqui voy guardando todos los productos que meta

print("TecnoTienda - Sistema de Inventario")
print("Captura de productos (* o nombre vacío para terminar)\n")

# aqui pido los datos
while True:
    nombre = input("Nombre del producto: ").strip()
    if nombre == "" or nombre == "*":
        break

    precio = float(input("Precio: "))
    categoria = input("Categoria: ")
    proveedor = input("Proveedor: ")
    stock = int(input("Stock: "))

    # cada producto va en un diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": stock
    }

    inventario.append(producto)  # lo guardo en la lista


# salida de datos crudos
print("\n3.1 DATOS (LISTA DE DICCIONARIOS):")
print(inventario)

# tabla 
print("\n3.2 TABLA DE DATOS:")
print(f"{'Nombre':20} {'Precio':>12} {'Categoria':15} {'Stock':>6} {'Proveedor':10}")
for p in inventario:
    print(f"{p['nombre']:20} {p['precio']:12,.2f} {p['categoria']:15} {p['stock']:6} {p['proveedor']:10}")

# resumen
print("\n3. RESUMEN:")

total = len(inventario)
print(f"Productos totales: {total}")

# contadores
cats = {}
provs = {}

for p in inventario:
    cats[p['categoria']] = cats.get(p['categoria'], 0) + 1
    provs[p['proveedor']] = provs.get(p['proveedor'], 0) + 1

print("Categorías:")
for c, v in cats.items():
    print(f"• {c}: {v}")

print("Proveedores:")
for pr, v in provs.items():
    print(f"• {pr}: {v}")

# stock y precios
suma_stock = sum(p['stock'] for p in inventario)
prom_stock = suma_stock / total if total > 0 else 0

suma_precio = sum(p['precio'] for p in inventario)
prom_precio = suma_precio / total if total > 0 else 0

print(f"Stock -> Suma: {suma_stock}, Promedio: {prom_stock:.2f}")
print(f"Precio -> Suma: {suma_precio:,.2f}, Promedio: {prom_precio:,.2f}")

# mas caro / mas barato
if total > 0:
    caro = max(inventario, key=lambda x: x['precio'])
    barato = min(inventario, key=lambda x: x['precio'])
    print(f"{caro['nombre']} de {caro['precio']:,.2f} es el más caro, "
          f"{barato['nombre']} de {barato['precio']:,.2f} es el más barato.")
