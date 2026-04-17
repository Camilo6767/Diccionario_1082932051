def agregar_contacto(directorio):
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    email = input("Email: ").strip()
    telefono = input("Teléfono: ").strip()
    ciudad = input("Ciudad: ").strip()

    directorio[nombre] = {
        "email": email,
        "teléfono": telefono,
        "ciudad": ciudad,
    }
    print(f"Contacto '{nombre}' agregado.")


def ver_contactos(directorio):
    if not directorio:
        print("El directorio está vacío.")
        return

    print("\nContactos:")
    for nombre, datos in directorio.items():
        print(f"- {nombre}")
        for campo, valor in datos.items():
            print(f"    {campo.capitalize()}: {valor}")
    print()


def buscar_contacto(directorio):
    nombre = input("Nombre a buscar: ").strip()
    contacto = directorio.get(nombre)
    if contacto is None:
        print(f"No se encontró el contacto '{nombre}'.")
        return

    print(f"\nDatos de {nombre}:")
    for campo, valor in contacto.items():
        print(f"{campo.capitalize()}: {valor}")
    print()


def actualizar_telefono(directorio):
    nombre = input("Nombre del contacto a actualizar: ").strip()
    if nombre not in directorio:
        print(f"No se encontró el contacto '{nombre}'.")
        return

    nuevo_telefono = input("Nuevo teléfono: ").strip()
    directorio[nombre]["teléfono"] = nuevo_telefono
    print(f"Teléfono de '{nombre}' actualizado.")


def eliminar_contacto(directorio):
    nombre = input("Nombre del contacto a eliminar: ").strip()
    eliminado = directorio.pop(nombre, None)
    if eliminado is None:
        print(f"No se encontró el contacto '{nombre}'.")
    else:
        print(f"Contacto '{nombre}' eliminado.")


def mostrar_menu():
    print("\nDirectorio de Contactos")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar por nombre")
    print("4. Actualizar teléfono")
    print("5. Eliminar contacto")
    print("6. Salir")


def main():
    directorio = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_contacto(directorio)
        elif opcion == "2":
            ver_contactos(directorio)
        elif opcion == "3":
            buscar_contacto(directorio)
        elif opcion == "4":
            actualizar_telefono(directorio)
        elif opcion == "5":
            eliminar_contacto(directorio)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
