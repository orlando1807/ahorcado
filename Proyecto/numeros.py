def decorador_ticket(categoria):
    print("Su turno es:")
    print(next(categoria))
    print("Aguarde y será atendido")
    continuar()


def continuar():
    auxiliar = input("Presione enter para continuar:")


def perfumeria():
    i = 1
    while True:
        yield f"P- {i}"
        i += 1


def farmacia():
    i = 1
    while True:
        yield f"F- {i}"
        i += 1


def cosmeticos():
    i = 1
    while True:
        yield f"C- {i}"
        i += 1


