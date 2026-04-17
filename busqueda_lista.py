lista_numeros = [12, 45, 78, 23, 56, 89, 34, 67]

def buscar_numero(numero):
    try:
        return lista_numeros.index(numero)
    except ValueError:
        return -1


def numeros_mayores(umbral):
    return [valor for valor in lista_numeros if valor > umbral]


def promedio_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def ordenar_lista(lista):
    return sorted(lista)


def mostrar_menu():
    print("\nBúsqueda en Lista")
    print("1. Buscar número")
    print("2. Números mayores que umbral")
    print("3. Promedio de la lista")
    print("4. Ordenar lista")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            try:
                numero = int(input("Número a buscar: ").strip())
            except ValueError:
                print("Ingresa un número válido.")
                continue
            indice = buscar_numero(numero)
            if indice == -1:
                print(f"El número {numero} no está en la lista.")
            else:
                print(f"El número {numero} está en el índice {indice}.")

        elif opcion == "2":
            try:
                umbral = int(input("Umbral: ").strip())
            except ValueError:
                print("Ingresa un número válido.")
                continue
            mayores = numeros_mayores(umbral)
            print(f"Números mayores que {umbral}: {mayores}")

        elif opcion == "3":
            promedio = promedio_lista(lista_numeros)
            print(f"Promedio de la lista: {promedio:.2f}")

        elif opcion == "4":
            ordenada = ordenar_lista(lista_numeros)
            print(f"Lista ordenada: {ordenada}")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
