import numeros
import os


farmacia = numeros.farmacia()
cosmeticos = numeros.cosmeticos()
perfumeria = numeros.perfumeria()


def menu():
    os.system("cls")
    print("""!Bienvenido a la farmacia!
    ¿A qué área desea dirigirse?
        [1] - Farmacia
        [2] - Cosmeticos
        [3] - Perfumeria
        [4] - Salir
        """)


def validar_respuesta():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            return opcion
        except:
            print("Debes seleccionar un entero, intenta denuevo.\n")


def validar_rango(min,max):
    opcion = validar_respuesta()
    while opcion < min or opcion > max:
        print("Opción inválida, intente denuevo. \n")
        opcion = validar_respuesta()
    return opcion


def menu_accion(opcion):
    if opcion == 1:
        numeros.decorador_ticket(farmacia)
    if opcion == 2:
        numeros.decorador_ticket(cosmeticos)
    if opcion == 3:
        numeros.decorador_ticket(perfumeria)


if __name__ == "__main__":
    while True:
        menu()
        opcion = validar_rango(1,4)
        menu_accion(opcion)
        if opcion == 4:
            break






