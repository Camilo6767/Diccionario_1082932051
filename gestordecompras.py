def agregar_articulo(lista_compras):
    producto = input("Nombre del producto: ").strip()
    if not producto:
        print("Producto no puede estar vacío.")
        return

    try:
        precio = float(input("Precio: ").strip())
        cantidad = int(input("Cantidad: ").strip())
    except ValueError:
        print("Precio debe ser un número y cantidad un entero.")
        return

    articulo = {
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad,
    }
    lista_compras.append(articulo)
    print(f"Artículo '{producto}' agregado.")


def ver_lista_compras(lista_compras):
    if not lista_compras:
        print("La lista de compras está vacía.")
        return

    print("\nLista de compras:")
    for indice, articulo in enumerate(lista_compras, start=1):
        print(f"{indice}. {articulo['producto']}")
        for clave, valor in articulo.items():
            if clave != "producto":
                print(f"   {clave.capitalize()}: {valor}")
    print()


def calcular_total(lista_compras):
    total = 0
    for articulo in lista_compras:
        total += articulo["precio"] * articulo["cantidad"]
    print(f"Total de la compra: {total:.2f}")


def eliminar_articulo(lista_compras):
    if not lista_compras:
        print("La lista de compras está vacía.")
        return

    nombre = input("Nombre del producto a eliminar: ").strip()
    for articulo in lista_compras:
        if articulo["producto"].lower() == nombre.lower():
            lista_compras.remove(articulo)
            print(f"Artículo '{articulo['producto']}' eliminado.")
            return

    print(f"No se encontró el producto '{nombre}'.")


def mostrar_menu():
    print("\nGestor de Compras")
    print("1. Agregar artículo")
    print("2. Ver lista de compras")
    print("3. Calcular total")
    print("4. Eliminar artículo")
    print("5. Salir")


def main():
    lista_compras = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_articulo(lista_compras)
        elif opcion == "2":
            ver_lista_compras(lista_compras)
        elif opcion == "3":
            calcular_total(lista_compras)
        elif opcion == "4":
            eliminar_articulo(lista_compras)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
